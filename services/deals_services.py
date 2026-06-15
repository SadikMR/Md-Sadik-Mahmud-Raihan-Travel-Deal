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
        
        logging.info(f"Retrieved {len(deal_list)} deals from the database")

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
            logging.info(f"Retrieved deal by ID {deal_id}: {deal.to_dict()}")
            return deal.to_dict()
        else:
            logging.warning(f"Deal with ID {deal_id} not found")
            return None
    
    except Exception as e:
        logging.error(f"Error retrieving deal by ID: {str(e)}")
        raise


# Search for deals based on destination, platform, or travel type
def search_deal(destination=None, platform=None, travel_type=None):
    try:
        query = TravelDeal.query

        if destination:
            query = query.filter(
                TravelDeal.destination.ilike(f"%{destination}%")
            )

        if platform:
            query = query.filter(
                TravelDeal.platform.ilike(f"%{platform}%")
            )

        if travel_type:
            query = query.filter(
                TravelDeal.travel_type.ilike(f"%{travel_type}%")
            )

        results = query.all()

        logging.info(
            f"Search completed. Found {len(results)} deals. "
            f"destination={destination}, "
            f"platform={platform}, "
            f"travel_type={travel_type}"
        )
        return [deal.to_dict() for deal in results]

    except Exception as e:
        logging.error(f"Error searching deals: {e}")
        raise