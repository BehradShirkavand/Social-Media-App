# Social-Media-App

A simple social media application built with Django. This project demonstrates the core functionalities of a social media platform and serves as an excellent starting point for developers looking to explore Django's capabilities.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About the Project

The Social Media App is a beginner-friendly Django project designed to mimic basic features of a social media platform. It allows users to create accounts, post updates, and interact with other users. This project showcases Django's Model-View-Template (MVT) architecture and is a great tool for learning how to build scalable web applications.

### Key Objectives

- Demonstrate Django's functionality in building web applications.
- Provide a simple and modular codebase for learning and expansion.
- Serve as a foundation for more advanced social media projects.

## Features

- User Authentication (Sign Up, Login, Logout).
- Create, Edit, and Delete Posts.
- View Posts by Other Users.
- Reply to Posts.
- Basic User Profiles.

## Technologies Used

- **Python** (80.9% of the code)
- **HTML** (19.1% of the code)
- **Django Framework**

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package manager)
- A virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BehradShirkavand/Social-Media-App.git
   cd Social-Media-App
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

Once the application is running, you can:

- **Sign Up**: Create a new user account.
- **Create Posts**: Share your updates with other users.
- **View Posts**: Browse posts created by other users.
- **Edit/Delete Posts**: Manage the content you have shared.

Feel free to explore the app and expand its functionality as needed!

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add NewFeature'`).
4. Push the branch (`git push origin feature/NewFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- Tutorials and guides that inspired this project.
- The open-source community for their invaluable resources and support.
