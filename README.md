# Rule Engine Application

This project is a rule engine application built using Django and Django Rest Framework. It allows users to define rules, evaluate them against user data, and modify existing rules.

## Features

- Create, read, update, and delete rules.
- Evaluate rules based on user-defined data.
- Modify existing rules, including changing operators and operand values.
- User-friendly front-end for rule evaluation and modification.

## Technologies Used

- Django
- Django Rest Framework
- JavaScript (jQuery)
- HTML/CSS

## Setup Instructions

Follow these steps to set up and run the project on your local machine:

1. **Clone the repository**: Open your terminal or command prompt and run the following command to clone the project repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/zeotap.git
2. **Navigate to the project directory**: Change into the project directory with the command:
   ```bash
   cd zeotap
3. **Install required dependencies**: Use pip to install the necessary packages defined in the:
   ```bash
   pip install -r requirements.txt

4. **Apply migrations to set up the database**:Run the following command to create the necessary database tables: 
   ```bash
   python manage.py migrate

5. **Run the development server**: Start the Django development server with the command:
   ```bash
   python manage.py runserver
   

## API ENDPOINTS
- Create a rule: POST /api/rules/
- Update a rule: PUT /api/rules/<id>/
- Delete a rule: DELETE /api/rules/<id>/
- Evaluate a rule: POST /api/rules/evaluate_rule/


## FRONTEND
The frontend consists of an HTML page where users can enter rule IDs and user data to evaluate rules or modify existing ones.






   
