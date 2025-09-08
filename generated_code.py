from mcp.server.fastmcp import FastMCP
import json
import sqlite3
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

mcp = FastMCP("Introduction to Python Programming")

# Database setup
DB_PATH = "course_data.db"

# Course content for database population (only used during initialization)
_COURSE_CONTENT = {
  "metadata": {
    "name": "Introduction to Python Programming",
    "author": "Dr. Sarah Chen",
    "description": "Complete code examples from all course chapters",
    "level": "beginner"
  },
  "chapters": [
    {
      "type": "chapter",
      "title": "Python Data Types Hierarchy",
      "current_title": "Python Data Types Hierarchy",
      "description": "Deep dive into Python data types, conditional statements, and loops",
      "content": [
        {
          "type": "text",
          "title": "Python Data Types",
          "body": "Python has several built-in data types: integers (int), floating-point numbers (float), strings (str), booleans (bool), lists, tuples, and dictionaries. Each type serves different purposes and has unique characteristics."
        },
        {
          "type": "video",
          "title": "Working with Lists and Dictionaries",
          "url": "https://python-course.com/videos/data-structures.mp4"
        },
        {
          "type": "example",
          "title": "Working with Lists and Dictionaries",
          "code": "# Lists - ordered and mutable\\nfruits = ['apple', 'banana', 'orange']\\nfruits.append('grape')\\nprint(fruits[0])  # apple\\n\\n# Dictionaries - key-value pairs\\nstudent = {\\n    'name': 'John',\\n    'age': 20,\\n    'major': 'Computer Science'\\n}\\nprint(student['name'])  # John\\n\\n# Conditional statements\\nif student['age'] >= 18:\\n    print('Adult')\\nelse:\\n    print('Minor')\\n\\n# Loops\\nfor fruit in fruits:\\n    print(f'I like {fruit}')",
          "language": "python"
        },
        {
          "type": "video",
          "title": "Control Flow Explanation",
          "url": "https://python-course.com/audio/control-flow.mp3"
        }
      ],
      "summary": "end_scope_operator"
    },
    {
      "type": "chapter",
      "title": "Object-Oriented Programming Concepts",
      "current_title": "Object-Oriented Programming Concepts",
      "description": "Learn to write reusable code with functions and understand classes and objects",
      "content": [
        {
          "type": "text",
          "title": "Functions in Python",
          "body": "Functions are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs more modular. Functions can accept parameters and return values."
        },
        {
          "type": "video",
          "title": "Creating Your First Functions",
          "url": "https://python-course.com/videos/functions.mp4"
        },
        {
          "type": "example",
          "title": "Creating Your First Functions",
          "code": "# Function definition\\ndef greet(name, age=18):\\n    '''Greet a person with their name and age'''\\n    return f'Hello {name}, you are {age} years old!'\\n\\n# Function calls\\nmessage1 = greet('Alice', 25)\\nmessage2 = greet('Bob')  # uses default age\\nprint(message1)\\nprint(message2)\\n\\n# Class definition\\nclass Student:\\n    def __init__(self, name, major):\\n        self.name = name\\n        self.major = major\\n        self.courses = []\\n    \\n    def enroll(self, course):\\n        self.courses.append(course)\\n        return f'{self.name} enrolled in {course}'\\n\\n# Creating objects\\nstudent1 = Student('John', 'Computer Science')\\nresult = student1.enroll('Python Programming')\\nprint(result)",
          "language": "python"
        },
        {
          "type": "video",
          "title": "Object-Oriented Programming Concepts",
          "url": "https://python-course.com/audio/oop-concepts.mp3"
        }
      ],
      "summary": "end_scope_operator"
    }
  ],
  "quizzes": [
    {
      "type": "quiz",
      "title": "Python Fundamentals Quiz",
      "current_title": "Python Fundamentals Quiz",
      "instructions": "Test your understanding of Python basics. Each question is worth equal points.",
      "settings": {
        "passing_score": 80,
        "time_limit": "15m"
      },
      "questions": [
        {
          "question": "Python is a case-sensitive language",
          "answer": True,
          "hint": "Think about variable names like 'Name' vs 'name'",
          "explanation": "Python is case-sensitive, meaning 'Name' and 'name' are treated as different variables."
        },
        {
          "question": "What built-in function would you use to find the length of a list?",
          "answer": "len()",
          "hint": "It's a three-letter function",
          "explanation": "The len() function returns the number of items in a sequence or collection."
        }
      ]
    }
  ],
  "exams": [
    {
      "type": "exam",
      "title": "Python Midterm Examination",
      "current_title": "Python Midterm Examination",
      "instructions": "This exam covers chapters 1-2. You have 90 minutes to complete all questions. Show your work for coding problems.",
      "settings": {
        "passing_score": 75
      },
      "questions": [
        {
          "question": "What keyword is used to define a class in Python?",
          "answer": "class",
          "explanation": "The 'class' keyword is used to define classes in Python."
        }
      ]
    },
    {
      "type": "exam",
      "title": "Python Programming Final Exam",
      "current_title": "Python Programming Final Exam",
      "instructions": "Comprehensive final examination covering all course material. Read each question carefully and show your work.",
      "settings": {
        "passing_score": 70
      },
      "questions": [
        {
          "question": "What is the purpose of the '__init__' method in a Python class?",
          "answer": "constructor",
          "explanation": "The __init__ method is the constructor that initializes new objects when they are created."
        }
      ]
    }
  ],
  "resources": [
    {
      "type": "resource",
      "title": "Code Examples Repository",
      "current_title": "Code Examples Repository",
      "description": "Complete code examples from all course chapters",
      "materials": [
        {
          "type": "file",
          "title": "Python Quick Reference Guide",
          "path": "resources/python-quick-ref.pdf"
        },
        {
          "type": "file",
          "title": "Practice Datasets",
          "path": "data/sample-datasets.zip"
        },
        {
          "type": "file",
          "title": "Code Examples Repository",
          "path": "resources/code-examples.zip"
        }
      ],
      "content": [
        {
          "type": "video",
          "title": "Official Python Documentation",
          "url": "https://docs.python.org/3/"
        },
        {
          "type": "video",
          "title": "Python Best Practices",
          "url": "https://python-course.com/videos/best-practices.mp4"
        },
        {
          "type": "video",
          "title": "Python Package Index (PyPI)",
          "url": "https://pypi.org/"
        }
      ]
    }
  ],
  "student_data": {}
}

# Database initialization
def init_database():
    """Initialize the course database with proper relational structure and course content"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Students table - basic student information
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            current_chapter INTEGER DEFAULT 1,
            last_activity TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Chapters table - store all course chapters
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chapters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_number INTEGER UNIQUE,
            title TEXT NOT NULL,
            description TEXT,
            content TEXT,
            summary TEXT,
            objectives TEXT
        )
    """)
    
    # Quizzes table - store quiz metadata
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_number INTEGER UNIQUE,
            title TEXT NOT NULL,
            instructions TEXT,
            passing_score INTEGER DEFAULT 70,
            time_limit TEXT,
            attempts_allowed INTEGER DEFAULT 1,
            randomize_questions BOOLEAN DEFAULT FALSE
        )
    """)
    
    # Questions table - store all quiz questions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER,
            question_number INTEGER,
            question_type TEXT,
            question_text TEXT NOT NULL,
            correct_answer TEXT,
            options TEXT,
            hint TEXT,
            explanation TEXT,
            FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
        )
    """)
    
    # Exams table - store exam metadata  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_name TEXT UNIQUE,
            title TEXT NOT NULL,
            instructions TEXT,
            passing_score INTEGER DEFAULT 70,
            time_limit TEXT,
            attempts_allowed INTEGER DEFAULT 1,
            weight REAL DEFAULT 1.0
        )
    """)
    
    # Exam questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exam_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_id INTEGER,
            question_number INTEGER,
            question_type TEXT,
            question_text TEXT NOT NULL,
            correct_answer TEXT,
            options TEXT,
            hint TEXT,
            explanation TEXT,
            FOREIGN KEY (exam_id) REFERENCES exams(id)
        )
    """)
    
    # Resources table - store learning resources
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_name TEXT UNIQUE,
            title TEXT NOT NULL,
            description TEXT,
            materials TEXT
        )
    """)
    
    # Chapter progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chapter_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            chapter_number INTEGER,
            completed BOOLEAN DEFAULT FALSE,
            completion_date TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            UNIQUE(student_id, chapter_number)
        )
    """)
    
    # Quiz sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            quiz_number INTEGER,
            current_question INTEGER DEFAULT 0,
            total_questions INTEGER,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            status TEXT DEFAULT 'in_progress',
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """)
    
    # Quiz answers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            question_number INTEGER,
            student_answer TEXT,
            correct_answer TEXT,
            is_correct BOOLEAN,
            answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (session_id) REFERENCES quiz_sessions(id)
        )
    """)
    
    # Quiz scores table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            quiz_number INTEGER,
            score REAL,
            max_score REAL,
            percentage REAL,
            passed BOOLEAN,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            UNIQUE(student_id, quiz_number)
        )
    """)
    
    # Exam scores table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exam_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            exam_name TEXT,
            score REAL,
            max_score REAL,
            percentage REAL,
            passed BOOLEAN,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            UNIQUE(student_id, exam_name)
        )
    """)
    
    conn.commit()
    
    # Populate course content from _COURSE_CONTENT
    populate_course_content(cursor, conn)
    
    conn.close()

def populate_course_content(cursor, conn):
    """Populate database with course content from _COURSE_CONTENT"""
    course = _COURSE_CONTENT
    
    # Insert chapters
    for i, chapter in enumerate(course.get('chapters', []), 1):
        cursor.execute("""
            INSERT OR REPLACE INTO chapters 
            (chapter_number, title, description, content, summary, objectives)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            i,
            chapter.get('title', f'Chapter {i}'),
            chapter.get('description', ''),
            json.dumps(chapter.get('content', [])),
            chapter.get('summary', ''),
            json.dumps(chapter.get('objectives', []))
        ))
    
    # Insert quizzes and questions
    for i, quiz in enumerate(course.get('quizzes', []), 1):
        # Insert quiz
        cursor.execute("""
            INSERT OR REPLACE INTO quizzes 
            (quiz_number, title, instructions, passing_score, time_limit, attempts_allowed, randomize_questions)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            i,
            quiz.get('title', f'Quiz {i}'),
            quiz.get('instructions', ''),
            quiz.get('settings', {}).get('passing_score', 70),
            quiz.get('settings', {}).get('time_limit', ''),
            quiz.get('settings', {}).get('attempts_allowed', 1),
            quiz.get('settings', {}).get('randomize_questions', False)
        ))
        
        quiz_id = cursor.lastrowid
        
        # Insert questions for this quiz
        for j, question in enumerate(quiz.get('questions', [])):
            cursor.execute("""
                INSERT OR REPLACE INTO questions 
                (quiz_id, question_number, question_type, question_text, correct_answer, options, hint, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                quiz_id,
                j,
                question.get('type', 'multiple_choice'),
                question.get('question', ''),
                str(question.get('answer', '')),
                json.dumps(question.get('options', [])),
                question.get('hint', ''),
                question.get('explanation', '')
            ))
    
    # Insert exams and exam questions
    for exam in course.get('exams', []):
        # Insert exam
        cursor.execute("""
            INSERT OR REPLACE INTO exams 
            (exam_name, title, instructions, passing_score, attempts_allowed, weight)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            exam.get('name', exam.get('title', 'Exam')),
            exam.get('title', 'Exam'),
            exam.get('instructions', ''),
            exam.get('settings', {}).get('passing_score', 70),
            exam.get('settings', {}).get('attempts_allowed', 1),
            exam.get('settings', {}).get('weight', 1.0)
        ))
        
        exam_id = cursor.lastrowid
        
        # Insert questions for this exam
        for j, question in enumerate(exam.get('questions', [])):
            cursor.execute("""
                INSERT OR REPLACE INTO exam_questions 
                (exam_id, question_number, question_type, question_text, correct_answer, options, hint, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                exam_id,
                j,
                question.get('type', 'multiple_choice'),
                question.get('question', ''),
                str(question.get('answer', '')),
                json.dumps(question.get('options', [])),
                question.get('hint', ''),
                question.get('explanation', '')
            ))
    
    # Insert resources
    for resource in course.get('resources', []):
        cursor.execute("""
            INSERT OR REPLACE INTO resources 
            (resource_name, title, description, materials)
            VALUES (?, ?, ?, ?)
        """, (
            resource.get('name', resource.get('title', 'Resource')),
            resource.get('title', 'Resource'),
            resource.get('description', ''),
            json.dumps(resource.get('materials', []))
        ))
    
    conn.commit()

init_database()

@mcp.tool()
def register_student(name: str, student_id: str) -> str:
    """Register a student for Introduction to Python Programming"""
    # Ensure database is initialized
    init_database()
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    existing = cursor.fetchone()
    
    if existing:
        conn.close()
        return f"Welcome back, {name}! You're already registered for Introduction to Python Programming."
    else:
        cursor.execute("""
            INSERT INTO students (student_id, name, last_activity)
            VALUES (?, ?, ?)
        """, (student_id, name, datetime.now().isoformat()))
        conn.commit()
        conn.close()
        return f"Welcome to Introduction to Python Programming, {name}! Registration successful."

@mcp.tool()
def get_course_info() -> str:
    """Get comprehensive course information"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get course metadata (hardcoded since it's in the code, not database)
    course_name = "Introduction to Python Programming"
    author = "Dr. Sarah Chen"
    description = "A comprehensive course covering Python fundamentals, data structures, and object-oriented programming"
    level = "beginner"
    
    info = f"Course: {course_name}\n"
    info += f"Instructor: {author}\n"
    info += f"Description: {description}\n"
    info += f"Level: {level}\n\n"
    
    # Get chapters from database
    cursor.execute("SELECT chapter_number, title FROM chapters ORDER BY chapter_number")
    chapters = cursor.fetchall()
    
    info += "Course Structure:\n"
    for chapter_num, title in chapters:
        info += f"{chapter_num}. {title}\n"
    
    # Get quiz count
    cursor.execute("SELECT COUNT(*) FROM quizzes")
    quiz_count = cursor.fetchone()[0]
    if quiz_count > 0:
        info += f"\nQuizzes Available: {quiz_count}\n"
        
    # Get exam count  
    cursor.execute("SELECT COUNT(*) FROM exams")
    exam_count = cursor.fetchone()[0]
    if exam_count > 0:
        info += f"Exams Available: {exam_count}\n"
        
    # Get resource count
    cursor.execute("SELECT COUNT(*) FROM resources")
    resource_count = cursor.fetchone()[0]
    if resource_count > 0:
        info += f"Resources Available: {resource_count}\n"
    
    return info

@mcp.tool()
def get_chapter_content(student_id: str, chapter_number: int) -> str:
    """Get detailed content for a specific chapter"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get chapter information from database
    cursor.execute("""
        SELECT title, description, content, summary, objectives 
        FROM chapters WHERE chapter_number = ?
    """, (chapter_number,))
    
    chapter_data = cursor.fetchone()
    conn.close()
    
    if not chapter_data:
        cursor.execute("SELECT COUNT(*) FROM chapters")
        total_chapters = cursor.fetchone()[0] if cursor.fetchone() else 0
        return f"Chapter {chapter_number} does not exist. Available chapters: 1-{total_chapters}"
    
    title, description, content_json, summary, objectives_json = chapter_data
    
    content = f"# {title}\n\n"
    content += f"**Description:** {description or 'No description'}\n\n"
    
    # Parse objectives
    try:
        objectives = json.loads(objectives_json) if objectives_json else []
        if objectives:
            content += "**Learning Objectives:**\n"
            for obj in objectives:
                content += f"- {obj}\n"
            content += "\n"
    except json.JSONDecodeError:
        pass
    
    # Parse content items
    try:
        content_items = json.loads(content_json) if content_json else []
        if content_items:
            content += "**Content:**\n\n"
            for item in content_items:
                if item['type'] == 'text':
                    content += f"### {item.get('title', 'Section')}\n"
                    content += f"{item.get('body', '')}\n\n"
                elif item['type'] == 'example':
                    content += f"### {item.get('title', 'Code Example')}\n"
                    content += f"```{item.get('language', 'python')}\n"
                    content += f"{item.get('code', '').replace('\\n', chr(10))}\n"
                    content += f"```\n"
                    if 'explanation' in item:
                        content += f"*{item['explanation']}*\n\n"
                elif item['type'] == 'video':
                    content += f"### {item.get('title', 'Video')}\n"
                    content += f"Video URL: {item.get('url', '')}\n\n"
    except json.JSONDecodeError:
        content += "Content format error.\n\n"
    
    if summary:
        content += f"**Summary:**\n{summary}\n"
    
    return content

@mcp.tool()
def list_available_quizzes() -> str:
    """List all available quizzes in the course"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get all quizzes with question counts
    cursor.execute("""
        SELECT q.quiz_number, q.title, q.time_limit, q.passing_score, 
               COUNT(qs.question_number) as question_count
        FROM quizzes q
        LEFT JOIN questions qs ON q.quiz_number = qs.quiz_id
        GROUP BY q.quiz_number, q.title, q.time_limit, q.passing_score
        ORDER BY q.quiz_number
    """)
    quizzes = cursor.fetchall()
    
    if not quizzes:
        conn.close()
        return "No quizzes available in this course."
    
    quiz_list = "Available Quizzes:\n\n"
    for quiz_num, title, time_limit, passing_score, question_count in quizzes:
        quiz_list += f"{quiz_num}. {title}\n"
        quiz_list += f"   Questions: {question_count}\n"
        if time_limit:
            quiz_list += f"   Time Limit: {time_limit}\n"
        if passing_score:
            quiz_list += f"   Passing Score: {passing_score}%\n"
        quiz_list += "\n"
    
    conn.close()
    return quiz_list

@mcp.tool()
def start_quiz(student_id: str, quiz_number: int) -> str:
    """Start a quiz session for a student"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get quiz information from database
    cursor.execute("SELECT * FROM quizzes WHERE quiz_number = ?", (quiz_number,))
    quiz_data = cursor.fetchone()
    
    if not quiz_data:
        cursor.execute("SELECT COUNT(*) FROM quizzes")
        total_quizzes = cursor.fetchone()[0]
        conn.close()
        return f"Quiz {quiz_number} does not exist. Available quizzes: 1-{total_quizzes}"
    
    quiz_id, quiz_num, title, instructions, passing_score, time_limit, attempts, randomize = quiz_data
    
    # Check if student exists
    cursor.execute("SELECT student_id FROM students WHERE student_id = ?", (student_id,))
    if not cursor.fetchone():
        conn.close()
        return "Student not registered. Please register first."
    
    # Get quiz questions
    cursor.execute("""
        SELECT question_number, question_text, hint FROM questions 
        WHERE quiz_id = ? ORDER BY question_number
    """, (quiz_id,))
    questions = cursor.fetchall()
    
    if not questions:
        conn.close()
        return f"Quiz {quiz_number} has no questions available."
    
    # Check for existing active session
    cursor.execute("""
        SELECT id FROM quiz_sessions 
        WHERE student_id = ? AND quiz_number = ? AND status = 'in_progress'
    """, (student_id, quiz_number))
    
    existing_session = cursor.fetchone()
    
    if existing_session:
        # Resume existing session
        session_id = existing_session[0]
        cursor.execute("""
            SELECT current_question FROM quiz_sessions WHERE id = ?
        """, (session_id,))
        current_question = cursor.fetchone()[0]
    else:
        # Create new session
        cursor.execute("""
            INSERT INTO quiz_sessions (student_id, quiz_number, current_question, total_questions, status)
            VALUES (?, ?, ?, ?, 'in_progress')
        """, (student_id, quiz_number, 0, len(questions)))
        session_id = cursor.lastrowid
        current_question = 0
    
    conn.commit()
    conn.close()
    
    # Return current question
    if current_question < len(questions):
        question_num, question_text, hint = questions[current_question]
        response = f"**{title}**\n\n"
        response += f"{instructions}\n\n" if instructions else "Test your understanding. Each question is worth equal points.\n\n"
        response += f"**Question {current_question + 1} of {len(questions)}:**\n"
        response += f"{question_text}\n\n"
        
        if hint:
            response += f"*Hint: {hint}*\n\n"
            
        response += "Use submit_quiz_answer() to submit your answer."
        
        return response
    else:
        return f"Quiz {quiz_number} has no questions or is already completed."

@mcp.tool()
def submit_quiz_answer(student_id: str, quiz_number: int, answer: str) -> str:
    """Submit an answer to the current quiz question"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get active quiz session
    cursor.execute("""
        SELECT id, current_question, total_questions FROM quiz_sessions 
        WHERE student_id = ? AND quiz_number = ? AND status = 'in_progress'
    """, (student_id, quiz_number))
    
    session_result = cursor.fetchone()
    if not session_result:
        conn.close()
        return "No active quiz session. Use start_quiz() first."
    
    session_id, current_q, total_questions = session_result
    
    # Get quiz and question information from database
    cursor.execute("""
        SELECT q.quiz_id, qu.passing_score FROM quiz_sessions qs
        JOIN quizzes qu ON qs.quiz_number = qu.quiz_number
        JOIN questions q ON qu.id = q.quiz_id
        WHERE qs.id = ? AND q.question_number = ?
    """, (session_id, current_q))
    
    question_result = cursor.fetchone()
    if not question_result:
        conn.close()
        return "Question not found."
    
    quiz_id, passing_score = question_result
    
    # Get current question details
    cursor.execute("""
        SELECT correct_answer, explanation FROM questions 
        WHERE quiz_id = ? AND question_number = ?
    """, (quiz_id, current_q))
    
    question_data = cursor.fetchone()
    if not question_data:
        conn.close()
        return "Question data not found."
    
    correct_answer, explanation = question_data
    
    # Check if answer is correct
    if correct_answer.lower() in ['true', 'false']:
        # For boolean answers, convert user input to boolean
        user_answer_bool = answer.lower().strip() in ['true', 'yes', '1', 'correct']
        correct_answer_bool = correct_answer.lower() == 'true'
        is_correct = user_answer_bool == correct_answer_bool
    else:
        # For string answers, do case-insensitive comparison
        is_correct = answer.lower().strip() == correct_answer.lower().strip()
    
    # Store the answer
    cursor.execute("""
        INSERT INTO quiz_answers (session_id, question_number, student_answer, correct_answer, is_correct)
        VALUES (?, ?, ?, ?, ?)
    """, (session_id, current_q, answer, correct_answer, is_correct))
    
    response = f"Answer submitted: {answer}\n"
    
    if is_correct:
        response += "✓ Correct!\n"
    else:
        response += f"✗ Incorrect. The correct answer was: {correct_answer}\n"
    
    # Show explanation if available
    if explanation:
        response += f"Explanation: {explanation}\n"
    
    # Move to next question
    next_question = current_q + 1
    
    if next_question < total_questions:
        # Update session to next question
        cursor.execute("""
            UPDATE quiz_sessions SET current_question = ? WHERE id = ?
        """, (next_question, session_id))
        
        # Get next question
        cursor.execute("""
            SELECT question_text, hint FROM questions 
            WHERE quiz_id = ? AND question_number = ?
        """, (quiz_id, next_question))
        
        next_q_data = cursor.fetchone()
        if next_q_data:
            question_text, hint = next_q_data
            response += f"\n**Question {next_question + 1} of {total_questions}:**\n"
            response += f"{question_text}\n"
            if hint:
                response += f"*Hint: {hint}*\n"
    else:
        # Quiz completed - calculate score
        cursor.execute("""
            SELECT COUNT(*) as total, SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct
            FROM quiz_answers WHERE session_id = ?
        """, (session_id,))
        
        total, correct = cursor.fetchone()
        score = (correct / total * 100) if total > 0 else 0
        
        # Mark session as completed
        cursor.execute("""
            UPDATE quiz_sessions SET status = 'completed', completed_at = CURRENT_TIMESTAMP 
            WHERE id = ?
        """, (session_id,))
        
        # Store final score
        passed = score >= passing_score
        
        cursor.execute("""
            INSERT OR REPLACE INTO quiz_scores 
            (student_id, quiz_number, score, max_score, percentage, passed)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id, quiz_number, correct, total, score, passed))
        
        response += f"\n**Quiz Completed!**\n"
        response += f"Score: {correct}/{total} ({score:.1f}%)\n"
        
        if passed:
            response += "🎉 You passed!"
        else:
            response += f"You need {passing_score}% to pass. Try again!"
    
    conn.commit()
    conn.close()
    
    return response
    
    if next_question < len(quiz['questions']):
        # Update session to next question
        cursor.execute("""
            UPDATE quiz_sessions SET current_question = ? WHERE id = ?
        """, (next_question, session_id))
        
        next_q = quiz['questions'][next_question]
        response += f"\n**Question {next_question + 1} of {len(quiz['questions'])}:**\n"
        response += f"{next_q['question']}\n"
        if 'hint' in next_q:
            response += f"*Hint: {next_q['hint']}*\n"
    else:
        # Quiz completed - calculate score
        cursor.execute("""
            SELECT COUNT(*) as total, SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct
            FROM quiz_answers WHERE session_id = ?
        """, (session_id,))
        
        total, correct = cursor.fetchone()
        score = (correct / total * 100) if total > 0 else 0
        
        # Mark session as completed
        cursor.execute("""
            UPDATE quiz_sessions SET status = 'completed', completed_at = CURRENT_TIMESTAMP 
            WHERE id = ?
        """, (session_id,))
        
        # Store final score
        passing_score = quiz.get('settings', {}).get('passing_score', 70)
        passed = score >= passing_score
        
        cursor.execute("""
            INSERT OR REPLACE INTO quiz_scores 
            (student_id, quiz_number, score, max_score, percentage, passed)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id, quiz_number, correct, total, score, passed))
        
        response += f"\n**Quiz Completed!**\n"
        response += f"Score: {correct}/{total} ({score:.1f}%)\n"
        
        if passed:
            response += "🎉 You passed!"
        else:
            response += f"You need {passing_score}% to pass. Try again!"
    
    conn.commit()
    conn.close()
    
    return response

@mcp.tool()
def get_quiz_results(student_id: str, quiz_number: int) -> str:
    """Get results for a completed quiz"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if student exists
    cursor.execute("SELECT student_id FROM students WHERE student_id = ?", (student_id,))
    if not cursor.fetchone():
        conn.close()
        return "Student not registered."
    
    # Get quiz score and quiz information
    cursor.execute("""
        SELECT qs.score, qs.max_score, qs.percentage, qs.passed, qs.completed_at,
               q.title, q.passing_score
        FROM quiz_scores qs
        JOIN quizzes q ON qs.quiz_number = q.quiz_number
        WHERE qs.student_id = ? AND qs.quiz_number = ?
    """, (student_id, quiz_number))
    
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        return f"No results found for Quiz {quiz_number}. Have you completed it?"
    
    score, max_score, percentage, passed, completed_at, quiz_title, passing_score = result
    
    result_text = f"**{quiz_title} Results**\n"
    result_text += f"Score: {percentage:.1f}%\n"
    result_text += f"Status: {'PASSED' if passed else 'FAILED'}\n"
    result_text += f"Passing Score: {passing_score}%"
    
    return result_text

@mcp.tool()
def get_student_progress(student_id: str) -> str:
    """Get comprehensive student progress report"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get basic student info
    cursor.execute("SELECT name, current_chapter, last_activity, created_at FROM students WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()
    
    if not result:
        conn.close()
        return "Student not registered."
    
    name, current_chapter, last_activity, created_at = result
    
    # Get course metadata from database structure
    cursor.execute("SELECT COUNT(*) FROM chapters")
    total_chapters = cursor.fetchone()[0]
    
    report = f"**Progress Report for {name}**\n\n"
    report += f"**Course:** Introduction to Python Programming\n"
    report += f"**Enrolled:** {created_at}\n"
    report += f"**Last Activity:** {last_activity}\n\n"
    
    # Chapter progress
    cursor.execute("SELECT COUNT(*) FROM chapter_progress WHERE student_id = ? AND completed = 1", (student_id,))
    completed_chapters = cursor.fetchone()[0]
    
    report += f"**Chapter Progress:**\n"
    report += f"Current Chapter: {current_chapter}\n"
    report += f"Completed Chapters: {completed_chapters}/{total_chapters}\n\n"
    
    # Quiz scores
    cursor.execute("""
        SELECT quiz_number, percentage, passed 
        FROM quiz_scores 
        WHERE student_id = ? 
        ORDER BY quiz_number
    """, (student_id,))
    
    quiz_results = cursor.fetchall()
    
    if quiz_results:
        report += f"**Quiz Scores:**\n"
        for quiz_num, percentage, passed in quiz_results:
            status = "✅" if passed else "❌"
            report += f"Quiz {quiz_num}: {percentage:.1f}% {status}\n"
    else:
        report += f"**Quiz Scores:** No quizzes completed\n"
    
    # Overall progress
    total_quizzes = len(course['quizzes'])
    completed_quizzes = len(quiz_results)
    
    if total_quizzes > 0:
        quiz_completion = (completed_quizzes / total_quizzes) * 100
        report += f"\n**Overall Quiz Completion:** {quiz_completion:.1f}%"
    
    conn.close()
    return report

if __name__ == "__main__":
    mcp.run()
