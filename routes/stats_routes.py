import logging
from flask import Blueprint

from services.stats_services import get_statistics, track_api_request
from utils.responses import (
    success_response,
    error_response
)

stats_bp = Blueprint(
    "stats",
    __name__
)


@stats_bp.route("/", methods=["GET"])
def statistics():
    """
    API Endpoint to retrieve application statistics.
    """

    try:
        statistics = get_statistics()

        track_api_request(success=True)

        return success_response(
            statistics,
            "Statistics retrieved successfully",
            200
        )

    except Exception as e:
        logging.error(
            f"Error retrieving statistics: {e}"
        )

        return error_response(
            "An error occurred while retrieving statistics",
            500
        )