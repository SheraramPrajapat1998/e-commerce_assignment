from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import OrderCreateForm
from .mail import order_created
from .models import Order, OrderItem

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def order_create(request):
  cart = Cart(request)
  if request.method == 'POST':
    form = OrderCreateForm(data=request.POST)
    if form.is_valid():
      form.instance.user = request.user
      order = form.save()
      for item in cart:
        OrderItem.objects.create(order=order,
                                 product=item['product'],
                                 price=item['price'],
                                 quantity=item['quantity'])

      # clear the cart
      cart.clear()
      # send mail
      order_created(order.id)
      return render(request, 'orders/order/created.html', {'order': order})
  else:
    form = OrderCreateForm()
  return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
  order = get_object_or_404(Order, id=order_id)
  return render(request, 'admin/orders/order/detail.html', {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
  order = get_object_or_404(Order, id=order_id)
  html = render_to_string('orders/order/pdf.html', {'order': order})
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
  weasyprint.HTML(string=html).write_pdf(response,
                                          stylesheets=[weasyprint.CSS(
                                              settings.STATIC_ROOT + '/css/pdf.css')])
  return response

@login_required
def myorders(request):
  orders = Order.objects.filter(user=request.user)
  print(orders)
  return render(request, 'orders/order/myorders.html', {'orders':orders})