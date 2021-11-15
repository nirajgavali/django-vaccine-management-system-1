from celery import shared_task
from time import sleep
from django.contrib import messages
from django.core.mail import EmailMessage, message
from .models import Parent
@shared_task
def sleepy(duration):
    sleep(duration)
    return None

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@shared_task
def send_mail(request,pk,duration):
		sleep(duration)
		# messages.info(request,"Sending Mail Please wait..")
		# company = Customer()
		
		user = request.user
		# customer = Customer
		customer = Parent.objects.get(id=pk)
		# orders = customer.order_set.all()
		# order_count = orders.count()
		# if order_count == 0:
		# 	print("in count")
		# 	messages.error(request,"No companies added by customer so cant shortlist",extra_tags="alert alert-danger")
		# 	print("messa passed")
		# 	return HttpResponseRedirect(reverse('home'))
		# customer = Customer.objects.get(id=pk)
		# uidb64 = urlsafe_base64_encode(force_bytes(customer.pk))
		# domain = get_current_site(request).domain
		# link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(customer)})
		# activate_url = 'http://'+domain+link
		# return HttpResponse('done')
		email_subject = "Congratulation you are shortlisted."
		email_body = "Please confirm your seat by clicking this link.\n"
		
		email = EmailMessage(
			email_subject,
			email_body,
			'samarth.mailme@gmail.com',
			[customer.email,'samarth.mailme@gmail.com'],
		
		)
		email.send(fail_silently=False)
		customer.is_mail_send = True
		customer.is_waiting = True
		customer.save()
		
		messages.success(request,f"Email Sent successfully to {customer}".format(customer),extra_tags="alert alert-success")
		# return redirect('admin')
		return None

# from celery.task.schedules import crontab
from celery.schedules import crontab
from celery.decorators import periodic_task
# from celery.decorators import periodic_task
# from .email_service import send_emails
# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
# @periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
# def trigger_emails():
#     send_emails()


