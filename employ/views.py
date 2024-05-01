from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Employee
from .forms import EmployeeForm,EmployeeUpdateForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from .models import Employee, Department
from django.contrib.auth import logout


@login_required
def logout_view(request):
    logout(request)
    return redirect('employee_login') 

@login_required
def employee_list(request):
    departments = Department.objects.all()
    department_id = request.GET.get('department')  # Get the department ID from the query parameters

    if department_id:
        employees = Employee.objects.filter(department_id=department_id)
    else:
        employees = Employee.objects.all()

    return render(request, 'employee_list.html', {'employees': employees, 'departments': departments})

@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            username = employee.first_name+employee.last_name
            password = User.objects.make_random_password()
            user = User.objects.create_user(username=username, password=password)
            employee.user = user
            employee.save()
            send_login_credentials(employee.first_name,username,password,employee.email)
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

@login_required
def employee_delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.user.delete()
    employee.delete()
    return redirect('employee_list')


@login_required
def employee_profile_update(request):
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, request.FILES, instance=request.user.employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('employee_profile_update')
    else:
        form = EmployeeUpdateForm(instance=request.user.employee)
    return render(request, 'employees/employee_profile_update.html', {'form': form})


def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("employee_list")
            else :
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


@login_required
def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            if request.user.is_superuser:
                return redirect('employee_list')
            else:
                return redirect('employee_dashboard')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

@login_required
def employee_dashboard(request):
    employee = request.user.employee  # Assuming 'Employee' model is linked to the user
    context = {'employee': employee}
    return render(request, 'employee_dashboard.html', context)


#helper
def send_login_credentials(first_name,username,password,email):
    subject = 'Login Credentials'
    message = f'Hello {first_name}, your login credentials are:\nUsername: {username}\nPassword: {password}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)