# Travel Deal API

A Flask-based REST API for managing and retrieving travel deals. This application allows you to create, retrieve, and manage travel deals from various platforms with ratings and pricing information.

## Repository

GitHub: [https://github.com/SadikMR/travel-deal](https://github.com/SadikMR/travel-deal)

## Postman Collection

Postman: https://www.postman.com/sadikmr-6504980/workspace/travel-deal/collection/54705650-20ced9a1-6a96-4d25-82c6-65cff1d454d5?action=share&source=copy-link&creator=54705650

## Features

## Features

* **Add Travel Deals**: Create new travel deals with destination, price, platform, rating, and travel type
* **Retrieve All Deals**: Fetch all available travel deals
* **Get Deal by ID**: Retrieve specific deal details using its ID
* **Search Deals**: Search deals by destination, platform, or travel type
* **Filter Deals**: Filter deals by price range
* **Sort Deals**: Sort deals by supported fields in ascending or descending order
* **Recently Viewed Deals**: Track and retrieve recently viewed travel deals
* **Data Validation**: Built-in validation for requests and query parameters
* **Logging**: Request, validation, success, and error logging
* **SQLite Database**: Lightweight persistent storage
* **Error Handling**: Comprehensive error handling and logging
* **Health Check**: API health status endpoint


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

## API Endpoints

### 1. Health Check

**Endpoint:** `GET /`

**Description:** Verify that the API is running.

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

**Description:** Create a new travel deal.

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
  "success": true
}
```

---

### 3. Get All Travel Deals

**Endpoint:** `GET /deals`

**Description:** Retrieve all travel deals.

**Request:**

```bash
curl http://localhost:5000/deals
```

---

### 4. Get a Specific Deal by ID

**Endpoint:** `GET /deals/<id>`

**Description:** Retrieve a specific travel deal by its ID.

**Request:**

```bash
curl http://localhost:5000/deals/1
```

**Note:** Accessing a deal by ID automatically records it as a recently viewed deal.

---

### 5. Search Travel Deals

**Endpoint:** `GET /deals/search`

**Description:** Search travel deals by destination, platform, or travel type.

**Query Parameters:**

| Parameter   | Description           |
| ----------- | --------------------- |
| destination | Search by destination |
| platform    | Search by platform    |
| travel_type | Search by travel type |

**Examples:**

```bash
curl "http://localhost:5000/deals/search?destination=dubai"
```

```bash
curl "http://localhost:5000/deals/search?platform=booking"
```

```bash
curl "http://localhost:5000/deals/search?travel_type=luxury"
```

**Features:**

* Case-insensitive search
* Partial matching support

---

### 6. Filter Travel Deals

**Endpoint:** `GET /deals/filter`

**Description:** Filter travel deals within a price range.

**Query Parameters:**

| Parameter | Description   |
| --------- | ------------- |
| min_price | Minimum price |
| max_price | Maximum price |

**Example:**

```bash
curl "http://localhost:5000/deals/filter?min_price=1000&max_price=5000"
```

**Validation Rules:**

* `min_price` cannot be negative
* `max_price` cannot be smaller than `min_price`

---

### 7. Sort Travel Deals

**Endpoint:** `GET /deals/sort`

**Description:** Sort travel deals.

**Query Parameters:**

| Parameter | Description      |
| --------- | ---------------- |
| sort_by   | Field to sort by |
| order     | asc or desc      |

**Example:**

```bash
curl "http://localhost:5000/deals/sort?sort_by=price&order=asc"
```

```bash
curl "http://localhost:5000/deals/sort?sort_by=price&order=desc"
```

**Validation Rules:**

* Invalid sorting fields return HTTP 400
* Invalid sort order returns HTTP 400

---

### 8. Get Recently Viewed Deals

**Endpoint:** `GET /deals/recent`

**Description:** Retrieve the most recently viewed travel deals.

**Request:**

```bash
curl http://localhost:5000/deals/recent
```

**Response Example:**

```json
{
  "data": [
    {
      "id": 6,
      "destination": "Dubai",
      "price": 5000.0,
      "platform": "Booking",
      "rating": 4.5,
      "travel_type": "Luxury"
    }
  ],
  "message": "Recent viewed deals retrieved successfully",
  "success": true
}
```

Returns the most recently viewed deals ordered by latest view time.

---

## Usage Examples

### Create a Travel Deal

```bash
curl -X POST http://localhost:5000/deals \
-H "Content-Type: application/json" \
-d '{
  "destination":"Paris",
  "price":899.99,
  "platform":"Booking.com",
  "rating":4.8,
  "travel_type":"Flight + Hotel"
}'
```

### Search Deals

```bash
curl "http://localhost:5000/deals/search?destination=dubai"
```

### Filter Deals

```bash
curl "http://localhost:5000/deals/filter?min_price=1000&max_price=5000"
```

### Sort Deals

```bash
curl "http://localhost:5000/deals/sort?sort_by=price&order=desc"
```

### View a Deal

```bash
curl http://localhost:5000/deals/1
```

### View Recently Viewed Deals

```bash
curl http://localhost:5000/deals/recent
```


## Project Structure

```text
travel-deal/
├── app.py                         # Application entry point
├── config.py                      # Application configuration
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── .gitignore
├── database/
│   ├── db.py                      # Database initialization
│   ├── deals_models.py            # TravelDeal model
│   └── recent_deals_models.py     # RecentViewedDeal model
├── routes/
│   └── deals_routes.py            # API route handlers
├── services/
│   └── deals_services.py          # Business logic layer
├── utils/
│   ├── responses.py               # Standardized API responses
│   └── validation.py              # Request validation utilities
├── logs/
│   └── app.log                    # Application logs (auto-generated)
└── instance/
    └── travel_deals.db            # SQLite database (auto-generated)
```


## Logging

The application uses Python's built-in `logging` module to track application activities and errors.

### Logged Events

* Search requests
* Invalid requests and validation failures
* Successful operations
* Failed API requests and exceptions

### Log Levels

* `logging.info()` – Successful operations and request tracking
* `logging.warning()` – Invalid requests and validation issues
* `logging.error()` – Unexpected errors and failures

### Log File

Application logs are written to:

```text
logs/app.log
```

Example:

```text
2026-06-15 17:45:10,123 - INFO - Search request received
2026-06-15 17:45:11,456 - WARNING - Empty search request
2026-06-15 17:45:12,789 - ERROR - Error searching deals
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

