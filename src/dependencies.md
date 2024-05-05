bash

pip install fastapi uvicorn gunicorn databases sqlalchemy alembic pydantic python-multipart  python-dotenv python-multipart python-jose aiofiles jinja2

Here's a brief explanation of each package:

    fastapi: The FastAPI framework itself.
    uvicorn: The ASGI server used to run the FastAPI application.
    gunicorn: A production-ready WSGI server commonly used to deploy FastAPI applications.
    databases: An asynchronous database library that provides simple asyncio support for a range of databases.
    sqlalchemy: A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
    alembic: A lightweight database migration tool for usage with SQLAlchemy.
    pydantic: A data validation and settings management library, widely used in FastAPI for request and response validation.
    python-multipart: Support for parsing multipart/form-data, commonly used for file uploads.
    python-jose[cryptography]: JSON Web Token (JWT) implementation for Python, used for authentication and authorization.
    python-dotenv: Reads the key-value pairs from a .env file and adds them to your environment variables.
    aiofiles: An asynchronous file operation library.
    jinja2: A modern and designer-friendly templating language for Python.