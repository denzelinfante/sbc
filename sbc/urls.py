from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_login_view, name='login'),  # Login URL
    path('adminAccounts/', views.admin_accounts, name='adminAccounts'),  # Home URL after login
    path('adminCreateAccount/', views.adminCreateAccount_view, name='adminCreateAccount'),
    path('inventory/', views.inventory_dashboard, name='inventoryDashboard'),
    path('purchasing/', views.purchasing_dashboard, name='purchasingDashboard'),
    path('admin/', views.admin_dashboard, name='adminDashboard'),



    
    path('logout/', views.logout_view, name='logout'),  # Logout URL
    path('adminPurchaseOrder/', views.adminPurchaseOrder_view, name='adminPurchaseOrder'),
    path('adminRequisitionProduct', views.adminRequisitionProduct_view, name='adminRequisitionProduct'),
    path('adminProductListing', views.adminProductListing_view, name='adminProductListing'),
    path('admin/accounts/update/<int:user_id>/', views.update_account, name='update_account'),  # Update account
    path('admin/accounts/delete/<int:user_id>/', views.delete_account, name='delete_account'),  # Delete account
    path('admin/accounts/create/', views.create_account, name='create_account'),

]
