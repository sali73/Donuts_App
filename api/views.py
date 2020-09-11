from django.shortcuts import render , redirect
from .models import Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.
def Index(request):
    product = [*Product.objects.all()]
    print(Product)
    return render(request,'product/Index.html' , {"Product": product})

def Home(request):
    return render(request,'product/Home.html')

def AddDonuts(request):
    return  render (request,"product/Add_Donuts.html")

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

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#                 username = form.cleaned_data.get("username")
#                 messages.success(request, f"Account created for'{username} !")
#                 login(request, username)
#                 messages.info(request, f"You Are Now Logged In As: {username}")
#                 return redirect("api:home")
#             else:
#                 for msg in form.error_messages:
#                     messages.error(request, f"{msg}:{form.error_messages[msg]}")
#     return render(request, 'users/register.html', {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("api:home")

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request,"users/login.html",{"form": form})


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