from django import urls
from django.contrib import admin
from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.urls import reverse
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, message
from django.shortcuts import render, redirect, render_to_response 

from django.urls import path
from django.contrib.messages import add_message
from django.http import HttpResponseRedirect
from django.views import View
from django.utils.html import format_html

# token_generator = AppTokenGenerator





# Register your models here.
from .models import *
# from .views import clientDetails, send_mail

from accounts.views import Parent
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from .models import Parent,Child


 
# class AppTokenGenerator(PasswordResetTokenGenerator):
#     # company = Company()
#     def _make_hash_value(self, customer, timestamp):
#         # company = Company()

#         return (
#             six.text_type(customer.pk) + six.text_type(timestamp) +
#             six.text_type(customer.is_shortlisted)
#         )

# token_generator = AppTokenGenerator()

# class CustomerAdmin(admin.ModelAdmin):
# 	list_display = ['user','email','account_actions','is_shortlisted','referals','refered_by','companys_added','client_websites']
# 	search_fields = ['user','email','account_actions','is_shortlisted','companys_added','client_websites']
# 	# list_display_links = ['companys_added','user']
# 	# list_select_related = ['user']
# 	actions = ['is_shortlisted','mail_send_false','update_default']

# 	def is_shortlisted_false(self,request,queryset):
# 		queryset.update(is_shortlisted = False)
# 	is_shortlisted_false.short_description = 'Set short list to false'
# 	def mail_send_false(self,request,queryset):
# 		queryset.update(is_mail_send = False)
# 	mail_send_false.short_description = 'Set is mail send to false'

# 	def update_default(self,request,queryset):
# 		queryset.update(is_mail_send = False,is_shortlisted = False,is_waiting = False)
# 	update_default.short_description = 'Set selected customers to default'


	
# 	def is_shortlisted(self,request,queryset):
# 		# token_generator = accounts.tokens.AppTokenGenerator()
# 		for customer in queryset:
# 			# messages.info(request,"Sending Mail Please wait..")
# 		# company = Customer()
# 		# user = request.user
# 		# customer = Customer
# 		# customer = Customer.objects.get(id=pk)
# 		# customer = Customer.objects.get(id=pk)
# 			uidb64 = urlsafe_base64_encode(force_bytes(customer.pk))
# 			domain = get_current_site(request).domain
# 			link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(customer)})
# 			activate_url = 'http://'+domain+link
# 			# return HttpResponse('done')
# 			email_subject = "Congratulation you are shortlisted."
# 			email_body = "Please confirm your seat by clicking this link.\n" + activate_url

# 			email = EmailMessage(
# 				email_subject,
# 				email_body,
# 				'samarth.mailme@gmail.com',
# 				[customer.email,'samarth.mailme@gmail.com'],
			
# 			)
# 			email.send(fail_silently=False)
# 			customer.is_mail_send = True
# 			customer.is_waiting = True
# 			customer.save()

# 		# message_user.success(request,f"Email Sent successfully to {customer}".format(customer))
# 			self.message_user(request, f'Email Sent Successfully to {customer}'.format(customer))
# 		return HttpResponseRedirect("/admin")



	
# 	def account_actions(self, obj):
# 			if obj.is_shortlisted == False and obj.is_waiting==False:
# 				return format_html(
# 				'<button><a class="button" style="color:black" href="{}">ShortList</a></button>'
# 				,
# 				reverse('send_mail', args=[obj.pk]),
            
#         		)
# 			elif obj.is_shortlisted == True and obj.is_waiting == False:
# 				return format_html(
# 				'<b>Short listed</b>'
#         		)
# 			elif  obj.is_waiting == True:
# 				return format_html(
# 				'<p>Waiting for Confirmation..</p>'
#         		)






# 				# messages.success(request) 
			
# 			# print("done with shortlist")
# 			# return redirect('home')
# 		# return HttpResponse('../')

# 			# queryset.update(is_shortlisted = True)
# 	is_shortlisted.short_description = "Short list selected users"
# 	def companys_added(self,obj):
		
# 		return ", ".join([order.company_name for order in obj.order_set.all()])
	
# 	def client_websites(self,obj):
		
# 		return ", ".join([client.client_website_address for client in obj.client_set.all()])
	
	
# 	# def get_urls(self):

# 	# 	urls = super().get_urls()
#     #     custom_urls = [
# 	# 		url(
#     #         path('age/<int:age_count>/', self.update_age)
# 	# 		)
# 	# 	]
		
# 		return custom_urls + urls

# class VerificationView(View):
# 		def get(self,request,uidb64,token):
			
# 			try:
# 				id = force_text(urlsafe_base64_decode(uidb64))
# 				print(request.session.get_expiry_date())
# 				customer = Customer.objects.get(pk = id)
# 				if not token_generator.check_token(customer,token):
# 					return HttpResponseRedirect("../")
# 				if customer.is_shortlisted:
# 					return HttpResponseRedirect("../")
# 				customer.is_shortlisted = True
# 				customer.is_waiting = False
# 				customer.save()
				
# 				return redirect('login')

# 			except Exception as ex:
# 				pass
# 			return HttpResponseRedirect("../")










		

# class OrderAdmin(admin.ModelAdmin):
# 	search_fields = ['customer__user__username','country','company_name','address','adhar_card_number','mobile_number','website_address','date_of_birth','state']
# 	list_display = ['customer','company_name','address','adhar_card_number','mobile_number','website_address','date_of_birth','state','country']
	
    # list_editable = ['is_mail_send','is_shortlisted']
	
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user','email','is_shortlisted']
# class ClientAdmin(admin.ModelAdmin):
# 	search_fields = ['customer__user__username','client_website_address']
# 	list_display = ['customer','client_website_address']
import datetime
def save_vaccines(modeladmin, request, queryset):
    for object in queryset:
        object.save()
def update_child_age(modeladmin, request, queryset):
    for object in queryset:
        object.save()
    # queryset.update(Added_on = datetime.date.today())

class VaccineAdmin(admin.ModelAdmin):
    actions = [save_vaccines]

class ChildAdmin(admin.ModelAdmin):
    actions = [update_child_age]


from .models import Vaccine
admin.site.register(Parent)
admin.site.register(Child,ChildAdmin)
admin.site.register(Vaccine,VaccineAdmin)
# admin header and title modification
admin.site.site_header = "Admin DashBoard"
admin.site.site_title = "Child Vaccine Management"
admin.site.index_title = ''

# from django.contrib import admin
# from django.template.defaultfilters import escape
# from django.urls import reverse
# from .models import ScheduledReport, ReportRecipient, ScheduledReportGroup
# from .forms import ScheduledReportForm
# class ReportRecipientAdmin(admin.TabularInline):
#     model = ReportRecipient
# class ScheduledReportAdmin(admin.ModelAdmin):
#     """
#         List display for Scheduled reports in Django admin
#     """
#     model = ScheduledReport
#     list_display = ('id', 'get_recipients')
#     inlines = [
#         ReportRecipientAdmin
#     ]
#     form = ScheduledReportForm
#     def get_recipients(self, model):
#         recipients = model.reportrecep.all().values_list('email', flat=True)
#         if not recipients:
#             return 'No recipients added'
#         recipient_list = ''
#         for recipient in recipients:
#             recipient_list = recipient_list + recipient + ', '
#         return recipient_list[:-2]
#     get_recipients.short_description = 'Recipients'
#     get_recipients.allow_tags = True
# class ScheduledReportGroupAdmin(admin.ModelAdmin):
#     """
#         List display for ScheduledReportGroup Admin
#     """
#     model = ScheduledReportGroup
#     list_display = ('get_scheduled_report_name','get_report_name')
#     def get_scheduled_report_name(self, model):
#         return model.scheduled_report.subject
#     def get_report_name(self, model):
#         return model.report.name
#     get_scheduled_report_name.short_description = "Scheduled Report Name"
#     get_report_name.short_description = "Report Name"
#     show_change_link = True
#     get_report_name.allow_tags = True
# admin.site.register(ScheduledReport, ScheduledReportAdmin)
# admin.site.register(ScheduledReportGroup, ScheduledReportGroupAdmin)
