# Elegant Eats

This project is built for learning purposes. The main focus of it is to learn the Django fundamentals. It is inspired by [Django Masterclass : Build 9 Real World Django Projects](https://www.udemy.com/course/django-course) course made by [Ashutosh Pawar](https://www.udemy.com/user/a9ff8aeb-0700-4b60-950d-ffdce7bf69bc/).

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/hebaghazali/eleganteats.git
    cd eleganteats
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/` to see the application.


## Features

- **Menu Listing**: View a list of all menu items.
- **Item Details**: View detailed information about a specific menu item.
- **Add Item**: Add a new menu item (static HTML form).
- **Delete Item**: Delete an existing menu item (static HTML form).

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## Credits

- Images used in this project are collected from [Unsplash](https://unsplash.com/).