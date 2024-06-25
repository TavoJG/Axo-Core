# AXO - Core

This repository contains the backend logic for the AXO Core project

## Table of Contents

- [Project Name](#axo-core)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setting Up](#setting-up)
  - [Usage](#usage)
  - [Running the Tests](#running-the-tests)
  - [Deployment](#deployment)
  - [Built With](#built-with)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Installation

### Prerequisites

- Python ~ 3.11
- Django 5.0 or higher
- Virtualenv (optional but recommended)

### Setting Up

1. Clone the repository:

   ```bash
   git clone https://github.com/TavoJG/Axo-Core
   cd yourproject
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Running the Tests

To run the tests, execute:

```bash
python manage.py test
```

## Deployment

To deploy this project, follow these steps:

1. Set up a production-ready environment (e.g., using Gunicorn and Nginx).
2. Configure the settings for production.
3. Collect static files:

   ```bash
   python manage.py collectstatic
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the application server (e.g., Gunicorn):

   ```bash
   gunicorn yourproject.wsgi:application
   ```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [DRF](https://www.django-rest-framework.org) - REST Framework

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
