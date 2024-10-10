from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Employee

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    
def service(request):
     employees = Employee.objects.all()  # Fetch all employee records
     return render(request, 'service.html', {'employees': employees})
    

def details(request):
    return render(request,'details.html')

def update(request):
    return render(request,'update.html')

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        age = request.POST.get('age')
        image = request.FILES.get('image')  # Get the uploaded image
        
        # Create a new Employee instance and save it
        employee = Employee(name=name, designation=designation, age=age, image=image)
        employee.save()
        
        return redirect('service')  # Redirect after saving the employee data
    
    return render(request, 'add_employee.html')


def delete_employee(request, id):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        return redirect('service')




def update_employee(request, id):
    # Fetch the employee object or return a 404 if not found
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        # Get updated data from the form
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        age = request.POST.get('age')
        image = request.FILES.get('image')

        # Update employee details
        employee.name = name
        employee.designation = designation
        employee.age = age

        # Only update the image if a new one is uploaded
        if image:
            employee.image = image

        # Save changes to the database
        employee.save()

        # Redirect to the service page after updating
        return redirect('service')

    # Render form with current employee data
    return render(request, 'update.html', {'employee': employee})