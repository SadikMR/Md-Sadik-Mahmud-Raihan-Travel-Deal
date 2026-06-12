from flask import Flask

def success_response(data, message = "success", status_code=200):
    """
    Standardized Success Response
    """
    return {
        "success": True,
        "message": message,
        "data": data
    }, status_code

def error_response(message = "An error occurred", status_code=500):
    """
    Standardized Error Response
    """
    return {
        "success": False,
        "message": message,
        "data": None
    }, status_code  