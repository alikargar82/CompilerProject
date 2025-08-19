from mcp.server.fastmcp import FastMCP
import yaml
import json
import csv
import io
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import re

mcp = FastMCP("WorldHistoryCourse")

# Data structures
@dataclass
class StudentProgress:
    student_id: str
    name: str
    current_chapter: int
    completed_chapters: List[str]
    quiz_scores: Dict[str, int]
    last_activity: str

@dataclass
class QuizSession:
    student_id: str
    quiz_id: str
    current_question: int
    answers: List[Any]
    score: int
    max_score: int

# Global storage (in production, this would be a database)
student_data: Dict[str, StudentProgress] = {}
active_quiz_sessions: Dict[str, QuizSession] = {}

# Course configuration (parsed from YAML)
course_config = {
    "Title": "Introduction to World History",
    "Instructor": "Dr. Eleanor Vance",
    "Settings": {
        "ShowScoreboard": False,
        "AllowStudentDiscussion": True
    },
    "chapters": {
        "ch1_preface": {
            "Title": "Course Preface",
            "order": 1
        },
        "ch2_renaissance": {
            "Title": "The Renaissance", 
            "order": 2,
            "quiz": "renaissance_quiz"
        },
        "roman_empire": {
            "Title": "The Roman Empire",
            "order": 3,
            "quiz": "roman_history_check"
        }
    },
    "quizzes": {
        "renaissance_quiz": {
            "Title": "Renaissance Art & Science",
            "PassingScore": 6,
            "Questions": [
                {
                    "id": "q_mona_lisa",
                    "title": "Who painted the Mona Lisa?",
                    "type": "MultipleChoice",
                    "options": [
                        {"text": "Vincent van Gogh", "isCorrect": False},
                        {"text": "Leonardo da Vinci", "isCorrect": True},
                        {"text": "Pablo Picasso", "isCorrect": False}
                    ],
                    "feedback": "Correct! Leonardo da Vinci painted the Mona Lisa in the early 16th century.",
                    "points": 2
                },
                {
                    "id": "q_galileo", 
                    "title": "What did Galileo discover using his telescope?",
                    "type": "MultipleChoice",
                    "options": [
                        {"text": "That the Earth was flat", "isCorrect": False},
                        {"text": "The moons of Jupiter", "isCorrect": True},
                        {"text": "The rings of Saturn", "isCorrect": False}
                    ],
                    "feedback": "Yes, Galileo discovered Jupiter's four largest moons, providing evidence for the heliocentric model.",
                    "points": 2
                },
                {
                    "id": "q_gutenberg",
                    "title": "What was Johannes Gutenberg's most famous invention?",
                    "type": "MultipleChoice", 
                    "options": [
                        {"text": "The telescope", "isCorrect": False},
                        {"text": "The printing press", "isCorrect": True},
                        {"text": "The compass", "isCorrect": False}
                    ],
                    "feedback": "Correct! Gutenberg invented the printing press, revolutionizing the spread of knowledge.",
                    "points": 2
                }
            ]
        },
        "roman_history_check": {
            "Title": "Roman History Check",
            "PassingScore": 7,
            "Questions": [
                {
                    "id": "q_first_emperor",
                    "title": "Who was the first Roman Emperor?",
                    "type": "MultipleChoice",
                    "options": [
                        {"text": "Julius Caesar", "isCorrect": False},
                        {"text": "Augustus", "isCorrect": True},
                        {"text": "Nero", "isCorrect": False}
                    ],
                    "feedback": "Correct! Augustus was the first Roman Emperor.",
                    "points": 5
                },
                {
                    "id": "q2_roman_roads",
                    "title": "Why were Roman roads so important?",
                    "type": "Essay",
                    "points": 5,
                    "word_count": {"min": 50, "max": 200}
                }
            ]
        },
        "final_exam_quiz": {
            "Title": "Final Exam",
            "PassingScore": 15,
            "Questions": [
                {
                    "id": "q_roman_empire_fall",
                    "title": "What were the main causes of the fall of the Roman Empire?",
                    "type": "Essay",
                    "points": 3,
                    "word_count": {"min": 100, "max": 300}
                }
            ]
        }
    }
}

@mcp.tool()
def register_student(name: str, student_id: str) -> str:
    """Register a student for the course and check their progress"""
    
    # Simulate checking student database (in real implementation, this would query a Google Sheet or database)
    if student_id in student_data:
        student = student_data[student_id]
        
        # Determine next activity
        if len(student.completed_chapters) == 0:
            next_activity = "Welcome to the course! Let's start with the Course Preface."
        elif "ch1_preface" in student.completed_chapters and "ch2_renaissance" not in student.completed_chapters:
            next_activity = "Time for the Renaissance Art & Science Quiz!"
        elif "ch2_renaissance" in student.completed_chapters and "roman_empire" not in student.completed_chapters:
            next_activity = "Ready for the Roman History Check quiz!"
        else:
            next_activity = "You've completed most of the course. Ready for the Final Exam?"
        
        return f"Welcome back, {student.name}! Based on your records, you've completed chapters: {', '.join(student.completed_chapters)}. {next_activity}"
    else:
        # New student registration
        new_student = StudentProgress(
            student_id=student_id,
            name=name,
            current_chapter=1,
            completed_chapters=[],
            quiz_scores={},
            last_activity=datetime.now().isoformat()
        )
        student_data[student_id] = new_student
        return f"Welcome to Introduction to World History, {name}! You've been registered with ID: {student_id}. Let's start with the Course Preface."

@mcp.tool()
def start_quiz(student_id: str, quiz_name: str) -> str:
    """Start a quiz for a student"""
    
    if student_id not in student_data:
        return "Please register first using your name and student ID."
    
    if quiz_name not in course_config["quizzes"]:
        return f"Quiz '{quiz_name}' not found. Available quizzes: {', '.join(course_config['quizzes'].keys())}"
    
    quiz = course_config["quizzes"][quiz_name]
    
    # Create quiz session
    session = QuizSession(
        student_id=student_id,
        quiz_id=quiz_name,
        current_question=0,
        answers=[],
        score=0,
        max_score=sum(q.get("points", 1) for q in quiz["Questions"])
    )
    active_quiz_sessions[student_id] = session
    
    # Return first question
    first_question = quiz["Questions"][0]
    question_text = f"Quiz: {quiz['Title']}\nPassing Score: {quiz['PassingScore']}\n\n"
    question_text += f"Question 1/{len(quiz['Questions'])}: {first_question['title']}\n"
    
    if first_question["type"] == "MultipleChoice":
        for i, option in enumerate(first_question["options"], 1):
            question_text += f"{i}. {option['text']}\n"
        question_text += "\nPlease respond with the number of your choice (1, 2, 3, etc.)"
    elif first_question["type"] == "Essay":
        word_count = first_question.get("word_count", {})
        if word_count:
            question_text += f"\nWord count: {word_count.get('min', 0)}-{word_count.get('max', 'unlimited')} words"
        question_text += "\nPlease provide your essay answer."
    
    return question_text

@mcp.tool()
def submit_answer(student_id: str, answer: str) -> str:
    """Submit an answer to the current quiz question"""
    
    if student_id not in active_quiz_sessions:
        return "No active quiz session. Please start a quiz first."
    
    session = active_quiz_sessions[student_id]
    quiz = course_config["quizzes"][session.quiz_id]
    current_q = quiz["Questions"][session.current_question]
    
    # Process answer based on question type
    is_correct = False
    feedback = ""
    points_earned = 0
    
    if current_q["type"] == "MultipleChoice":
        try:
            choice_idx = int(answer) - 1
            if 0 <= choice_idx < len(current_q["options"]):
                chosen_option = current_q["options"][choice_idx]
                is_correct = chosen_option["isCorrect"]
                if is_correct:
                    points_earned = current_q.get("points", 1)
                    session.score += points_earned
                feedback = current_q.get("feedback", "")
            else:
                return "Invalid choice. Please select a number corresponding to one of the options."
        except ValueError:
            return "Please provide a number (1, 2, 3, etc.) for your choice."
    
    elif current_q["type"] == "Essay":
        # For essay questions, we'll do basic word count validation
        word_count = len(answer.split())
        min_words = current_q.get("word_count", {}).get("min", 0)
        max_words = current_q.get("word_count", {}).get("max", float('inf'))
        
        if word_count < min_words:
            return f"Your answer is too short. Please provide at least {min_words} words. Current word count: {word_count}"
        elif word_count > max_words:
            return f"Your answer is too long. Please keep it under {max_words} words. Current word count: {word_count}"
        else:
            # For demo purposes, award full points for properly formatted essays
            points_earned = current_q.get("points", 1)
            session.score += points_earned
            is_correct = True
            feedback = "Thank you for your thoughtful essay response!"
    
    session.answers.append(answer)
    session.current_question += 1
    
    # Prepare response
    response = f"Answer recorded! "
    if feedback:
        response += f"{feedback} "
    response += f"Points earned: {points_earned}/{current_q.get('points', 1)}\n"
    response += f"Current score: {session.score}/{session.max_score}\n\n"
    
    # Check if quiz is complete
    if session.current_question >= len(quiz["Questions"]):
        return complete_quiz(student_id)
    else:
        # Present next question
        next_q = quiz["Questions"][session.current_question]
        response += f"Question {session.current_question + 1}/{len(quiz['Questions'])}: {next_q['title']}\n"
        
        if next_q["type"] == "MultipleChoice":
            for i, option in enumerate(next_q["options"], 1):
                response += f"{i}. {option['text']}\n"
            response += "\nPlease respond with the number of your choice."
        elif next_q["type"] == "Essay":
            word_count = next_q.get("word_count", {})
            if word_count:
                response += f"\nWord count: {word_count.get('min', 0)}-{word_count.get('max', 'unlimited')} words"
            response += "\nPlease provide your essay answer."
    
    return response

@mcp.tool()
def complete_quiz(student_id: str) -> str:
    """Complete the current quiz and update student progress"""
    
    if student_id not in active_quiz_sessions:
        return "No active quiz session found."
    
    session = active_quiz_sessions[student_id]
    quiz = course_config["quizzes"][session.quiz_id]
    student = student_data[student_id]
    
    # Calculate final results
    passing_score = quiz["PassingScore"]
    percentage = (session.score / session.max_score) * 100
    passed = session.score >= passing_score
    
    # Update student records
    student.quiz_scores[session.quiz_id] = session.score
    student.last_activity = datetime.now().isoformat()
    
    # Update chapter completion based on quiz
    if passed:
        if session.quiz_id == "renaissance_quiz" and "ch2_renaissance" not in student.completed_chapters:
            student.completed_chapters.append("ch2_renaissance")
        elif session.quiz_id == "roman_history_check" and "roman_empire" not in student.completed_chapters:
            student.completed_chapters.append("roman_empire")
    
    # Clean up session
    del active_quiz_sessions[student_id]
    
    # Prepare results message
    result_msg = f"Quiz Complete: {quiz['Title']}\n"
    result_msg += f"Final Score: {session.score}/{session.max_score} ({percentage:.1f}%)\n"
    result_msg += f"Passing Score: {passing_score}\n"
    result_msg += f"Result: {'PASSED' if passed else 'FAILED'}\n\n"
    
    if passed:
        result_msg += "Congratulations! Your progress has been updated.\n"
        
        # Suggest next activity
        if len(student.completed_chapters) == 1:
            result_msg += "Ready for the next chapter: The Roman Empire!"
        elif len(student.completed_chapters) == 2:
            result_msg += "Great progress! You're ready for the Final Exam when you are."
        else:
            result_msg += "Excellent work! You've completed the course."
    else:
        result_msg += f"You need at least {passing_score} points to pass. You can retake this quiz when ready."
    
    return result_msg

@mcp.tool()
def get_student_progress(student_id: str) -> str:
    """Get detailed progress report for a student"""
    
    if student_id not in student_data:
        return "Student not found. Please register first."
    
    student = student_data[student_id]
    
    report = f"Progress Report for {student.name} (ID: {student.student_id})\n"
    report += f"Course: {course_config['Title']}\n"
    report += f"Instructor: {course_config['Instructor']}\n\n"
    
    report += f"Completed Chapters: {len(student.completed_chapters)}/3\n"
    for chapter in student.completed_chapters:
        chapter_info = course_config["chapters"].get(chapter, {})
        report += f"  ✓ {chapter_info.get('Title', chapter)}\n"
    
    report += f"\nQuiz Scores:\n"
    for quiz_id, score in student.quiz_scores.items():
        quiz_info = course_config["quizzes"].get(quiz_id, {})
        max_score = sum(q.get("points", 1) for q in quiz_info.get("Questions", []))
        passing_score = quiz_info.get("PassingScore", 0)
        status = "PASSED" if score >= passing_score else "FAILED"
        report += f"  {quiz_info.get('Title', quiz_id)}: {score}/{max_score} ({status})\n"
    
    report += f"\nLast Activity: {student.last_activity}"
    
    return report

@mcp.tool()
def list_available_quizzes() -> str:
    """List all available quizzes in the course"""
    
    quiz_list = "Available Quizzes:\n\n"
    
    for quiz_id, quiz_info in course_config["quizzes"].items():
        quiz_list += f"• {quiz_info['Title']} (ID: {quiz_id})\n"
        quiz_list += f"  Questions: {len(quiz_info['Questions'])}\n"
        quiz_list += f"  Passing Score: {quiz_info['PassingScore']}\n\n"
    
    return quiz_list

@mcp.tool()
def get_course_info() -> str:
    """Get general information about the course"""
    
    info = f"Course: {course_config['Title']}\n"
    info += f"Instructor: {course_config['Instructor']}\n\n"
    
    info += "Course Structure:\n"
    chapters = sorted(course_config["chapters"].items(), key=lambda x: x[1].get("order", 0))
    
    for chapter_id, chapter_info in chapters:
        info += f"{chapter_info.get('order', '?')}. {chapter_info['Title']}\n"
        if "quiz" in chapter_info:
            quiz_title = course_config["quizzes"][chapter_info["quiz"]]["Title"]
            info += f"   Quiz: {quiz_title}\n"
    
    info += f"\nSettings:\n"
    info += f"  Student Discussion: {'Enabled' if course_config['Settings']['AllowStudentDiscussion'] else 'Disabled'}\n"
    info += f"  Scoreboard: {'Visible' if course_config['Settings']['ShowScoreboard'] else 'Hidden'}\n"
    
    return info

@mcp.tool()
def reset_student_progress(student_id: str) -> str:
    """Reset a student's progress (for testing purposes)"""
    
    if student_id not in student_data:
        return "Student not found."
    
    student = student_data[student_id]
    student.current_chapter = 1
    student.completed_chapters = []
    student.quiz_scores = {}
    student.last_activity = datetime.now().isoformat()
    
    # Clear any active quiz session
    if student_id in active_quiz_sessions:
        del active_quiz_sessions[student_id]
    
    return f"Progress reset for {student.name}. You can start fresh from the beginning!"

if __name__ == "__main__":
    mcp.run()