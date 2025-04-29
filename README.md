# Django Blog and Forum

A basic Django website that includes simple blog and forum functionality. This project is intended as a lightweight, minimal example for educational purposes or as a starting point for a more complex application.

## Features

- **User**
  -email authentication upon registration

- **Blog**
  - Create, edit, delete posts
  - View posts by author and date
  - Comment system for each post

- **Forum**
  - Categories and discussion threads
  - Users can create and reply to topics
  - Basic moderation tools (delete/edit posts)

## Tech Stack

- **Backend:** Django 4.x
- **Database:** SQLite (default), can be swapped with PostgreSQL or MySQL
- **Frontend:** HTML templates with basic styling (no frontend framework)
- **Authentication:** Django’s built-in user model

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/AntoniKingston/DjangoForumAndBlog
cd DajngoForumAndBlog
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
