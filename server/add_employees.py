from models import db, Employee
from app import app  # Import the app instance

def add_employees():
    with app.app_context():
        db.session.add(Employee(name="Kai Uri", salary=89000))
        db.session.add(Employee(name="Alena Lee", salary=125000))
        db.session.commit()
        print(Employee.query.all())

if __name__ == "__main__":
    add_employees()
