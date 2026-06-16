import logging
from flask import Flask
from config import Config
from database.db import db
from database.deals_models import TravelDeal
from routes.deals_routes import deal_bp
from routes.stats_routes import stats_bp
import os



def create_app():
    """
    Application Factory
    """
    app = Flask(__name__)
    
    # Load Config
    app.config.from_object(Config)

    os.makedirs("logs", exist_ok=True)
    
    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler()
        ]
    )
    
    # Initialize DB
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(deal_bp, url_prefix="/deals")
    app.register_blueprint(stats_bp, url_prefix="/stats")
    
    
    @app.route("/")
    def health():
        """
        Health Check API
        """
        return {
            "message": "Travel Deal API Running"
        }
        
    @app.errorhandler(Exception)
    def handle_exception(error):
        """
        Global Error Handler
        """
        return (
            {
                "message": str(error)
            },
            500
        )
        
    # Create Tables
    with app.app_context():
        db.create_all()
        
    return app

app = create_app()

if __name__ == "__main__":
    app.run()