from datetime import datetime
from joke_generator import db

class Jokes(db.Model):
    __tablename__ = 'jokes'
    id = db.Column('id', db.Integer, primary_key=True)
    joke = db.Column('joke', db.Text, nullable=False)
    sentiment = db.Column('sentiment', db.Numeric(precision=10, scale=2), nullable=False)
    date_added = db.Column('date_added', db.Date, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': str(self.id),
            'joke': self.joke,
            'sentiment': self.sentiment
        }
    
class CleanJokes(db.Model):
    __tablename__ = 'cleanjokes'
    id = db.Column('id', db.Integer, primary_key=True)
    joke = db.Column('joke', db.Text, nullable=False)
    sentiment = db.Column('sentiment', db.Numeric(precision=10, scale=2), nullable=False)
    date_added = db.Column('date_added', db.Date, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': str(self.id),
            'joke': self.joke,
            'sentiment': self.sentiment
        }

