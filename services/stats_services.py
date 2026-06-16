import logging
from database.db import db
from database.stats_models import SearchAnalytics, ApiMetrics
from database.deals_models import TravelDeal

# works as service for the endpoint (GET /stats)
def get_statistics():
    """
    Retrieves application statistics.

    Returns:
        dict: Statistics data.
    """

    try:
        metrics = ApiMetrics.query.first()

        most_viewed_deal = TravelDeal.query.order_by(
            TravelDeal.view_count.desc()
        ).first()

        most_searched = SearchAnalytics.query.order_by(
            SearchAnalytics.search_count.desc()
        ).first()

        most_viewed_deal_data = None

        if (
            most_viewed_deal and
            most_viewed_deal.view_count > 0
        ):
            most_viewed_deal_data = {
                "id": most_viewed_deal.id,
                "destination": most_viewed_deal.destination,
                "price": most_viewed_deal.price,
                "platform": most_viewed_deal.platform,
                "rating": most_viewed_deal.rating,
                "travel_type": most_viewed_deal.travel_type,
                "view_count": most_viewed_deal.view_count
            }

        statistics = {
            "total_requests": (
                metrics.total_requests if metrics else 0
            ),
            "successful_requests": (
                metrics.successful_requests if metrics else 0
            ),
            "failed_requests": (
                metrics.failed_requests if metrics else 0
            ),
            "most_searched_destination": (
                most_searched.destination
                if most_searched else None
            ),
            "most_viewed_deal": (
                most_viewed_deal_data
            )
        }

        logging.info(
            "Statistics retrieved successfully"
        )

        return statistics

    except Exception as e:
        logging.error(
            f"Error retrieving statistics: {e}"
        )
        raise


# Function that stores data in api_metrices 
def track_api_request(success=True):
    """
    Track API usage statistics.

    Args:
        success (bool): True if request succeeded, False otherwise.
    """

    try:
        metrics = ApiMetrics.query.first()

        if not metrics:
            metrics = ApiMetrics()
            db.session.add(metrics)

        metrics.total_requests += 1

        if success:
            metrics.successful_requests += 1
        else:
            metrics.failed_requests += 1

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error tracking API metrics: {e}")
        raise


# Helping service for storing in service_stats model
def track_search(search_term):
    """
    Track search terms for analytics.

    Args:
        search_term (str): The search term entered by the user.
    """

    try:
        if not search_term:
            return

        search = SearchAnalytics.query.filter_by(
            destination=search_term.lower().strip()
        ).first()

        if search:
            search.search_count += 1
        else:
            search = SearchAnalytics(
                destination=search_term.lower().strip(),
                search_count=1
            )
            db.session.add(search)

        db.session.commit()

        logging.info(
            f"Tracked search term '{search_term}' successfully"
        )

    except Exception as e:
        db.session.rollback()

        logging.error(
            f"Error tracking search term '{search_term}': {e}"
        )

        raise