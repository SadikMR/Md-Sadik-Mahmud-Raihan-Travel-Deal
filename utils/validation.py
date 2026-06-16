# validation functions for validating incoming data for creating and updating deals.
def validate_deal_data(data):
    """
    Validates the incoming deal data.
    Returns a tuple (is_valid, message) where:
    - is_valid: True if data is valid, False otherwise
    - message: Error message if data is invalid, None otherwise
    """

    if not data:
            return False, "No JSON payload provided"
        
    required_fields = ["destination", "price", "platform", "rating", "travel_type"]
        
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"

    allowed_travel_types = ["Budget", "Luxury", "Family", "Adventure"]
    
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
    
    platform = data.get("platform")
    if not isinstance(platform, str) or not platform.strip():
        return False, "Platform must be a non-empty string"
    
    return True, None
    


# Additional validation functions can be added here as needed, such as validating query parameters for filtering or searching deals.
def validate_filter_params(min_price, max_price):
    """
    Validates the filter parameters for price.
    Returns a tuple (is_valid, message) where:
    - is_valid: True if parameters are valid, False otherwise
    - message: Error message if parameters are invalid, None otherwise
    """
    
    if min_price is not None:
        try:
            min_price = float(min_price)
            if min_price < 0:
                return False, "min_price must be a non-negative number"
        except ValueError:
            return False, "min_price must be a valid number"
    
    if max_price is not None:
        try:
            max_price = float(max_price)
            if max_price < 0:
                return False, "max_price must be a non-negative number"
        except ValueError:
            return False, "max_price must be a valid number"
    
    if min_price is not None and max_price is not None and min_price > max_price:
        return False, "min_price cannot be greater than max_price"
    
    return True, None


# Validation function for sorting parameters
def validate_sort_params(sort_by, sort_order):
    """
    Validates the sorting parameters for deals.
    Returns a tuple (is_valid, message) where:
    - is_valid: True if parameters are valid, False otherwise
    - message: Error message if parameters are invalid, None otherwise
    """
    
    allowed_sort_by = ["price"]
    allowed_sort_order = ["asc", "desc"]

    if not sort_by:
        return False, "sort_by parameter is required"
    
    if sort_by and sort_by not in allowed_sort_by:
        return False, f"sort_by must be one of: {', '.join(allowed_sort_by)}"
    
    if sort_order and sort_order not in allowed_sort_order:
        return False, f"sort_order must be one of: {', '.join(allowed_sort_order)}"
    
    return True, None