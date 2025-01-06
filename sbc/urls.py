from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_login_view, name='login'),  # Login URL
    path('adminAccounts/', views.admin_accounts, name='adminAccounts'),  # Home URL after login
    path('adminCreateAccount/', views.adminCreateAccount_view, name='adminCreateAccount'),
    path('logout/', views.logout_view, name='logout'),  # Logout URL
    path('adminPurchaseOrder/', views.admin_purchase_order, name='adminPurchaseOrder'),
    path('adminRequisitionProduct/', views.admin_requisition_product, name='adminRequisitionProduct'),
    path('adminProductListing/', views.admin_product_listing, name='adminProductListing'),
    path('inventory/inventoryStocks/', views.inventoryStocks_view, name='inventoryStocks'),

]

