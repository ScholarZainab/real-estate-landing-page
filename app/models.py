class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    premium_category = db.Column(db.String(20), default="Standard")  # New field
    is_premium = db.Column(db.Boolean, default=False)  # Highlight premium properties
