from flask import Flask, render_template, jsonify,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///treasury_yield_curve_rates.db'

db = SQLAlchemy(app)

class TreasuryYieldTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255), nullable=False)
    one_mo = db.Column(db.String(255), nullable=False)
    two_mo = db.Column(db.Float, nullable=False)
    three_mo = db.Column(db.Float, nullable=False)
    six_month = db.Column(db.Float, nullable=False)
    one_year = db.Column(db.Float, nullable=False)
    two_year = db.Column(db.Float, nullable=False)
    three_year = db.Column(db.Float, nullable=False)
    five_year = db.Column(db.Float, nullable=False)
    seven_year = db.Column(db.Float, nullable=False)
    ten_year = db.Column(db.Float, nullable=False)
    twenty_year = db.Column(db.Float, nullable=False)
    thirty_year = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Treasury yield curve rates {self.id} {self.date}>"

if __name__=='__main__':
    app.run(debug=True)