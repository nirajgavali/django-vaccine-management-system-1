# from accounts.views import Customer
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six
# from .models import Customer
 
# class AppTokenGenerator(PasswordResetTokenGenerator):
#     # company = Company()
#     def _make_hash_value(self, customer, timestamp):
#         # company = Company()

#         return (
#             six.text_type(customer.pk) + six.text_type(timestamp) +
#             six.text_type(customer.is_shortlisted)
#         )

# token_generator = AppTokenGenerator()