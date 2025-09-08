class ContentAwareCourseCodeGenerator:
    def __init__(self):
        import json
        self.json = json
        self.course_data = {
            'metadata': {},
            'chapters': [],
            'quizzes': [],
            'exams': [],
            'resources': [],
            'student_data': {}
        }
        self.current_item = {}
        self.context_stack = []
        
    def extract_course_content(self, ast_traversal):
        """Extract all course content from AST traversal"""
        # Parse the linear AST traversal into structured data
        
        # Extract metadata
        for i, token in enumerate(ast_traversal):
            if token == 'metadata_name' and i > 0:
                self.course_data['metadata']['name'] = ast_traversal[i-1].strip('"')
            elif token == 'metadata_author' and i > 0:
                self.course_data['metadata']['author'] = ast_traversal[i-1].strip('"')
            elif token == 'metadata_description' and i > 0:
                self.course_data['metadata']['description'] = ast_traversal[i-1].strip('"')
            elif token == 'metadata_level' and i > 0:
                self.course_data['metadata']['level'] = ast_traversal[i-1].strip('"')
        
        # Extract structured content by tracking sections
        current_section = None
        current_item = {}
        i = 0
        
        while i < len(ast_traversal):
            token = ast_traversal[i]
            
            # Detect section types
            if token == 'flow_type' and i > 0:
                section_type = ast_traversal[i-1].strip('"')
                if section_type in ['chapter', 'quiz', 'exam', 'resource']:
                    if current_section and current_item:
                        self.finalize_section(current_section, current_item)
                    current_section = section_type
                    current_item = {'type': section_type}
            # Fallback: some listeners may emit just 'type'
            elif token == 'type' and i > 0:
                section_type = ast_traversal[i-1].strip('"')
                if section_type in ['chapter', 'quiz', 'exam', 'resource']:
                    if current_section and current_item:
                        self.finalize_section(current_section, current_item)
                    current_section = section_type
                    current_item = {'type': section_type}
            
            # Extract content based on current section
            elif current_section:
                if token == 'content_title' and i > 0:
                    current_item['title'] = ast_traversal[i-1].strip('"')
                elif token == 'instructions' and i > 0:
                    current_item['instructions'] = ast_traversal[i-1].strip('"')
                elif token == 'metadata_description' and i > 0:
                    current_item['description'] = ast_traversal[i-1].strip('"')
                elif token == 'setting_passing_score' and i > 0:
                    if 'settings' not in current_item:
                        current_item['settings'] = {}
                    current_item['settings']['passing_score'] = int(ast_traversal[i-1])
                elif token == 'setting_time_limit' and i > 0:
                    if 'settings' not in current_item:
                        current_item['settings'] = {}
                    current_item['settings']['time_limit'] = ast_traversal[i-1].strip('"')
                elif token == 'question_question' and i > 0:
                    if 'questions' not in current_item:
                        current_item['questions'] = []
                    # Extract complete question
                    question = self.extract_question_from_position(ast_traversal, i)
                    if question:
                        current_item['questions'].append(question)
                elif token == 'content_body' and i > 0:
                    if 'content' not in current_item:
                        current_item['content'] = []
                    current_item['content'].append({
                        'type': 'text',
                        'title': current_item.get('current_title', 'Content'),
                        'body': ast_traversal[i-1].strip('"')
                    })
                elif token == 'content_code' and i > 0:
                    if 'content' not in current_item:
                        current_item['content'] = []
                    current_item['content'].append({
                        'type': 'example',
                        'title': current_item.get('current_title', 'Example'),
                        'code': ast_traversal[i-1].strip('"').replace('\\\\n', '\\n'),
                        'language': 'python'
                    })
                elif token == 'content_url' and i > 0:
                    if 'content' not in current_item:
                        current_item['content'] = []
                    current_item['content'].append({
                        'type': 'video',
                        'title': current_item.get('current_title', 'Video'),
                        'url': ast_traversal[i-1].strip('"')
                    })
                elif token == 'material_path' and i > 0:
                    if 'materials' not in current_item:
                        current_item['materials'] = []
                    current_item['materials'].append({
                        'type': 'file',
                        'title': current_item.get('current_title', 'File'),
                        'path': ast_traversal[i-1].strip('"')
                    })
                elif token == 'summary' and i > 0:
                    current_item['summary'] = ast_traversal[i-1].strip('"')
                    
                # Track current title for content items
                if token == 'content_title' and i > 0:
                    current_item['current_title'] = ast_traversal[i-1].strip('"')
            
            i += 1
        
        # Finalize last section
        if current_section and current_item:
            self.finalize_section(current_section, current_item)
        
        return self.course_data
    
    def extract_question_from_position(self, ast_traversal, start_pos):
        """Extract a complete question starting from question_question position"""
        question = {'question': ast_traversal[start_pos-1].strip('"')}
        
        # Look ahead for question components
        i = start_pos + 1
        while i < len(ast_traversal) and not (ast_traversal[i] == 'question_question'):
            token = ast_traversal[i]
            
            if token == 'question_answer' and i > 0:
                answer_val = ast_traversal[i-1].strip('"')
                if answer_val == 'true':
                    question['answer'] = True
                elif answer_val == 'false':
                    question['answer'] = False
                else:
                    question['answer'] = answer_val
            elif token == 'question_hint' and i > 0:
                question['hint'] = ast_traversal[i-1].strip('"')
            elif token == 'content_explanation' and i > 0:
                question['explanation'] = ast_traversal[i-1].strip('"')
            elif token == 'question_options' and i > 1:
                # Extract options array - look backwards for the array
                options = []
                j = i - 1
                while j >= 0 and ast_traversal[j] != 'begin_scope_operator':
                    if ast_traversal[j] != 'array' and ast_traversal[j] != 'end_scope_operator':
                        if ast_traversal[j].startswith('"') and ast_traversal[j].endswith('"'):
                            options.insert(0, ast_traversal[j].strip('"'))
                    j -= 1
                if options:
                    question['options'] = options
            elif token in ['flow_type', 'end_scope_operator']:
                # End of question
                break
                
            i += 1
        
        return question if len(question) > 1 else None
    
    def finalize_section(self, section_type, item_data):
        """Add completed section to course data - only if it has meaningful content"""
        if section_type == 'chapter':
            # Only add chapters that have a title or content
            if item_data.get('title') or item_data.get('content') or item_data.get('description'):
                self.course_data['chapters'].append(item_data)
        elif section_type == 'quiz':
            if item_data.get('title') or item_data.get('questions'):
                self.course_data['quizzes'].append(item_data)
        elif section_type == 'exam':
            if item_data.get('title') or item_data.get('questions'):
                self.course_data['exams'].append(item_data)
        elif section_type == 'resource':
            if item_data.get('title') or item_data.get('materials'):
                self.course_data['resources'].append(item_data)
    
    def extract_chapter_content(self, ast_traversal, start_idx):
        """Extract chapter content including title, description, content items"""
        chapter = {'type': 'chapter', 'content': [], 'objectives': []}
        i = start_idx
        
        while i < len(ast_traversal):
            token = ast_traversal[i]
            
            if token == 'content_title' and i > 0:
                chapter['title'] = ast_traversal[i-1].strip('"')
            elif token == 'metadata_description' and i > 0:
                chapter['description'] = ast_traversal[i-1].strip('"')
            elif token == 'content_body' and i > 0:
                chapter['content'].append({
                    'type': 'text',
                    'title': chapter.get('current_content_title', 'Content'),
                    'body': ast_traversal[i-1].strip('"')
                })
            elif token == 'content_code' and i > 0:
                chapter['content'].append({
                    'type': 'example',
                    'title': chapter.get('current_content_title', 'Example'),
                    'code': ast_traversal[i-1].strip('"').replace('\\\\n', '\\n'),
                    'language': 'python'
                })
            elif token == 'content_url' and i > 0:
                chapter['content'].append({
                    'type': 'video',
                    'title': chapter.get('current_content_title', 'Video'),
                    'url': ast_traversal[i-1].strip('"')
                })
            elif token == 'summary' and i > 0:
                chapter['summary'] = ast_traversal[i-1].strip('"')
                break
                
            # Track current content title
            if token == 'content_title' and i > 0:
                chapter['current_content_title'] = ast_traversal[i-1].strip('"')
                
            i += 1
            
        return chapter
    
    def extract_quiz_content(self, ast_traversal, start_idx):
        """Extract quiz content including questions and settings"""
        quiz = {'type': 'quiz', 'questions': [], 'settings': {}}
        i = start_idx
        current_question = {}
        
        while i < len(ast_traversal):
            token = ast_traversal[i]
            
            if token == 'content_title' and i > 0:
                quiz['title'] = ast_traversal[i-1].strip('"')
            elif token == 'instructions' and i > 0:
                quiz['instructions'] = ast_traversal[i-1].strip('"')
            elif token == 'setting_passing_score' and i > 0:
                quiz['settings']['passing_score'] = int(ast_traversal[i-1])
            elif token == 'setting_time_limit' and i > 0:
                quiz['settings']['time_limit'] = ast_traversal[i-1].strip('"')
            elif token == 'question_question' and i > 0:
                if current_question:
                    quiz['questions'].append(current_question.copy())
                current_question = {'question': ast_traversal[i-1].strip('"')}
            elif token == 'question_answer' and i > 0:
                if current_question:
                    answer_value = ast_traversal[i-1].strip('"')
                    # Convert JSON boolean strings to Python booleans
                    if answer_value == 'true':
                        current_question['answer'] = True
                    elif answer_value == 'false':
                        current_question['answer'] = False
                    else:
                        current_question['answer'] = answer_value
            elif token == 'question_hint' and i > 0:
                if current_question:
                    current_question['hint'] = ast_traversal[i-1].strip('"')
            elif token == 'content_explanation' and i > 0:
                if current_question:
                    current_question['explanation'] = ast_traversal[i-1].strip('"')
            elif 'flow_type' in token and i > 0 and ast_traversal[i-1].strip('"') != 'quiz':
                # End of quiz section
                if current_question:
                    quiz['questions'].append(current_question)
                break
                
            i += 1
            
        if current_question and current_question not in quiz['questions']:
            quiz['questions'].append(current_question)
            
        return quiz
    
    def extract_exam_content(self, ast_traversal, start_idx):
        """Extract exam content similar to quiz but with exam specifics"""
        return self.extract_quiz_content(ast_traversal, start_idx)  # Same structure for now
    
    def extract_resource_content(self, ast_traversal, start_idx):
        """Extract resource content"""
        resource = {'type': 'resource', 'materials': []}
        i = start_idx
        
        while i < len(ast_traversal):
            token = ast_traversal[i]
            
            if token == 'content_title' and i > 0:
                resource['title'] = ast_traversal[i-1].strip('"')
            elif token == 'metadata_description' and i > 0:
                resource['description'] = ast_traversal[i-1].strip('"')
            elif token == 'material_path' and i > 0:
                resource['materials'].append({
                    'type': 'file',
                    'title': resource.get('current_material_title', 'Resource'),
                    'path': ast_traversal[i-1].strip('"')
                })
            elif token == 'content_url' and i > 0:
                resource['materials'].append({
                    'type': 'link',
                    'title': resource.get('current_material_title', 'Link'),
                    'url': ast_traversal[i-1].strip('"')
                })
            elif 'flow_type' in token and i > 0 and ast_traversal[i-1].strip('"') != 'resource':
                break
                
            # Track current material title
            if token == 'content_title' and i > 0:
                resource['current_material_title'] = ast_traversal[i-1].strip('"')
                
            i += 1
            
        return resource
    
    def generate_content_aware_code(self, course_data):
        """Generate Python code with embedded course content"""
        
        course_name = course_data['metadata'].get('name', 'Course')
        author = course_data['metadata'].get('author', 'Instructor')
        
        # Generate runtime loader that reads main.json and referenced flow files
        code = f'''from mcp.server.fastmcp import FastMCP
import json
import sqlite3
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

mcp = FastMCP("{course_name}")

# Database setup
DB_PATH = "course_data.db"

# Default path to main course file (override with env var COURSE_MAIN_JSON)
MAIN_JSON_PATH = os.environ.get("COURSE_MAIN_JSON", os.path.join("input", "main.json"))

def _safe_read_json(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def _normalize_path(base_dir: str, ref_path: str) -> str:
    # Resolve refs like "chapters/chapter1.json" relative to base_dir
    norm = os.path.normpath(os.path.join(base_dir, ref_path))
    return norm

def load_course_from_files(main_json_path: str) -> Dict[str, Any]:
    """Load course metadata and flow items from main.json and referenced files."""
    course: Dict[str, Any] = {{
        'metadata': {{}},
        'chapters': [],
        'quizzes': [],
        'exams': [],
        'resources': []
    }}

    main_abs = os.path.abspath(main_json_path)
    base_dir = os.path.dirname(main_abs)

    main_data = _safe_read_json(main_abs)
    if not main_data:
        return course

    # Metadata
    meta = main_data.get('course_introduction') or {{}}
    course['metadata'] = {{
        'name': meta.get('name', "{course_name}"),
        'author': meta.get('author', "{author}"),
        'description': meta.get('description', ''),
        'level': meta.get('level', ''),
        'tags': meta.get('tags', [])
    }}

    # Flow items
    for item in main_data.get('flow', []):
        item_type = (item or {{}}).get('type')
        ref = (item or {{}}).get('ref')
        if not item_type:
            continue
        if ref:
            ref_path = _normalize_path(base_dir, ref)
            ref_data = _safe_read_json(ref_path)
        else:
            ref_data = None

        if item_type == 'chapter' and ref_data:
            course['chapters'].append(ref_data)
        elif item_type == 'quiz' and ref_data:
            course['quizzes'].append(ref_data)
        elif item_type == 'exam' and ref_data:
            course['exams'].append(ref_data)
        elif item_type == 'resource' and ref_data:
            course['resources'].append(ref_data)
        # registration or unreferenced items are ignored for content purposes

    return course

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
    
    # Load and populate course content from files
    course = load_course_from_files(MAIN_JSON_PATH)
    populate_course_content(cursor, conn, course)
    
    conn.close()


def populate_course_content(cursor, conn, course: Dict[str, Any]):
    """Populate database with course content from loaded course dict"""
    
    # Insert chapters
    for i, chapter in enumerate(course.get('chapters', []), 1):
        cursor.execute("""
            INSERT OR REPLACE INTO chapters 
            (chapter_number, title, description, content, summary, objectives)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            i,
            chapter.get('title', f'Chapter {{i}}'),
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
            quiz.get('title', f'Quiz {{i}}'),
            quiz.get('instructions', ''),
            (quiz.get('settings', {{}}) or {{}}).get('passing_score', 70),
            (quiz.get('settings', {{}}) or {{}}).get('time_limit', ''),
            (quiz.get('settings', {{}}) or {{}}).get('attempts_allowed', 1),
            (quiz.get('settings', {{}}) or {{}}).get('randomize_questions', False)
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
            (exam.get('settings', {{}}) or {{}}).get('passing_score', 70),
            (exam.get('settings', {{}}) or {{}}).get('attempts_allowed', 1),
            (exam.get('settings', {{}}) or {{}}).get('weight', 1.0)
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
    """Register a student for {course_name}"""
    # Ensure database is initialized
    init_database()
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    existing = cursor.fetchone()
    
    if existing:
        conn.close()
        return f"Welcome back, {{name}}! You're already registered for {course_name}."
    else:
        cursor.execute("""
            INSERT INTO students (student_id, name, last_activity)
            VALUES (?, ?, ?)
        """, (student_id, name, datetime.now().isoformat()))
        conn.commit()
        conn.close()
        return f"Welcome to {course_name}, {{name}}! Registration successful."

@mcp.tool()
def get_course_info() -> str:
    """Get comprehensive course information"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get course metadata (loaded from main.json when initializing)
    md = load_course_from_files(MAIN_JSON_PATH).get('metadata', {{}})
    course_name_local = md.get('name', "{course_name}")
    author_local = md.get('author', "{author}")
    description = md.get('description', '') or "A comprehensive course"
    level = md.get('level', '') or "beginner"
    
    info = f"Course: {{course_name_local}}"
    info += f"Instructor: {{author_local}}"
    info += f"Description: {{description}}"
    info += f"Level: {{level}}"
    
    # Get chapters from database
    cursor.execute("SELECT chapter_number, title FROM chapters ORDER BY chapter_number")
    chapters = cursor.fetchall()
    
    info += "Course Structure:"
    for chapter_num, title in chapters:
        info += f"{{chapter_num}}. {{title}}"
    
    # Get quiz count
    cursor.execute("SELECT COUNT(*) FROM quizzes")
    quiz_count = cursor.fetchone()[0]
    if quiz_count > 0:
        info += f"Quizzes Available: {{quiz_count}}"
        
    # Get exam count  
    cursor.execute("SELECT COUNT(*) FROM exams")
    exam_count = cursor.fetchone()[0]
    if exam_count > 0:
        info += f"Exams Available: {{exam_count}}"
        
    # Get resource count
    cursor.execute("SELECT COUNT(*) FROM resources")
    resource_count = cursor.fetchone()[0]
    if resource_count > 0:
        info += f"Resources Available: {{resource_count}}"
    
    conn.close()
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
    if not chapter_data:
        cursor.execute("SELECT COUNT(*) FROM chapters")
        total_chapters = cursor.fetchone()[0]
        conn.close()
        return f"Chapter {{chapter_number}} does not exist. Available chapters: 1-{{total_chapters}}"
    
    title, description, content_json, summary, objectives_json = chapter_data
    conn.close()
    
    content = f"# {{title}}"
    content += f"**Description:** {{description or 'No description'}}"
    
    # Parse objectives
    try:
        objectives = json.loads(objectives_json) if objectives_json else []
        if objectives:
            content += "**Learning Objectives:**"
            for obj in objectives:
                content += f"- {{obj}}"
            content += ""
    except json.JSONDecodeError:
        pass
    
    # Parse content items
    try:
        content_items = json.loads(content_json) if content_json else []
        if content_items:
            content += "**Content:**"
            for item in content_items:
                if item['type'] == 'text':
                    content += f"### {{item.get('title', 'Section')}}"
                    content += f"{{item.get('body', '')}}"
                elif item['type'] == 'example':
                    content += f"### {{item.get('title', 'Code Example')}}"
                    content += f"```{{item.get('language', 'python')}}"
                    content += f"{{item.get('code', '').replace('\', chr(10))}}"
                    content += f"```"
                    if 'explanation' in item:
                        content += f"*{{item['explanation']}}*"
                elif item['type'] == 'video':
                    content += f"### {{item.get('title', 'Video')}}"
                    content += f"Video URL: {{item.get('url', '')}}"
    except json.JSONDecodeError:
        content += "Content format error."
    
    if summary:
        content += f"**Summary:**{{summary}}"
    
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
        LEFT JOIN questions qs ON q.id = qs.quiz_id
        GROUP BY q.quiz_number, q.title, q.time_limit, q.passing_score
        ORDER BY q.quiz_number
    """)
    quizzes = cursor.fetchall()
    
    if not quizzes:
        conn.close()
        return "No quizzes available in this course."
    
    quiz_list = "Available Quizzes:"
    for quiz_num, title, time_limit, passing_score, question_count in quizzes:
        quiz_list += f"{{quiz_num}}. {{title}}"
        quiz_list += f"   Questions: {{question_count}}"
        if time_limit:
            quiz_list += f"   Time Limit: {{time_limit}}"
        if passing_score:
            quiz_list += f"   Passing Score: {{passing_score}}%"
        quiz_list += ""
    
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
        return f"Quiz {{quiz_number}} does not exist. Available quizzes: 1-{{total_quizzes}}"
    
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
        return f"Quiz {{quiz_number}} has no questions available."
    
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
        response = f"**{{title}}**"
        response += f"{{instructions}}" if instructions else "Test your understanding. Each question is worth equal points."
        response += f"**Question {{current_question + 1}} of {{len(questions)}}:**"
        response += f"{{question_text}}"
        
        if hint:
            response += f"*Hint: {{hint}}*"
            
        response += "Use submit_quiz_answer() to submit your answer."
        
        return response
    else:
        return f"Quiz {{quiz_number}} has no questions or is already completed."

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
        SELECT q.id, qu.passing_score FROM quiz_sessions qs
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
    if isinstance(correct_answer, str) and correct_answer.lower() in ['true', 'false']:
        # For boolean answers, convert user input to boolean
        user_answer_bool = answer.lower().strip() in ['true', 'yes', '1', 'correct']
        correct_answer_bool = correct_answer.lower() == 'true'
        is_correct = user_answer_bool == correct_answer_bool
    else:
        # For string answers, do case-insensitive comparison
        is_correct = str(answer).lower().strip() == str(correct_answer).lower().strip()
    
    # Store the answer
    cursor.execute("""
        INSERT INTO quiz_answers (session_id, question_number, student_answer, correct_answer, is_correct)
        VALUES (?, ?, ?, ?, ?)
    """, (session_id, current_q, answer, correct_answer, is_correct))
    
    response = f"Answer submitted: {{answer}}"
    
    if is_correct:
        response += "✓ Correct!"
    else:
        response += f"✗ Incorrect. The correct answer was: {{correct_answer}}"
    
    # Show explanation if available
    if explanation:
        response += f"Explanation: {{explanation}}"
    
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
            response += f"**Question {{next_question + 1}} of {{total_questions}}:**"
            response += f"{{question_text}}"
            if hint:
                response += f"*Hint: {{hint}}*"
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
        
        response += f"**Quiz Completed!**"
        response += f"Score: {{correct}}/{{total}} ({{score:.1f}}%)"
        
        if passed:
            response += "🎉 You passed!"
        else:
            response += f"You need {{passing_score}}% to pass. Try again!"
    
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
        return f"No results found for Quiz {{quiz_number}}. Have you completed it?"
    
    score, max_score, percentage, passed, completed_at, quiz_title, passing_score = result
    
    result_text = f"**{{quiz_title}} Results**"
    result_text += f"Score: {{percentage:.1f}}%"
    result_text += f"Status: {{'PASSED' if passed else 'FAILED'}}"
    result_text += f"Passing Score: {{passing_score}}%"
    
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
    
    # Get course metadata from files
    md = load_course_from_files(MAIN_JSON_PATH).get('metadata', {{}})
    course_name_local = md.get('name', "{course_name}")
    
    # Get course structure counts
    cursor.execute("SELECT COUNT(*) FROM chapters")
    total_chapters = cursor.fetchone()[0]
    
    report = f"**Progress Report for {{name}}**"
    report += f"**Course:** {{course_name_local}}"
    report += f"**Enrolled:** {{created_at}}"
    report += f"**Last Activity:** {{last_activity}}"
    
    # Chapter progress
    cursor.execute("SELECT COUNT(*) FROM chapter_progress WHERE student_id = ? AND completed = 1", (student_id,))
    completed_chapters = cursor.fetchone()[0]
    
    report += f"**Chapter Progress:**"
    report += f"Current Chapter: {{current_chapter}}"
    report += f"Completed Chapters: {{completed_chapters}}/{{total_chapters}}"
    
    # Quiz scores
    cursor.execute("""
        SELECT quiz_number, percentage, passed 
        FROM quiz_scores 
        WHERE student_id = ? 
        ORDER BY quiz_number
    """, (student_id,))
    
    quiz_results = cursor.fetchall()
    
    if quiz_results:
        report += f"**Quiz Scores:**"
        for quiz_num, percentage, passed in quiz_results:
            status = "✅" if passed else "❌"
            report += f"Quiz {{quiz_num}}: {{percentage:.1f}}% {{status}}"
    else:
        report += f"**Quiz Scores:** No quizzes completed"
    
    # Overall progress
    cursor.execute("SELECT COUNT(*) FROM quizzes")
    total_quizzes = cursor.fetchone()[0]
    completed_quizzes = len(quiz_results)
    
    if total_quizzes > 0:
        quiz_completion = (completed_quizzes / total_quizzes) * 100
        report += f"**Overall Quiz Completion:** {{quiz_completion:.1f}}%"
    
    conn.close()
    return report

if __name__ == "__main__":
    mcp.run()
'''
        
        return code
    
    def generate_from_ast(self, ast_traversal):
        """Main method to generate content-aware code from AST"""
        course_data = self.extract_course_content(ast_traversal)
        return self.generate_content_aware_code(course_data)
