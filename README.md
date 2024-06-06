"# blogrestapi" 

A simple Django REST Framework API for managing blog posts and categories.

## Features

- Create, retrieve, and update blog posts
- Create, retrieve, and update categories

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/B-nod/blogrestapi
   cd blogapi

2. **Create and activate a virtual environment:**
- python -m venv blog_venv
- blog_venv\scripts\activate  # to activate the virtual environment

3. **Install the required packages:**
- pip install -r requirements.txt

4. **Migrations, migrate and runserver:**
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

### Model

*** Category ***
- id: Integer, primary key
- name: String, name of the category

*** Blog ***
- id: Integer, primary key
- title: String, title of the blog post
- description: Text, description of the blog post
- category: ForeignKey, related category

### API Endpoints

*** Blogs ***
- POST localhost:8000/blogs/ : Create a new blog
- GET localhost:8000/blogs/ : List all blogs
- GET localhost:8000/blogs/5/ : Retrieve a blog by ID
- PUT localhost:8000/blogs/2/ : Update a blog by ID

*** Categories ***
- POST localhost:8000/categories/ : Create a new category
- GET localhost:8000/categories/ : List all categories
- GET localhost:8000/categories/4/ : Retrieve a category by ID
- PUT localhost:8000/categories/1/ : Update a category by ID
