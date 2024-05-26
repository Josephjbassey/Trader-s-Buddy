# Trading Journal Web Application with Wagtail

This project is a comprehensive trading journal web application built using Wagtail, a Django-based CMS. The application includes features for logging trades, managing compound growth goals, a daily to-do checklist, and a risk management calculator.

## Features

- **Trading Journal**: Log, view, edit, and delete trade entries with detailed information.
- **Compound Plan Goal Checker**: Set and track compound growth goals for your trading account.
- **Daily To-Do Checklist**: Manage daily tasks with the ability to mark them as complete or incomplete.
- **Risk Management Calculator**: Calculate the appropriate position size for trades based on account balance and risk-to-reward ratio.
- **User Authentication**: Register, log in, and log out. Each user's data is private and accessible only to them.

## Technology Stack

- Python
- Django
- Wagtail
- PostgreSQL (or another database of your choice)
- HTML/CSS
- JavaScript

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- PostgreSQL (optional, for production use)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/trading-journal.git
   cd trading-journal
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Update the `DATABASES` setting in `trading_journal/settings.py` to configure your database. By default, it uses SQLite. For production, configure PostgreSQL or another database.

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your web browser to see the application.

### Using GitHub Codespaces

1. **Open the repository in GitHub Codespaces:**

   Go to your repository on GitHub, click the `Code` button, and select `Open with Codespaces`.

2. **Set up the virtual environment and install dependencies:**

   In the terminal provided by Codespaces:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up the database and run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   Follow the link provided by Codespaces to access the application in your web browser.

## Project Structure

- `trading_journal/`: Root project directory.
- `journal/`: Contains the trading journal app.
- `users/`: Contains user authentication logic.
- `goals/`: Manages compound plan goals.
- `checklist/`: Manages daily to-do tasks.
- `calculator/`: Implements the risk management calculator.
- `templates/`: HTML templates for the application.
- `static/`: Static files (CSS, JavaScript).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Wagtail](https://wagtail.io/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/) (optional, for frontend styling)
