import logging
from database.db import db
from database.deals_models import TravelDeal
from database.recent_viewed_deals import RecentViewedDeal

# Service function to create a new travel deal in the database
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



# Service function to retrieve all travel deals from the database
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
            add_recent_viewed_deal(deal_id)
            return deal.to_dict()
        else:
            logging.warning(f"Deal with ID {deal_id} not found")
            return None
    
    except Exception as e:
        logging.error(f"Error retrieving deal by ID: {str(e)}")
        raise



# Search for deals based on destination, platform, or travel type
def search_deal(destination=None, platform=None, travel_type=None):
    """
    Search for deals based on destination, platform, or travel type.
    Args:
        destination (str, optional): The destination to search for.
        platform (str, optional): The platform to search for.
        travel_type (str, optional): The travel type to search for.
    Returns:
        list: A list of dictionaries.
    """

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



# Filter deals based on price range
def filter_deals_by_price(min_price=None, max_price=None):
    """
    Filter deals based on price range.
    Args:
        min_price (float, optional): The minimum price to filter by.
        max_price (float, optional): The maximum price to filter by.
    Returns:
        list: A list of dictionaries.
    """

    try:
        query = TravelDeal.query

        if min_price is not None:
            query = query.filter(TravelDeal.price >= min_price)

        if max_price is not None:
            query = query.filter(TravelDeal.price <= max_price)

        results = query.all()

        logging.info(
            f"Filter completed. Found {len(results)} deals. "
            f"min_price={min_price}, max_price={max_price}"
        )
        return [deal.to_dict() for deal in results]

    except Exception as e:
        logging.error(f"Error filtering deals: {e}")
        raise



# Sort deals based on price
def sort_deals_by_price(sort_by = 'price', order_by="asc"):
    """
    Sort deals based on price.
    Args: sort_by(str): The field to sort by (currently only supports 'price').
        order_by (str): The order to sort by ('asc' for ascending, 'desc' for descending).
    Returns: list: A list of dictionaries.
    """

    try:
        query = TravelDeal.query

        if sort_by == 'price':
            if order_by == "desc":
                query = query.order_by(TravelDeal.price.desc())
            else:
                query = query.order_by(TravelDeal.price.asc())
        
        results = query.all()

        logging.info(
            f"Sorting completed. Found {len(results)} deals. "
            f"sort_by={sort_by}, order_by={order_by}"
        )
        return [deal.to_dict() for deal in results]
        
    except Exception as e:
        logging.error(f"Error sorting deals: {e}")
        raise



# services for adding to recent viewd deal. It's called automaticaly when user searched specific deal by id
def add_recent_viewed_deal(deal_id):
    """
    Creates new recent viewed deal in recent viewd deals table
    Args: deal_id(int): The field to identify specific deal
    Returns: A dictionary represents deal
    """
    
    try:
        recent_viewed_deal = RecentViewedDeal(
            deal_id = deal_id
        )
        db.session.add(recent_viewed_deal)
        db.session.commit()

        logging.info(f"Added to recent_viewed_deal")
        return recent_viewed_deal.to_dict()
    
    except Exception as e:
        logging.error(f"Error adding to recent_viewd_deal: {e}")
        raise



#Services for retrieving recent_viewed_deals
def get_recent_viewed_deals():
    """
    Fetches all recent viewed deals based on views time
    returns: A list of dictionary representing recent viewd deals
    """

    try:
        recent_viewed_deals = (RecentViewedDeal.query.order_by(RecentViewedDeal.viewed_at.desc()).all())
        deals = []

        for recent_viewed_deal in recent_viewed_deals:
            deal = TravelDeal.query.get(recent_viewed_deal.deal_id)
            if(deal): 
                deals.append(deal.to_dict())
        
        logging.info(f"Retrivied recent_viewd deals. Found {len(deals)}")
        return deals
    
    except Exception as e:
        logging.error(f"Error fetching recent viewed deals: {e}")
        raise
