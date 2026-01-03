Flask Authentication & Funds API
A robust, modular Flask RESTful API featuring User Authentication (Signup/Login) and database persistence using SQLAlchemy. This project follows the Application Factory Pattern for scalability.

🚀 Features
Modular Architecture: Uses Blueprints to separate authentication from core logic.

Secure Authentication: Password hashing using werkzeug.security.

Database Integration: SQLite/SQLAlchemy with User and Funds models.

Input Validation: Checks for required fields and existing user records.


🛠️ Installation & Setup
1. Clone the repository:
   git clone <your-repo-url>
   cd my_project
   
2. Create a Virtual Environment:
   python -m venv venv
   source venv/bin/activate 

3. Install the Dependencies:
   pip install flask flask-sqlalchemy PyJWT

4. Run the Application:
   python run.py


