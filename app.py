import logging
from flask import Flask
from config import Config
from database.db import db
from database.deals_models import TravelDeal
from routes.deals_routes import deal_bp



def create_app():
    """
    Application Factory
    """
    app = Flask(__name__)
    
    # Load Config
    app.config.from_object(Config)
    
    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        ),
    )
    
    # Initialize DB
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(deal_bp, url_prefix="/deals")
    
    
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