from django.core.mail import send_mail
from django.conf import settings

from .models import Order

def order_created(order_id):
  """
  Send an e-mail notification when an order is
  successfully created.
  """
  order = Order.objects.get(id=order_id)
  subject = f'Order nr. {order.id}'
  message = f'Dear {order.first_name},\n\n You have successfully placed an order. Your order ID is {order.id}.'
  mail_sent = send_mail(subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [order.email])
  return mail_sent
