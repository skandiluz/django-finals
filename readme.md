# Overview

The Django Student Management System is a collaborative web application designed to streamline the management of student records for educational institutions. Built with Django, this platform enables administrators and authorized users to securely register, log in, and manage student data through an intuitive dashboard. Key features include adding, editing, viewing, and deleting student records, advanced search and filtering, and a contact form for feedback or inquiries. The application emphasizes security, user experience, and responsive design, making it accessible on both desktop and mobile devices. Developed as a group project, each team member contributed to different aspects of the system, ensuring a robust and user-friendly solution for student management needs.
---

## 🚀 Features
**User Authentication**
  - User registration, login, and logout
  - Only authenticated users can access student management features

- **Dashboard**
  - Quick access to all major features

- **Student Management**
  - Add, view, edit, and delete student records
  - Detailed student profile view
  - Search and filter students by name (NEW)
  - List of all students with easy navigation

- **Contact Form**
  - Users can send messages or feedback

- **Enhanced User Experience**
  - Flash messages for actions (e.g., student added, deleted)
  - Navigation bar with links to all major sections
  - Consistent styling using custom CSS

- **Security**
  - Passwords and user data securely handled using Django’s authentication system
  - Views protected with `@login_required` where necessary

- **Student Search/Filter:**  
  Users can search for students by name using the search bar on the "Search Students" page. Results update instantly based on the query.

- **Improved Dashboard:**  
  The dashboard now displays quick stats and provides direct links to all major features, including student management, adding students, contact form, and search.

- **Detailed Student View:**  
  Each student has a dedicated detail page showing all their information, with options to edit or delete.


---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, 
- **Database:** SQLite (default, can be changed)
- **Version Control:** Git & GitHub

---
Developed by beckened boys.  

Project Manager: kyle cane
UI/UX Designer: karl gomez
Frontend Developer: charles catamco
Backend Developer: mark arabis

## 📦 Setup Instructions


### 1. Create virtual environment

bash

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run migrations and start server

python manage.py migrate
python manage.py runserver

## Credits



