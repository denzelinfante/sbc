from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SBC
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


def my_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminAccounts')  # Redirect to admin accounts page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'my_login.html')

def admin_accounts(request):
    users = SBC.objects.all()
    if request.method == "POST":
        if "delete" in request.POST:
            user_id = request.POST.get('user_id')
            user_to_delete = get_object_or_404(SBC, id=user_id)
            user_to_delete.user.delete()  # This deletes both the SBC profile and the associated User
            return redirect('adminAccounts')
    return render(request, 'adminAccounts.html', {'users': users})
    pass

def update_account(request, user_id):
    user_profile = get_object_or_404(SBC, id=user_id)
    if request.method == 'POST':
        user_profile.firstname = request.POST.get('firstname')
        user_profile.lastname = request.POST.get('lastname')
        user_profile.role = request.POST.get('role')
        user_profile.is_active = request.POST.get('is_active') == 'on'
        user_profile.save()
        user_profile.user.email = request.POST.get('email')
        user_profile.user.username = request.POST.get('username')
        user_profile.user.save()
        return redirect('adminAccounts')
    return render(request, 'updateAccount.html', {'user_profile': user_profile})

def delete_account(request, user_id):
    try:
        user_profile = get_object_or_404(SBC, id=user_id)
        user_profile.user.delete()  # This deletes both the SBC profile and the associated User
        messages.success(request, "Account deleted successfully.")
    except SBC.DoesNotExist:
        messages.error(request, "Account not found.")
    return redirect('adminAccounts')

def adminCreateAccount_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'adminCreateAccount.html')
        
        user = User.objects.create(
            username=username,
            password=make_password(password)
        )
        
        SBC.objects.create(
            user=user,
            role=role
        )
        
        messages.success(request, 'Account created successfully.')
        
        # Role-based redirection
        if role == 'inventory':
            return redirect('inventoryDashboard')
        elif role == 'purchasing':
            return redirect('purchasingDashboard')
        elif role == 'admin':
            return redirect('adminDashboard')
        
    return render(request, 'adminCreateAccount.html')

def create_account(request):
    # Your logic for creating an account goes here
    return HttpResponse("Account creation page")


def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def adminPurchaseOrder_view(request):
    return render(request, 'adminPurchaseOrder.html')

@login_required
def adminRequisitionProduct_view(request):
    return render(request, 'adminRequisitionProduct.html')

@login_required
def adminProductListing_view(request):
    return render(request, 'adminProductListing.html')

def adminCreateAccount_view(request):
    return render(request, 'adminCreateAccount.html')

@login_required
def inventory_dashboard(request):
    return render(request, 'inventoryDashboard.html')

@login_required
def purchasing_dashboard(request):
    return render(request, 'purchasingDashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'adminDashboard.html')

