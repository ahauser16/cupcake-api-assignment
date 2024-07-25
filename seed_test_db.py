# seed.py
from models.models import db, Cupcake
from dotenv import load_dotenv
import os

def seed_database():
    from app import app  # Move the import statement here
    load_dotenv()  # Load environment variables from .env file
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
    with app.app_context():
        db.drop_all()
        db.create_all()

        c1 = Cupcake(
            flavor="cherry",
            size="large",
            rating=5,
        )

        c2 = Cupcake(
            flavor="chocolate",
            size="small",
            rating=9,
            image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg",
        )

        db.session.add_all([c1, c2])
        db.session.commit()
        
if __name__ == "__main__":
    seed_database()
    print("Database seeding completed.")