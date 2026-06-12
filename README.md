# Travel Deal API

A Flask-based REST API for managing and retrieving travel deals. This application allows you to create, retrieve, and manage travel deals from various platforms with ratings and pricing information.

## Repository

GitHub: [https://github.com/SadikMR/travel-deal](https://github.com/SadikMR/travel-deal)

## Postman Collection

Postman: https://www.postman.com/sadikmr-6504980/workspace/travel-deal/collection/54705650-20ced9a1-6a96-4d25-82c6-65cff1d454d5?action=share&source=copy-link&creator=54705650

## Features

- **Add Travel Deals**: Create new travel deals with destination, price, platform, rating, and travel type
- **Retrieve All Deals**: Fetch all available travel deals
- **Get Deal by ID**: Retrieve specific deal details using its ID
- **Data Validation**: Built-in validation for deal data
- **SQLite Database**: Lightweight persistent storage
- **Error Handling**: Comprehensive error handling and logging
- **Health Check**: API health status endpoint

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SadikMR/travel-deal.git
cd travel-deal
```

### 2. Create a Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Dependencies

The project uses the following Python packages:
- **Flask** (3.1.3) - Web framework
- **Flask-SQLAlchemy** (3.1.1) - SQL toolkit and ORM
- **SQLAlchemy** (2.0.50) - Database abstraction layer
- **pytest** (8.4.1) - Testing framework

See `requirements.txt` for the complete list.

## Configuration

The application uses SQLite database by default. Configuration is managed in `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "sqlite:///travel_deals.db"  # Database location
DEBUG = True                                            # Debug mode
SQLALCHEMY_TRACK_MODIFICATIONS = False                # Disable modification tracking
```

### Environment Variables

Currently, the application uses default configuration. You can modify `config.py` to add custom environment variables if needed.

## Running the Application

### Start the Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Verify the Server is Running

```bash
curl http://localhost:5000
```

Expected response:
```json
{
  "message": "Travel Deal API Running"
}
```

## API Endpoints

### 1. Health Check

**Request:**
```bash
curl http://localhost:5000
```

**Response:**
```json
{
  "message": "Travel Deal API Running"
}
```

---

### 2. Add a New Travel Deal

**Endpoint:** `POST /deals`

**Description:** Create a new travel deal

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "destination": "Paris",
  "price": 899.99,
  "platform": "Booking.com",
  "rating": 4.8,
  "travel_type": "Flight + Hotel"
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:5000/deals \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Paris",
    "price": 899.99,
    "platform": "Booking.com",
    "rating": 4.8,
    "travel_type": "Flight + Hotel"
  }'
```

**Success Response (201 Created):**
```json
{
  "data": {
    "id": 1,
    "destination": "Paris",
    "price": 899.99,
    "platform": "Booking.com",
    "rating": 4.8,
    "travel_type": "Flight + Hotel"
  },
  "message": "Success",
  "status": 201
}
```

**Error Response (400 Bad Request):**
```json
{
  "message": "Missing required fields: destination, price",
  "status": 400
}
```

---

### 3. Get All Travel Deals

**Endpoint:** `GET /deals`

**Description:** Retrieve all travel deals

**cURL Example:**
```bash
curl http://localhost:5000/deals
```

**Success Response (200 OK):**
```json
{
  "data": [
    {
      "id": 1,
      "destination": "Paris",
      "price": 899.99,
      "platform": "Booking.com",
      "rating": 4.8,
      "travel_type": "Flight + Hotel"
    },
    {
      "id": 2,
      "destination": "Tokyo",
      "price": 1299.99,
      "platform": "Expedia",
      "rating": 4.9,
      "travel_type": "Flight + Hotel"
    }
  ],
  "message": "Deals retrieved successfully",
  "status": 200
}
```

---

### 4. Get a Specific Deal by ID

**Endpoint:** `GET /deals/<id>`

**Description:** Retrieve a specific travel deal by its ID

**cURL Example:**
```bash
curl http://localhost:5000/deals/1
```

**Success Response (200 OK):**
```json
{
  "data": {
    "id": 1,
    "destination": "Paris",
    "price": 899.99,
    "platform": "Booking.com",
    "rating": 4.8,
    "travel_type": "Flight + Hotel"
  },
  "message": "Deal retrieved successfully",
  "status": 200
}
```

**Error Response (404 Not Found):**
```json
{
  "message": "Deal not found",
  "status": 404
}
```

## Usage Examples

### Example 1: Create Multiple Travel Deals

```bash
# Deal 1: Paris
curl -X POST http://localhost:5000/deals \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Paris",
    "price": 899.99,
    "platform": "Booking.com",
    "rating": 4.8,
    "travel_type": "Flight + Hotel"
  }'

# Deal 2: Tokyo
curl -X POST http://localhost:5000/deals \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Tokyo",
    "price": 1299.99,
    "platform": "Expedia",
    "rating": 4.9,
    "travel_type": "Flight + Hotel"
  }'

# Deal 3: New York
curl -X POST http://localhost:5000/deals \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "New York",
    "price": 599.50,
    "platform": "Kayak",
    "rating": 4.7,
    "travel_type": "Flight Only"
  }'
```

### Example 2: Retrieve All Deals

```bash
curl http://localhost:5000/deals | python -m json.tool
```

### Example 3: Retrieve a Specific Deal

```bash
# Get deal with ID 2
curl http://localhost:5000/deals/2 | python -m json.tool
```

### Example 4: Test Error Handling

```bash
# Missing required fields
curl -X POST http://localhost:5000/deals \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "London",
    "price": 750.00
  }'

# Response:
# {
#   "message": "Missing required fields: platform, rating, travel_type",
#   "status": 400
# }
```

## Project Structure

```
travel-deal/
├── app.py                    # Application entry point
├── config.py                 # Application configuration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── database/
│   ├── db.py                # Database initialization
│   └── deals_models.py       # SQLAlchemy models
├── routes/
│   └── deals_routes.py       # API route handlers
├── services/
│   └── deals_services.py     # Business logic
├── utils/
│   ├── responses.py          # Response formatting utilities
│   └── validation.py         # Data validation utilities
└── instance/
    └── travel_deals.db       # SQLite database (auto-generated)
```

## Required Fields for Travel Deals

When creating a travel deal, ensure all required fields are provided:

| Field | Type | Example |
|-------|------|---------|
| `destination` | String | "Paris" |
| `price` | Float | 899.99 |
| `platform` | String | "Booking.com" |
| `rating` | Float | 4.8 |
| `travel_type` | String | "Flight + Hotel" |

## Testing

To run tests (if available):

```bash
pytest
```

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'flask'`
**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # On Linux/Mac
pip install -r requirements.txt
```

### Issue: `Address already in use`
**Solution:** The port 5000 is already in use. Kill the process:
```bash
# On Linux/Mac
lsof -ti:5000 | xargs kill -9

# On Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Issue: Database file not found
**Solution:** The database is automatically created on first run. If needed, delete `instance/travel_deals.db` and restart the application.

## API Response Format

All API responses follow a consistent format:

**Success Response:**
```json
{
  "data": { /* actual data */ },
  "message": "Success",
  "status": 200
}
```

**Error Response:**
```json
{
  "message": "Error description",
  "status": 400
}
```
---

**Last Updated:** June 2026
