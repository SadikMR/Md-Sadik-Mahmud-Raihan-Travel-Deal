import logging
from flask import Blueprint, request, jsonify
from services.deals_services import create_deal, get_all_deals, get_deal_by_id
from utils.responses import error_response, success_response
from utils.validation import validate_deal_data

deal_bp = Blueprint("deals", __name__) 

logger = logging.getLogger(__name__)

# API Endpoint to add a new travel deal
@deal_bp.route("", methods=["POST"])
def add_deal():
    """
    API Endpoint to add a new travel deal.
    Expects JSON body with:
    {
        "destination": "string",
        "price": float,
        "platform": "string",
        "rating": float,
        "travel_type": "string"
    }
    """
    try:
        data = request.get_json(silent=True) 

        if not data:
            return error_response("No JSON payload provided", 400)
        
        required_fields = ["destination", "price", "platform", "rating", "travel_type"]
        
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return error_response(f"Missing required fields: {', '.join(missing_fields)}", 400)

        # Validate incoming data
        is_valid, validation_message = validate_deal_data(data)

        if not is_valid:
            logger.warning(f"Validation failed: {validation_message}")
            return error_response(validation_message, 400)
        
        # Create the deal using the service layer
        new_deal = create_deal(data)
        return success_response(new_deal, 201)
    
    except Exception as e:
        logger.error(f"Error in add_deal endpoint: {str(e)}")
        return error_response("An error occurred while adding the deal", 500) 
    


# API Endpoint to retrieve all travel deals
@deal_bp.route("", methods=["GET"])
def get_deals():
    """
    API Endpoint to retrieve all travel deals.
    """
    try:
        # Retrieve all deals using the service layer
        deals = get_all_deals()
        return success_response(deals, "Deals retrieved successfully", 200)
    
    except Exception as e:
        logger.error(f"Error in get_deals endpoint: {str(e)}")
        return error_response("An error occurred while retrieving the deals", 500)
    
    

# API Endpoint to retrieve a specific travel deal by ID
@deal_bp.route("/<int:deal_id>", methods=["GET"])
def get_deal(deal_id):
    """
    API Endpoint to retrieve a specific travel deal by ID.
    """
    try:
        # Retrieve the deal using the service layer
        deal = get_deal_by_id(deal_id)
        if not deal:
            return error_response("Deal not found", 404)
        
        return success_response(deal, "Deal retrieved successfully", 200)
    
    except Exception as e:
        logger.error(f"Error in get_deal endpoint: {str(e)}")
        return error_response("An error occurred while retrieving the deal", 500)