# Flask Points Tracker API

This project implements a REST API for managing and tracking points based on different payers. The application supports adding points, spending points in a FIFO order, and fetching the current balances per payer. It is built using **Python** and **Flask**.

---

## Features

- **Add Points**: Add points to a payer's account with a timestamp.
- **Spend Points**: Deduct points based on FIFO (oldest points first), ensuring no payer's balance goes negative.
- **Fetch Balances**: Retrieve the current balance for each payer.

---

## Requirements

- Python 3.8+
- Flask

---

## Setup Instructions

1. **Clone the Repository**:
git clone 
cd 

2. **Install Dependencies**:
pip install -r requirements.txt

3. **Run the Application**:
python run.py

4. **Access the API**:
The API will run on `http://localhost:8000`.

---

## API Endpoints

### 1. **Add Points**
- **Method**: `POST`
- **Route**: `/add`
{
“payer”: “DANNON”,
“points”: 300,
“timestamp”: “2022-10-31T10:00:00Z”
}
- **Response Example**: `200 OK`

---

### 2. **Spend Points**
- **Method**: `POST`
- **Route**: `/spend`
- **Request Body**:
{
“points”: 5000
}
- **Response Example**:
[
{ “payer”: “DANNON”, “points”: -100 },
{ “payer”: “UNILEVER”, “points”: -200 },
{ “payer”: “MILLER COORS”, “points”: -4700 }
]
---

### 3. **Get Balances**
- **Method**: `GET`
- **Route**: `/balance`
- **Response Example**:
{
“DANNON”: 1000,
“UNILEVER”: 0,
“MILLER COORS”: 5300
}
---

## Testing the API

You can test the API using tools like **Postman**, **curl**, or any HTTP client.

**Example Commands**:

1. **Add Points**:
curl -X POST http://localhost:8000/add -H “Content-Type: application/json” -d ‘{“payer”: “DANNON”, “points”: 300, “timestamp”: “2022-10-31T10:00:00Z”}’

2. **Spend Points**:
curl -X POST http://localhost:8000/spend -H “Content-Type: application/json” -d ‘{“points”: 5000}’

3. **Get Balances**:
curl -X GET http://localhost:8000/balance
---

## Project Structure
project/
├── app/
│   ├── init.py            # Initializes Flask app
│   ├── routes.py          # API route definitions
│   ├── services.py        # Core logic for transactions
├── run.py                 # Entry point for the application
├── summary.txt            # Assignment questions