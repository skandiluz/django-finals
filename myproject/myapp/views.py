from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, StudentForm
from .models import Student


def register(request):
    if request.method == 'POST':
        # Get form data from POST request
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return redirect('register')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Create the new user
        user = User.objects.create_user(username=username, password=password1)

        # Automatically log them in
        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # You could save to database, send email, etc.
            messages.success(request, f"Thank you {name}! Your message has been sent.")
            return redirect('contact')
    else:
        form = ContactForm()  # Create an empty form for GET requests
    
    return render(request, 'contact.html', {'form': form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves to Student model
            messages.success(request, "Student created successfully!")
            return redirect('students_list')
    else:
        form = StudentForm()
    
    return render(request, 'student_form.html', {'form': form})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student {student.name} updated successfully!")
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f"Student {student_name} deleted successfully!")
        return redirect('students_list')
    
    return render(request, 'delete_student.html', {'student': student})

def filter_students(request):
    # Get all students
    all_students = Student.objects.all()
    
    # Filter students by age >= 18
    adult_students = Student.objects.filter(age__gte=18)
    
    # Filter students by name containing specific text
    search_term = request.GET.get('search', '')
    if search_term:
        filtered_students = Student.objects.filter(name__icontains=search_term)
    else:
        filtered_students = all_students
    
    context = {
        'all_students': all_students,
        'adult_students': adult_students,
        'filtered_students': filtered_students,
        'search_term': search_term,
    }
    
    return render(request, 'filter_students.html', context)

def create_student_direct(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        
        # Direct model creation
        student = Student(name=name, age=int(age), email=email)
        student.save()
        
        messages.success(request, f"Student {name} created successfully!")
        return redirect('students_list')
    
    return render(request, 'create_student_direct.html')

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html')
