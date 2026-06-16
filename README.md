# Travel Deal API

A Flask-based REST API for managing and retrieving travel deals. This application allows you to create, retrieve, and manage travel deals from various platforms with ratings and pricing information.

## Repository

GitHub: [https://github.com/SadikMR/travel-deal](https://github.com/SadikMR/travel-deal)

## Postman Collection

Postman: https://www.postman.com/sadikmr-6504980/workspace/travel-deal/collection/54705650-12047859-dbd4-4e8b-970d-ec8cc2348b59?action=share&source=collection_link&creator=54705650

### Using the Postman Collection

1. **Import the Collection**
   - Open Postman and click "Import"
   - Copy and paste the collection link or download the `Travel-Deals.postman_collection.json` file
   - The collection will be imported with all pre-configured endpoints

2. **Set Base URL Variable**
   - The collection uses a `{{base_url}}` variable (default: `http://localhost:5000`)
   - Go to Collections → Travel-Deals → Variables
   - Update the `base_url` value if your API runs on a different host/port

3. **Replace Path Parameters**
   - Endpoints with `:id` (e.g., `GET /deals/:id`, `PUT /deals/:id`, `DELETE /deals/:id`)
   - Replace `:id` with an actual deal ID (e.g., `1`, `2`, etc.)
   - In Postman, these are typically configured as path variables

4. **Make API Requests**
   - All 12 endpoints are organized in the collection
   - Click on any endpoint to view its details
   - Modify request bodies and query parameters as needed
   - Click "Send" to execute the request

5. **Available Endpoints**
   - Health Check
   - CRUD Operations (Create, Read, Update, Delete)
   - Search, Filter, and Sort
   - Recently Viewed Deals
   - Most Popular Deals
   - Statistics

## Features

* **Add Travel Deals**: Create new travel deals with destination, price, platform, rating, and travel type
* **Retrieve All Deals**: Fetch all available travel deals
* **Get Deal by ID**: Retrieve specific deal details using its ID
* **Update Deals**: Update existing travel deal information
* **Delete Deals**: Remove travel deals from the system
* **Search Deals**: Search deals by destination, platform, or travel type
* **Filter Deals**: Filter deals by price range
* **Sort Deals**: Sort deals by supported fields in ascending or descending order
* **Recently Viewed Deals**: Track and retrieve recently viewed travel deals
* **Most Popular Deals**: Retrieve the top popular deals based on view counts or popularity metrics
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
  "travel_type": "Luxury"
}
```

**Allowed Travel Types:** Budget, Luxury, Family, Adventure

**Success Response (201 Created):**

```json
{
  "data": {
    "id": 1,
    "destination": "Paris",
    "price": 899.99,
    "platform": "Booking.com",
    "rating": 4.8,
    "travel_type": "Luxury"
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

**Path Parameter:**
- `<id>`: The ID of the deal to retrieve (replace with an actual deal ID, e.g., 1)

**Request:**

```bash
curl http://localhost:5000/deals/1
```

**Note:** Accessing a deal by ID automatically records it as a recently viewed deal.

---

### 5. Update a Travel Deal

**Endpoint:** `PUT /deals/<id>`

**Description:** Update an existing travel deal by its ID.

**Path Parameter:**
- `<id>`: The ID of the deal to update (replace with an actual deal ID, e.g., 1)

**Request Body:**

```json
{
  "destination": "Paris",
  "price": 879.99,
  "platform": "Booking.com",
  "rating": 4.9,
  "travel_type": "Luxury"
}
```

**Allowed Travel Types:** Budget, Luxury, Family, Adventure

**Success Response (200 OK):**

```json
{
  "data": {
    "id": 1,
    "destination": "Paris",
    "price": 879.99,
    "platform": "Booking.com",
    "rating": 4.9,
    "travel_type": "Luxury"
  },
  "message": "Updated deal successfully",
  "success": true
}
```

**Request:**

```bash
curl -X PUT http://localhost:5000/deals/1 \
-H "Content-Type: application/json" \
-d '{
  "destination": "Paris",
  "price": 879.99,
  "platform": "Booking.com",
  "rating": 4.9,
  "travel_type": "Luxury"
}'
```

---

### 6. Delete a Travel Deal

**Endpoint:** `DELETE /deals/<id>`

**Description:** Delete a travel deal by its ID.

**Path Parameter:**
- `<id>`: The ID of the deal to delete (replace with an actual deal ID, e.g., 1)

**Request:**

```bash
curl -X DELETE http://localhost:5000/deals/1
```

**Success Response (200 OK):**

```json
{
  "data": {
    "id": 1,
    "destination": "Paris",
    "price": 879.99,
    "platform": "Booking.com",
    "rating": 4.9,
    "travel_type": "Flight + Hotel"
  },
  "message": "Deleted deal successfully",
  "success": true
}
```

---

### 7. Search Travel Deals

**Endpoint:** `GET /deals/search`

**Description:** Search travel deals by destination, platform, or travel type.

**Query Parameters:** (At least one required)

| Parameter   | Type   | Required | Description           |
| ----------- | ------ | -------- | --------------------- |
| destination | String | Optional | Search by destination |
| platform    | String | Optional | Search by platform    |
| travel_type | String | Optional | Search by travel type |

**Note:** At least one of the above parameters must be provided.

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

### 8. Filter Travel Deals

**Endpoint:** `GET /deals/filter`

**Description:** Filter travel deals within a price range.

**Query Parameters:** (Optional, at least one recommended)

| Parameter | Type  | Required | Description   |
| --------- | ----- | -------- | ------------- |
| min_price | Float | Optional | Minimum price |
| max_price | Float | Optional | Maximum price |

**Note:** Both parameters are optional, but at least one should be provided for filtering results.

**Example:**

```bash
curl "http://localhost:5000/deals/filter?min_price=1000&max_price=5000"
```

**Validation Rules:**

* `min_price` cannot be negative
* `max_price` cannot be smaller than `min_price`
* Both must be valid numbers

---

### 9. Sort Travel Deals

**Endpoint:** `GET /deals/sort`

**Description:** Sort travel deals.

**Query Parameters:**

| Parameter | Type   | Required | Allowed Values | Description      |
| --------- | ------ | -------- | -------------- | ---------------- |
| sort_by   | String | **Yes**  | price          | Field to sort by |
| order_by  | String | Optional | asc, desc      | Sort order (default: asc) |

**Examples:**

```bash
curl "http://localhost:5000/deals/sort?sort_by=price&order_by=asc"
```

```bash
curl "http://localhost:5000/deals/sort?sort_by=price&order_by=desc"
```

**Validation Rules:**

* `sort_by` parameter is **required**
* Invalid sorting fields return HTTP 400
* Invalid sort order returns HTTP 400

---

### 10. Get Recently Viewed Deals

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

### 11. Get Most Popular Deals

**Endpoint:** `GET /deals/popular`

**Description:** Retrieve the most popular travel deals.

**Request:**

```bash
curl http://localhost:5000/deals/popular
```

**Response Example:**

```json
{
  "data": [
    {
      "id": 2,
      "destination": "Paris",
      "price": 899.99,
      "platform": "Booking.com",
      "rating": 4.9,
      "travel_type": "Flight + Hotel"
    }
  ],
  "message": "Retrieved most 5 popular deals successfully",
  "success": true
}
```

Returns the top popular deals, typically the most viewed or highest ranked.

---

### 12. Get Statistics

**Endpoint:** `GET /stats`

**Description:** Retrieve application statistics including API usage metrics.

**Request:**

```bash
curl http://localhost:5000/stats
```

**Response Example:**

```json
{
  "data": {
    "total_api_requests": 45,
    "successful_requests": 42,
    "failed_requests": 3
  },
  "message": "Statistics retrieved successfully",
  "success": true
}
```

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
  "travel_type":"Luxury"
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

### Update a Deal

```bash
curl -X PUT http://localhost:5000/deals/1 \
-H "Content-Type: application/json" \
-d '{
  "destination": "Paris",
  "price": 879.99,
  "platform": "Booking.com",
  "rating": 4.9,
  "travel_type": "Flight + Hotel"
}'
```

### Delete a Deal

```bash
curl -X DELETE http://localhost:5000/deals/1
```

### View Most Popular Deals

```bash
curl http://localhost:5000/deals/popular
```

### View Statistics

```bash
curl http://localhost:5000/stats
```


## Project Structure

```text
travel-deal/
├── app.py                         # Application entry point
├── config.py                      # Application configuration
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── Travel-Deals.postman_collection.json  # Postman API collection
├── .gitignore
├── database/
│   ├── db.py                      # Database initialization
│   ├── deals_models.py            # TravelDeal model
│   └── stats_models.py            # Statistics model
├── routes/
│   ├── deals_routes.py            # Deals API route handlers
│   └── stats_routes.py            # Statistics API route handlers
├── services/
│   ├── deals_services.py          # Deals business logic layer
│   └── stats_services.py          # Statistics business logic layer
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
| `rating` | Float | 4.8 (1-5) |
| `travel_type` | String | "Luxury" (Budget, Luxury, Family, Adventure) |


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

