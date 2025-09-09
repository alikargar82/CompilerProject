# Course DSL Compiler

This is a simple compiler that takes course information written in JSON files and turns it into a working MCP server for education.

## What it does

You write course content in JSON files (chapters, quizzes, exams), and this program automatically creates a Python server that can handle students, track progress, and deliver the course content.

## How it works

1. **Input**: JSON files describing your course
2. **Processing**: The compiler reads these files and understands the course structure
3. **Output**: A complete Python MCP server that runs your course

## Main Parts

- `Course.g4` - Defines what valid course JSON looks like
- `main.py` - The main program you run
- `CustomCourseListener.py` - Reads and understands the JSON structure
- `code_generator.py` - Creates the final Python server code

## How to use it

Run this command:
```bash
python main.py -i input/main.json
```

This reads your course from `input/main.json` and creates `generated_code.py`.

## Course file format

Your main course file looks like this:

```json
{
  "course_introduction": {
    "name": "My Course",
    "author": "Your Name", 
    "description": "What the course is about",
    "level": "beginner"
  },
  "flow": [
    {
      "type": "chapter",
      "ref": "chapters/chapter1.json"
    },
    {
      "type": "quiz",
      "ref": "quizzes/quiz1.json"
    }
  ]
}
```

## What you can put in courses

- **Chapters**: Text content, videos, code examples
- **Quizzes**: Multiple choice questions with answers
- **Exams**: Longer tests with different question types
- **Resources**: Files and links for students

## What you get

After running the compiler, you get a Python file that:
- Stores student data in a database
- Delivers course content to students
- Handles quiz submissions and grading
- Tracks student progress
- Manages course resources

## Example files

Check the `input/` folder to see example courses with:
- Chapter content with videos and text
- Quiz questions with multiple choice answers
- Exam questions with coding problems
- Resource files and links

## Requirements

- Python 3.7 or newer
- ANTLR4 for Python
