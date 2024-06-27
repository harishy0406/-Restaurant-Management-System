# Restaurant Management System 🍽️

## Description 📝
The Restaurant Management System is a Python-based application developed using Tkinter for the graphical user interface (GUI) and MySQL for the database. This system is designed to streamline table reservations, order processing, and inventory tracking. It was created as a project for my Class 12th Computer Science course.

## Features ✨
- Table reservations 📅
- Order processing 📝
- Inventory tracking 📦
- User-friendly GUI 🎨

## Installation ⚙️

### Prerequisites
- [Python](https://www.python.org/downloads/) 🐍
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [MySQL](https://www.mysql.com/downloads/)
- [XAMPP](https://www.apachefriends.org/index.html) (for managing MySQL server)

### Setup
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Restaurant-Management-System.git
    ```

2. **Install required Python packages:**
    ```bash
    pip install mysql-connector-python
    pip install tkinter
    ```

3. **Setup XAMPP:**
    - Start Apache and MySQL modules in XAMPP control panel.
    - Open phpMyAdmin and create a database named `restaurant_db`.
    - Import the `restaurant_db.sql` file located in the project's `db` directory to set up the database schema and initial data.

4. **Configure database connection:**
    - Open `db_connection.py` file.
    - Update the database host, user, password, and database name as per your XAMPP setup.
    ```python
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'restaurant_db'
    }
    ```

## Usage 🚀
1. **Run the project:**
    ```bash
    python main.py
    ```

2. **Navigate through the system:**
    - Use the GUI to manage table reservations, process orders, and track inventory.

## Snapshots 📸
Here are some snapshots of the project:

![image](https://github.com/harishy0406/Restaurant-Management-System/assets/142865295/d656bb1b-e8b3-4e23-9e33-40251e39b925)


![image](https://github.com/harishy0406/Restaurant-Management-System/assets/142865295/ad60bf67-451d-43f5-9c69-d6594dc599f6)

![image](https://github.com/harishy0406/Restaurant-Management-System/assets/142865295/c6959ac1-ce5d-4164-aa72-88ba443e3ca1)


Thank you for visiting my Restaurant Management System project! 😊 Feel free to explore and reach out if you have any questions or opportunities. 📫



