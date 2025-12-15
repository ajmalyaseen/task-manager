# 📝 Django To-Do App

A simple and efficient To-Do List application built with Django. This app allows users to create accounts, manage their daily tasks, and customize their profiles.

## 🚀 Features

* **User Authentication:** Secure Sign Up, Login, and Logout functionality.
* **CRUD Operations:** Create, Read, Update, and Delete tasks easily.
* **Profile Management:** Users can update their profile details.
* **Dynamic Avatars:** * Users can upload a profile picture.
    * If no picture is uploaded, the app automatically generates a **First Letter Avatar** (like Gmail).
* **Responsive Design:** Works well on both desktop and mobile.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (Default)

## 💻 How to Run This Project

Follow these steps to run the project locally on your machine:

### 1. Clone the repository

```bash
git clone [https://github.com/ajmalyaseen/task-manager](https://github.com/ajmalyaseen/task-manager)
cd YOUR_REPO_NAME

```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```
### 6. Run the Server
```bash

python manage.py runserver

```
Open your browser and go to http://127.0.0.1:8000/ to see the app!

🤝 Contributing
Feel free to fork this repository and submit pull requests.

Made with ❤️ by [Ajmal yaseen]