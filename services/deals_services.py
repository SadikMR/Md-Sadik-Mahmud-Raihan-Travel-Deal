import logging
from database.db import db
from database.deals_models import TravelDeal

def create_deal(data):
    """
    Creates a new travel deal in the database.
    Args:
        data (dict): A dictionary containing the travel deal details.
    Returns:
        dict: A dictionary representation of the created travel deal.
    """
    try:
        new_deal = TravelDeal(
            destination=data['destination'],
            price=data['price'],
            platform=data['platform'],
            rating=data['rating'],
            travel_type=data['travel_type']
        )

        db.session.add(new_deal)
        db.session.commit()

        logging.info(f"Created new deal: {new_deal.to_dict()}")

        return new_deal.to_dict()
    
    except Exception as e:
        logging.error(f"Error creating deal: {str(e)}")
        raise


def get_all_deals():
    """
    Retrieves all travel deals from the database.
    Returns:
        list: A list of dictionaries, each representing a travel deal.
    """
    try:
        deals = TravelDeal.query.all()
        deal_list = []

        for deal in deals:
            deal_list.append(deal.to_dict())

        return deal_list
    
    except Exception as e:
        logging.error(f"Error retrieving deals: {str(e)}")
        raise


# Additional service functions can be added here as needed, such as updating or deleting deals, or retrieving deals by specific criteria.
def get_deal_by_id(deal_id):
    """
    Retrieves a travel deal by its ID.
    Args:
        deal_id (int): The ID of the travel deal to retrieve.
    Returns:
        dict: A dictionary representation of the travel deal if found, None otherwise.
    """
    try:
        deal = TravelDeal.query.get(deal_id)

        if deal:
            return deal.to_dict()
        else:
            return None
    
    except Exception as e:
        logging.error(f"Error retrieving deal by ID: {str(e)}")
        raise