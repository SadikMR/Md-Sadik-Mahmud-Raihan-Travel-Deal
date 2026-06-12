def validate_deal_data(data):
    """
    Validates the incoming deal data.
    Returns a tuple (is_valid, message) where:
    - is_valid: True if data is valid, False otherwise
    - message: Error message if data is invalid, None otherwise
    """
    required_fields = ["rating", "travel_type", "price", "destination"]

    allowed_travel_types = ["Budget", "Luxury", "Family", "Adventure"]
    
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    price = data.get("price")
    if not isinstance(price, (int, float)) or price < 0:
        return False, "Price must be a non-negative number"
    
    rating = data.get("rating")
    if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
        return False, "Rating must be a number between 1 and 5"
    
    travel_type = data.get("travel_type")
    if travel_type not in allowed_travel_types:
        return False, f"Travel type must be one of: {', '.join(allowed_travel_types)}"
    
    destination = data.get("destination")
    if not isinstance(destination, str) or not destination.strip():
        return False, "Destination must be a non-empty string"
    
    return True, None
    