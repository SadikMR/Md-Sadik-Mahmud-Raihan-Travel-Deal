# config.py

class Config:
    """
    Application Configuration
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///travel_deals.db"
    
    # Disable unnecessary tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Enable debug mode
    DEBUG = True