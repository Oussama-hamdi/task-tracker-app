# Task Tracker App

This is a simple task tracking application built with **React.js** for the frontend and **Django** for the backend. The application allows users to create and view tasks. This project demonstrates how to use React components to interact with Django API endpoints.

## Features

- **Add a Task**: Users can create new tasks with a title and description.
- **View Tasks**: Displays a list of tasks fetched from the Django API.
- **Responsive UI**: Simple and easy-to-use interface built with React.

## Tech Stack

- **Frontend**: React.js
- **Backend**: Django (Django REST Framework)
- **API Communication**: Axios for making HTTP requests from the frontend to the backend.
- **In-memory storage**: The tasks are stored in-memory in the backend (no database integration for simplicity).

## Project Structure

### Frontend (React)

- **TaskForm Component**: A form to add new tasks by sending a POST request to the Django backend.
- **TaskList Component**: Displays all tasks by fetching them with a GET request from the backend.
- **TaskItem Component**: A simple component to display individual task details.

### Backend (Django)

- **API Endpoints**:
  - **GET `/api/tasks/`**: Retrieve all tasks.
  - **POST `/api/tasks/add/`**: Add a new task.

## Installation

### Backend Setup (Django)

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required Python packages:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the Django server:
   ```bash
   python3 manage.py runserver
   ```

### Frontend Setup (React)

1. Navigate to the `frontend` folder:

   ```bash
   cd frontend
   ```

2. Install npm dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The React app will now be running at `http://localhost:3000`, and the Django backend will be available at `http://127.0.0.1:8000/api/tasks/`.

## Usage

1. Open the application in your browser: `http://localhost:3000`.
2. Use the task form to add new tasks.
3. View the list of tasks updated in real-time.

## API Endpoints

- **GET /api/tasks/**: Retrieves all the tasks.
- **POST /api/tasks/add/**: Adds a new task. The request body should contain:
  ```json
  {
    "title": "Task title",
    "description": "Task description"
  }
  ```
