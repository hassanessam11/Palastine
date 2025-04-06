from Palastine import db,app
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    ip_address = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sent = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f'<User {self.username}>'