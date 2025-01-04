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


def adminCreateAccount_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        role = request.POST.get('role')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'adminCreateAccount.html')
        
        user = User.objects.create(
            username=username,
            password=make_password(password),
            email=email,
            first_name=firstname,
            last_name=lastname
        )
        
        SBC.objects.create(
            user=user,
            role=role,
            firstname=firstname,
            lastname=lastname
        )
        
        messages.success(request, 'Account created successfully.')
        
        if role == 'inventory':
            return redirect('inventoryDashboard')
        elif role == 'purchasing':
            return redirect('purchasingDashboard')
        elif role == 'admin':
            return redirect('adminDashboard')
        
    return render(request, 'adminCreateAccount.html')

def admin_purchase_order(request):
    return render(request, 'adminPurchaseOrder.html')

def admin_requisition_product(request):
    return render(request, 'adminRequisitionProduct.html')

def admin_product_listing(request):
    return render(request, 'adminProductListing.html')


def logout_view(request):
    logout(request)
    return redirect('login') 

