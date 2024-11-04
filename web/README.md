
# StudyBuddy

StudyBuddy is a web application built with Django that helps students connect, collaborate, and study together. This README provides an overview of the project, setup instructions, and usage guidelines.

## Features

- User authentication and profiles
- Create and join study groups
- Schedule study sessions
- Share resources and notes
- Real-time chat

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/StudyBuddy.git
    ```
2. Navigate to the project directory:
    ```bash
    cd StudyBuddy
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new account or log in with your superuser credentials.
3. Explore the features and start collaborating with other students.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the project's coding standards and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer at your.email@example.com.
