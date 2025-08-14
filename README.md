# Todo App with OpenAI Integration

This project is a simple Todo application built with Django that utilizes OpenAI to generate tasks and set their priority based on fetched context.

## Project Structure

```
todo_openai_project/
├── manage.py
├── README.md
├── requirements.txt
├── todo_openai_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todo/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── openai_utils.py
    ├── tests.py
    ├── views.py
    └── urls.py
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd todo_openai_project
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```
   python manage.py migrate
   ```

5. **Run the development server**:
   ```
   python manage.py runserver
   ```

## Usage

- You can create, view, update, and delete tasks in the Todo app.
- The app integrates with OpenAI to generate tasks based on context and set their priority automatically.

## Requirements

- Python 3.x
- Django
- OpenAI API client

## License

This project is licensed under the MIT License.