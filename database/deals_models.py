from database.db import db

class TravelDeal(db.Model):
    """
    Represents a travel deal in the database.
    Attributes:
        id (int): The unique identifier for the travel deal.
        destination (str): The destination of the travel deal.
        price (float): The price of the travel deal.
        platform (str): The platform where the deal is available.
        rating (float): The rating of the travel deal.
        travel_type (str): The type of travel.
    """

    __tablename__ = 'travel_deals'
    
    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    destination = db.Column(
        db.String(255), 
        nullable=False
    )

    price = db.Column(
        db.Float, 
        nullable=False
    )

    platform = db.Column(
        db.String(255), 
        nullable=False
    )

    rating = db.Column(
        db.Float, 
        nullable=False
    )

    travel_type = db.Column(
        db.String(255), 
        nullable=False
    )

    view_count = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )
        
    def to_dict(self):
        """
        Converts the TravelDeal object to a dictionary.
        Returns: dict: A dictionary representation of the TravelDeal object.
        """
        
        return {
            'id': self.id,
            'destination': self.destination,
            'price': self.price,
            'platform': self.platform,
            'rating': self.rating,
            'travel_type': self.travel_type,
            'view_count': self.view_count
        }