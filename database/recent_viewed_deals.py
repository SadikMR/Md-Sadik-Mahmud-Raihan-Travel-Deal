from database.db import db


class RecentViewedDeal(db.Model):
    __tablename__ = "recent_viewed_deals"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    deal_id = db.Column(
        db.Integer,
        db.ForeignKey("travel_deals.id"),
        nullable=False
    )

    viewed_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "deal_id": self.deal_id,
            "viewed_at": self.viewed_at.isoformat()
        }