
# Create your views here.

from django.conf.urls import url
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect, render_to_response 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .tasks import sleepy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
# Create your views here.
from .models import *
from .forms import *
# from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.views import View

# from .tokens import AppTokenGenerator,token_generator


@unauthenticated_user
def registerPage(request):
	user = request.user
	# parent_id = request.session.get('ref_profile')
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			print("for calid")
			if user is not None:
				# recommended_by_profile = Customer.objects.get(id = customer_id)
				user = form.save()
				user = User.objects.get(id = user.id)
				# registered_Customer = Customer.objects.get(user = registered_user)
				# registered_Customer.refered_by = recommended_by_profile.user
				# registered_Customer.save()
				username = form.cleaned_data.get('username')
				group = Group.objects.get(name='customer')
				user.groups.add(group)
				print("parent added to customer")
				create_parent = Parent(user = user,email = user.email)
				create_parent.save()
				print("parent created")
                    # customer_group.customer.add(user)
            # user.groups.add(group)


				messages.success(request, 'Account was created for ' + username)

				return redirect('login')
			else:
				redirect('register')

				# print(user)
				
				# print(user.email)

			
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)





# @unauthenticated_user
# def registerPage2(request,code):
# 	code = str(code)
# 	customer_refered = Customer.objects.get(code = code)
# 	if customer_refered.is_token_valid == False:
# 		return HttpResponse("This Link is no longer valid.. and already used")
# 	# customer_id = request.session.get('ref_profile')
	

# 	print('refcode = ',code)
# 	form = CreateUserForm()
# 	print("in register2")
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			print(user)
# 			username = form.cleaned_data.get('username')
# 			print(user.email)
# 			group = Group.objects.get(name='customer')
# 			user.groups.add(group)
# 			customer_refered = Customer.objects.get(code = code)
# 			customer_refered.is_token_valid = False
# 			create_customer = Customer(user = user,email = user.email,refered_by = customer_refered.user.username )
# 			create_customer.save()
# 			customer_refered.referals +=1
# 			customer_refered.save()
	
# 			print("customer created")
#                     # customer_group.customer.add(user)
#             # user.groups.add(group)


# 			messages.success(request, 'Account was created for ' + username)

# 			return redirect('login')
		

	# context = {'form':form}
	# return render(request, 'accounts/register.html', context)



@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
	childs = Child.objects.all()
	parents = Parent.objects.all()
	
	
	total_customers = parents.count()

	total_orders = childs.count()
	# total_shortlisted = customers.filter(is_shortlisted = True).count()
	# waiting_count = customers.filter(is_waiting = True).count()
	# delivered = orders.filter(status='Delivered').count()
	# pending = orders.filter(status='Pending').count()
	# customer = Customer.objects.get(id=pk)
	# orders = customer.order_set.all()
	# order_count = orders.count()

	context = {'orders':childs, 'customers':parents,
				'total_customers':total_customers,'total_orders':total_orders
	 }

	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request,pk):
	# declaring variables to NA
	grand_next_vaccine_date = grand_next_vaccine = grand_next_child = total_orders = "NA"
	vaccines = Vaccine.objects.all()

	# sleepy.delay(10)
	parent = Parent.objects.get(id = pk)
	# token=token_generator.make_token(customer)
	orders = parent.child_set.all()
	print(orders)
	days_left_for_next_min=10000
	for child in orders:
		d1 = date.today()

		childBirthDate = child.date_of_birth
		delta = d1-childBirthDate
		print("days= ",delta.days)
		child.child_age_in_days = delta.days
		child.save()

		grand_dict=[]
		for vaccine in vaccines:
			if vaccine.to_be_taken_age_in_days:
				if vaccine.to_be_taken_age_in_days>=child.child_age_in_days:
					days_left_for_next = vaccine.to_be_taken_age_in_days -  child.child_age_in_days
					next_date = date.today()+ timedelta(days=days_left_for_next)
					print("next_date = ",next_date)
					vaccine.next_date = next_date
					vaccine.save()
					if days_left_for_next >0:
						if min(days_left_for_next_min,days_left_for_next) == days_left_for_next:
						
							days_left_for_next_min = min(days_left_for_next_min,days_left_for_next)
							 
							grand_next_vaccine = vaccine.vaccine_name
							grand_next_child = child.child_name
							date.today()+ timedelta(days=days_left_for_next)
							grand_next_vaccine_date = date.today()+ timedelta(days=days_left_for_next_min) 

					
	
	

	# customer = Customer.objects.get(id=pk)
	total_orders = orders.count()
	# delivered = orders.filter(status='Delivered').count()
	# pending = orders.filter(status='Pending').count()

	# print('ORDERS:', orders)

	context = {'orders':orders,'grand_next_vaccine_date':grand_next_vaccine_date,'grand_next_vaccine':grand_next_vaccine,'grand_next_child':grand_next_child,'total_orders':total_orders,'customer':parent, 'vaccines':vaccines,
	}
	return render(request, 'accounts/user.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
# def accountSettings(request):
# 	customer = request.user.customer
# 	form = CustomerForm(instance=customer)

# 	if request.method == 'POST':
# 		form = CustomerForm(request.POST, request.FILES,instance=customer)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')


# 	context = {'form':form}
# 	return render(request, 'accounts/account_settings.html', context)
from django.http import HttpResponseRedirect
# token_generator = accounts.tokens.AppTokenGenerator()
from accounts.views import Parent
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from .models import *
 
# class AppTokenGenerator(PasswordResetTokenGenerator):
#     # company = Company()
#     def _make_hash_value(self, customer, timestamp):
#         # company = Company()
# 		# print(timestamp)

#         return (
#             six.text_type(customer.pk) + six.text_type(timestamp) +
#             six.text_type(customer.is_shortlisted)
#         )

# token_generator = AppTokenGenerator()



# # @login_required(login_url='login')
# # @allowed_users(allowed_roles=['admin'])
# # def products(request):
# # 	products = Product.objects.all()

# # 	return render(request, 'accounts/products.html', {'products':products})
from datetime import date,timedelta
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def customer(request, pk_test):
	child = Child.objects.get(id=pk_test)
	d1 = date.today()

	childBirthDate = child.date_of_birth
	delta = d1-childBirthDate
	print("days= ",delta.days)
	child.child_age_in_days = delta.days
	child.save()

	print(child.child_age_in_days)
	# Vaccine.objects.order_by('to_be_taken_age_in_days')
	vaccines = Vaccine.objects.order_by('to_be_taken_age_in_days')
	
	pending_vaccines=[]
	for vaccine in vaccines:
		if vaccine.to_be_taken_age_in_days:
			if vaccine.to_be_taken_age_in_days>=child.child_age_in_days:
				days_left_for_next = vaccine.to_be_taken_age_in_days -  child.child_age_in_days
				if days_left_for_next >0:
					next_date = date.today()+ timedelta(days=days_left_for_next)
					print("next_date = ",next_date)
					vaccine.next_date = next_date
					vaccine.save()

					pending_vaccines.append(vaccine)
		else:
			print(vaccine)
	
	
	total_vaccine = vaccines.count()
	print(total_vaccine)
	days_left_for_next = "All Done :)"
	next_date1 = "All Done :)"
	if len(pending_vaccines)!=0:
		days_left_for_next = pending_vaccines[0].to_be_taken_age_in_days -  child.child_age_in_days
		next_date1 = date.today()+ timedelta(days=days_left_for_next)
		next_vaccine = pending_vaccines[0]
	else:
		next_vaccine = "All Done :)"
	list_vaccine_pending = []
	
	total_vaccine_pending = len(pending_vaccines)
	context = {'child':child,'vaccines':vaccines,'next_vaccine':next_vaccine,'days_left_for_next':days_left_for_next,'next_date1':next_date1,'total_vaccine_pending':total_vaccine_pending,'list_vaccine_pending':list_vaccine_pending,'total_vaccine':total_vaccine,'pending_vaccines':pending_vaccines,
	}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
	customer = Parent.objects.get(id=pk)
	# customer = request.user
	form = ChildForm(initial={'customer':customer})
	
	# formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ChildForm(request.POST)
		

		# formset = OrderFormSet(request.POST, instance=customer)
		if form.is_valid():
			# print("form is valid")
			order = form.save(commit=False)
			order.parent = customer
			order.save()
            
			form.save()
			messages.success(request,"Child Added Successfully",extra_tags="alert alert-success")
			return redirect('/')
		else:
			print("form not vlais")

	context = {'form':form,'customer':customer}
	return render(request, 'accounts/company_form.html', context)



# edit child
@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def edit_child(request,pk):
	child = Child.objects.get(id=pk)
	# customer = request.user
	form = ChildForm(instance=child)
	
	# formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ChildForm(request.POST,instance=child)
		

		# formset = OrderFormSet(request.POST, instance=customer)
		if form.is_valid():
			# print("form is valid")
			
            
			form.save()
			messages.success(request,"Child Updated Successfully",extra_tags="alert alert-success")
			return redirect('/')
		else:
			print("form not vlais")

	context = {'form':form,'customer':child}
	return render(request, 'accounts/edit_child.html', context)

# Delete child
@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def delete_child(request,pk):
	child = Child.objects.get(id=pk)
	child.delete()
	
		
            
	
	messages.success(request,"Child Deleted Successfully",extra_tags="alert alert-danger")
	return redirect('/')
		

	


# mail_reminder
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def mail_reminder(request):
	childs = Child.objects.all()
	d1 = date.today()
	for child in childs:
		childBirthDate = child.date_of_birth
		delta = d1-childBirthDate
		print("days= ",delta.days)
		child.child_age_in_days = delta.days
		child.save()
		childBirthDate = child.date_of_birth
		vaccines = Vaccine.objects.order_by('to_be_taken_age_in_days')
		email_sent_list_vaccines = []
		email_sent_list=[]
		for vaccine in vaccines:
			if vaccine.to_be_taken_age_in_days:
				
				if vaccine.to_be_taken_age_in_days>=child.child_age_in_days:
					k=vaccine.to_be_taken_age_in_days - child.child_age_in_days
					if k<=5:
						send_mail(
								f'{k} days left for {child.child_name} next vaccine',
								f'After {k} days {child.child_name} is to be vaccinted by {vaccine.vaccine_name}.\n Thanks for choosing our servive :)',
								'samarth.mailme@gmail.com',
								[child.parent.email],
								fail_silently=False,
							)
						email_sent_list_vaccines.append({vaccine.vaccine_name})
						email_sent_list.append(child)




	

	context = {'email_sent_list':email_sent_list,'email_sent_list_vaccines':email_sent_list_vaccines}
	return render(request, 'accounts/mail_sent.html', context)


