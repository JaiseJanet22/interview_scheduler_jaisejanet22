# **Interview Scheduler API**

This project provides APIs for scheduling interviews. Candidates and interviewers can register their availability, and the system calculates common time slots.

---

## **Features**
- **Register Availability**: Candidates and interviewers can register their availability.
- **Find Common Slots**: The system calculates common time slots based on availability.
- **Docker Support**: The application is containerized using Docker for easier setup and deployment.

---

## **Prerequisites**
- Python 3.9 or higher
- Docker (optional for containerized execution)

---

## **Installation and Running Locally**

### 1. Clone the Repository
```bash
git clone https://github.com/JaiseJanet22/interview_scheduler_jaisejanet22.git
cd interview_scheduler_jaisejanet22
```

### 2. Set Up Virtual Environment and Install Dependencies
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 3. Apply Migrations and Start the Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 4. Access the Application Locally
- Home: `http://127.0.0.1:8000/`
- APIs:
  - `http://127.0.0.1:8000/api/register/` (POST)
  - `http://127.0.0.1:8000/api/slots/` (POST)

---

## **Running with Docker**

### 1. Build the Docker Image
```bash
docker build -t interview_scheduler .
```

### 2. Run the Docker Container
```bash
docker run -p 8000:8000 interview_scheduler
```

### 3. Access the Application
- Home: `http://127.0.0.1:8000/`

---

## **API Endpoints**

### **1. Register Availability**
This API allows candidates and interviewers to register their availability.

- **URL**: `/api/register/`
- **Method**: POST
- **Request Body Example (Candidate)**:
```json
{
    "user": 1,
    "start_time": "10:00:00",
    "end_time": "14:00:00",
    "date": "2025-01-12"
}
```
- **Request Body Example (Interviewer)**:
```json
{
    "user": 2,
    "start_time": "09:00:00",
    "end_time": "12:00:00",
    "date": "2025-01-12"
}
```
- **Expected Response**:
```json
{
    "id": 1,
    "user": 1,
    "start_time": "10:00:00",
    "end_time": "14:00:00",
    "date": "2025-01-12"
}
```

---

### **2. Get Common Slots**
This API calculates common 1-hour time slots between a candidate and an interviewer.

- **URL**: `/api/slots/`
- **Method**: POST
- **Request Body Example**:
```json
{
    "candidate_id": 1,
    "interviewer_id": 2
}
```
- **Expected Response**:
```json
{
    "common_slots": [
        ["10:00:00", "11:00:00"],
        ["11:00:00", "12:00:00"]
    ]
}
```

---

## **Postman Testing**

### **1. Register Availability API**
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/api/register/`
- **Headers**:
  - `Content-Type: application/json`
- **Body Example**:
  ```json
  {
      "user": 1,
      "start_time": "10:00:00",
      "end_time": "14:00:00",
      "date": "2025-01-12"
  }
  ```
- **Expected Response**:
  ```json
  {
      "id": 1,
      "user": 1,
      "start_time": "10:00:00",
      "end_time": "14:00:00",
      "date": "2025-01-12"
  }
  ```

---

### **2. Get Common Slots API**
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/api/slots/`
- **Headers**:
  - `Content-Type: application/json`
- **Body Example**:
  ```json
  {
      "candidate_id": 1,
      "interviewer_id": 2
  }
  ```
- **Expected Response**:
  ```json
  {
      "common_slots": [
          ["10:00:00", "11:00:00"],
          ["11:00:00", "12:00:00"]
      ]
  }
  ```

---

## **Assumptions**
1. All time slots are of 1-hour duration.
2. Availability is registered for one day at a time.

---

## **Suggestions for Improvement**

### **1. Better Scheduling Solution**
- **Integration with Calendar APIs**:
  - Integrate with Google Calendar or Outlook Calendar APIs to dynamically fetch and manage user availability.
- **Custom Slot Durations**:
  - Allow flexible slot durations (e.g., 30 minutes, 2 hours).

---

### **2. Improvements with More Time**
- **User Authentication**:
  - Add authentication for secure access to APIs.
- **Unit Testing**:
  - Implement automated unit tests for reliability.
- **API Documentation**:
  - Use tools like Swagger or Postman Collections to auto-generate API documentation.
- **Frontend**:
  - Build a simple frontend to visualize and manage schedules.

---



