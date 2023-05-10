<!-- ABOUT THE PROJECT -->
## About The Project

QUAN LY KHACH SAN :smile:

This project aims  to provide a Hotel Management System for Manager:
* View information of each Customer
* View information of Customer's Booking
* Add new Room Type
* View statistics of each hotel branch


### Built With
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Django][djangoproject.com]][Django-url]
* Mysql as Database

## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/siunhanvjp/hotel-management
   ```
2. Configure Database settings in settings.py in folder "project" at line 86

3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Migrate database
   ```sh
   python manage.py migrate
   ```

## Usage

Create a user with DBA

   ```sh
   python manage.py createsuperuser
   ```
Then you proceed to create a Username and Password.

Run the website
   ```sh
   python manage.py runserver
   ```





