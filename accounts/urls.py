from django.urls import path
from . import views
from . import admin


urlpatterns = [
	path('register/', views.registerPage, name="register"),
    # path('register/<str:code>/', views.registerPage2, name="register2"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/<str:pk>/', views.userPage, name="user-page"),

    # path('account/', views.accountSettings, name="account"),

    # path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('edit_child/<str:pk>/', views.edit_child, name="edit_child"),
    path('delete_child/<str:pk>/', views.delete_child, name="delete_child"),
    path('send_mail_reminder/', views.mail_reminder, name="mail_reminder"),
    # path('activate/<uidb64>/<token>/', admin.VerificationView.as_view(), name="activate"),
    # path('copy_link/<str:code>/', views.copy_link, name="copy_link"),
    #  path('activate2/<uidb64>/<token>/', views.VerificationView.as_view(), name="activate2"),

    path('add_child/<str:pk>/', views.createOrder, name="create_company"),
    
    # path('generate_link/<str:pk>/',views.generate_link2, name="generate_link2"),
    # path('<str:ref_code>/',views.generate_link2, name="generate_link2")
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]