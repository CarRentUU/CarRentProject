# CarRentProject
## Urmia University Software Project



The project is built with a clean MVC-style architecture (Model–View–Controller). That basically means the code is split into:

Models → define what a car, customer, or rental looks like.

Controllers → contain the rules (e.g., “you can’t rent a car if it’s already taken”).

Data Access → a simple in-memory database that stores everything.

This setup keeps things tidy and makes it easy to extend later — for example, if you want to plug in a real database or build a web app on top of it.

✨ What You Can Do

👤Add and manage customers 

🚘Register and update cars 

📄Rent cars to customers and track their rentals 

🔄Return cars and free them up for the next rental 

🏗️Project Structure
```
final_project/
├── main.py                # Entry point
├── controller/            # Business logic (Car, Person, Rental controllers)
├── model/
│   ├── entity/            # Car, Person, Rental classes
│   └── da/                # Data Access layer (acts like a mini database)
```
⚙️How It Works

🔮Entities
Think of these as blueprints: a Car, a Person, and a Rental. Each one has its own properties, like a car’s model or a customer’s name.

🔮Data Access
Instead of using a real database, the project currently uses in-memory storage (just Python objects in lists). It’s simple but can be swapped out for a real DB later.

🔮Controllers
This is where the rules live. For example:

🔮You can’t rent a car that’s already rented.

🔮You can’t register the same person twice.

Main Program
The main.py script ties everything together. Right now, it’s command-line–based, but the architecture is ready for bigger things (like a GUI or API).

🚀 Getting Started
Requirements

Python 3.10+

Installation
```
git clone https://github.com/CarRentUU/CarRentProject.git
cd CarRentProject
```
Run it
```
python main.py
```
📌 Example Usage

Here’s how you’d use the system in code:

# Register a customer
```
from controller.person_controller import PersonController
pc = PersonController()
pc.register(name="Alice", contact="alice@email.com")
```
# Add a car
```
from controller.car_controller import CarController
cc = CarController()
cc.register(model="Toyota Corolla", year=2022)
```
# Rent a car
```
from controller.rental_controller import RentalController
rc = RentalController()
rc.rent(car_id=1, person_id=1, rental_date="2025-09-08")

# Return it
rc.return_car(rental_id=1, return_date="2025-09-10")
```

## Test Execution

#### 1. Using the Custom Test Runner
```bash
# Run all tests
python run_tests.py

# Run with verbose output
python run_tests.py -v

# Run specific test pattern
python run_tests.py --pattern "test_car*"

# Run tests from specific directory
python run_tests.py --dir tests/model
```

#### 2. Using Python's unittest module
```bash
# Run specific test file
python -m unittest tests.model.test_car

# Run with verbose output
python -m unittest discover tests -v
```
