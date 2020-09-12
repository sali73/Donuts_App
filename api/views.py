from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import Product , Cart
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from .forms import ProductForm
from django.urls import reverse


# Create your views here.
def Index(request):
    product = [*Product.objects.all()]
    print(Product)
    return render(request,'product/Index.html' , {"Product": product})

def Home(request):
    return render(request,'product/Home.html')

def AddDonuts(request):
    return  render (request,"product/Add_Donuts.html")


# index views
# ---------------
def add_donuts_form_submission(request):
    print('hello form is submitted')
    title = request.POST['title']
    price = request.POST['price']
    sale_price = request.POST['sale_price']
    image = request.POST['image']
    slug = request.POST['slug']
    description = request.POST['description']
    product = Product(title=title,price=price,sale_price=sale_price,image=image,slug=slug,description=description)
    product.save()
    return render(request,"product/Add_Donuts.html")

# create a view
# --------------------
def detail_view(request, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "product/detail_view.html", context)

# update products
# ____________________
def update_view(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "product/update_view.html", context)


# delete view for details
# ______________________________
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
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
                messages.info(request, f"You are now logged in as {username}")
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
    cart=Cart.objects.all()[0]
    context={"cart":cart}
    template = "cart/view.html"
    return render(request, template,context)

def update_cart(request, slug):
    cart=Cart.objects.all()[0]
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

    cart.totle = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart"))


# def remove_from_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.remove(product)
#
# def get_cart(request):
#     return render(request, 'cart.html', {'cart': Cart(request)})