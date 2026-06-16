from database.db import db

class SearchAnalytics(db.Model):
    __tablename__ = "search_analytics"

    id = db.Column(db.Integer, primary_key=True)

    destination = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    search_count = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )