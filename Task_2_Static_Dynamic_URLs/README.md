# 🧩 Task 2: Static and Dynamic URLs in Django

In this task, we explore the basics of Django URLs, their types, and how to configure them using `urls.py` and `views.py`.

---

## 🌐 What is a URL in Django?

In Django, a **URL (Uniform Resource Locator)** is a web address that maps to a specific view function. Django uses a powerful URL dispatcher to match the requested path and direct it to the appropriate logic.

All URLs are defined in a special file called `urls.py`, and the views they connect to are defined in `views.py`.

---

## 🔹 Types of URLs in Django
In Django, URLs are categorized as:

- **Static URLs**: Fixed paths that always return the same response.
- **Dynamic URLs**: Paths that accept parameters from the user and return custom responses.

| URL                             | Type       | Description                              |
|---------------------------------|------------|------------------------------------------|
| `/sta/`                         | Static     | Returns a fixed message                  |
| `/dyn/<str:name>/<int:id>/`     | Dynamic    | Returns a message using name and ID      |


This task implements both using `HttpResponse`.

---

## 📁 Project Structure
Task_2_Static_Dynamic_URLs/
├── NewProject/
│ └── urls.py
├── NewApp/
│ └── views.py
└── README.md

## ▶️ How to Run
### Run the server:
- python manage.py runserver
#### Visit these URLs in your browser:

1. Static URL:
- http://127.0.0.1:8000/sta/

2. Dynamic URL:
- http://127.0.0.1:8000/dyn/YourName/123/

- You can replace YourName and 123 with any values.
