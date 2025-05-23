# 🎓Django Student Management System

a web-based student management system built using the Django framework. It allows administrators to manage student records, track performance, and interact with the platform securely via login and registration systems.

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
- **Frontend:** HTML, CSS, Bootstrap (custom styles)
- **Database:** SQLite (default, can be changed)
- **Version Control:** Git & GitHub

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name



### 2. Create virtual environment

bash

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

###  4. Run migrations and start server

python manage.py migrate
python manage.py runserver

## Credits

Developed by beckened boys.  

Project Manager: kyle cane
UI/UX Designer: karl gomez
Frontend Developer: charles catamco
Backend Developer: mark arabis

