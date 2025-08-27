# Blog API with FastAPI, Pydantic, and SQLAlchemy

This is a simple **Blog API** built using **FastAPI**, **Pydantic**, and **SQLAlchemy** (MySQL). It demonstrates CRUD operations, relationships between users and posts, and API request/response validation using Pydantic models.

---

## Features

- **User Endpoints**
  - Get all users
  - Get user by ID
  - Create a new user
- **Post Endpoints**
  - Get all posts
  - Create a post for a specific user
- **Validation**
  - Request and response validation with **Pydantic models**
- **Database**
  - MySQL integration using **SQLAlchemy ORM**
  - One-to-many relationship: User → Posts
- **Error Handling**
  - Raises appropriate HTTP exceptions (404, 400)

---

## Tech Stack

- **Python 3.11+**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **MySQL**
- **Uvicorn** (ASGI server)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd blog-fastapi
