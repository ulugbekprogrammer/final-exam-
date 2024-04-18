from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import *

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Home(TemplateView):
    template_name = 'index.html'


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart')
    return render(request, 'product_detail.html', {'product': product})

def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'shop.html', {'cart_items': cart_items, 'total_price': total_price})

def delete_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.subtotal() for item in cart_items)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_price)
        order.items.set(cart_items)
        order.save()
        cart_items.delete()  # Clear the cart
        return redirect('order_success')
    return render(request, 'checkout.html', {'total_price': total_price})

def order_success(request):
    return render(request, 'order_success.html')


def detail(request):
    return render(request, 'details.html', context={})

def compare(request):
    return render(request, 'compare.html', context={})

def accounts(request):
    return render(request, 'accounts.html', context={})


