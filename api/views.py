from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import Product , Cart
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from .forms import ProductForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def Index(request):
    product = [*Product.objects.all()]
    print(Product)
    return render(request,'product/Index.html' , {"Product": product})

@login_required(login_url='login')
def Home(request):
    return render(request,'product/Home.html')

def AddDonuts(request):
    return  render (request,"product/Add_Donuts.html")


# add
# ---------------
def add_donuts_form_submission(request):
    print('hello form is submitted')
    title = request.POST['title']
    price = request.POST['price']
    image = request.POST['image']
    slug = request.POST['slug']
    description = request.POST['description']
    qty = request.POST['qty']
    product = Product(title=title,price=price,image=image,slug=slug,description=description,qty=qty)
    product.save()
    return render(request,"product/Add_Donuts.html")

def detail_view(request,id):
    print (id)
    products = Product.objects.get(id=id)
    context = {"data":products}
    template = "product/detail_view.html"
    return render(request,template , context)

# update products
# ____________________
def update_view(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/index/")
    context["form"] = form
    return render(request, "product/update_view.html", context)

# delete view for details
# ______________________________
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/index/")
    return render(request, "product/delete_view.html", context)

# user setup
# ---------------
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You Are Now Logged In As: {username}")
            return redirect("api:home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                  "users/register.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("api:home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome back {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name ="users/login.html",
                  context={"form":form})

# cart setup
# ________________
def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart=Cart.objects.get(id=the_id)
        context={"cart":cart}
    else:
        empty_message = ' Your Cart is Empty, Please Keep Shpping.'
        context={"empty":True, "empty_message": empty_message}
    template = "cart/view.html"
    return render(request, template,context)

def update_cart(request, slug):
    request.session.set_expiry(3000000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    new_total= 0.00
    for item in cart.products.all():
        new_total += float(item.price)

    request.session['items_total'] = cart.products.count()
    cart.totle = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart"))
