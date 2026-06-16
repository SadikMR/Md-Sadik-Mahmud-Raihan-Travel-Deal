from database.db import db

class ApiMetrics(db.Model):

    __tablename__ = "api_metrics"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    total_requests = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    successful_requests = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    failed_requests = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )



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