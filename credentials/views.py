from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


from .forms import DetailForm
from .models import Detail, Place


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'new.html')
        else:
            messages.info(request,"invalid credentials")
            return render(request,'login.html')
    return render(request,'login.html')
def register (request):
    if request.method == "POST":
        username = request.POST['USERNAME']
        email = request.POST['EMAIL']
        password = request.POST['PASSWORD']
        cpassword = request.POST['CONFIRM PASSWORD']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return render(request,'register.html')
            else:
                 user =User.objects.create_user(username=username,email=email,password=password)
                 user.save();
            return render(request,'login.html')

        else:
            messages.info(request,"incorrect password")
            return render(request,'register.html')
        return redirect('/')
    return render(request,'register.html')
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['USERNAME']
#         password = request.POST['PASSWORD']
#         c_password = request.POST['CONFIRM PASSWORD']
#         if password == c_password:
#
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username already exists")
#                 return render(request,'register.html')
#             else:
#                  user =User.objects.create_user(username=username,password=password)
#                  user.save();
#             return render(request,'login.html')
#
#         else:
#             messages.info(request,"incorrect password")
#             return render(request,'register.html')
#     return render(request,'register.html')

def detail(request):
    form = DetailForm()
    if request.method == 'POST':
        name=request.POST.get('name',)
        age = request.POST.get('age', )
        dob = request.POST.get('dob', )
        gender = request.POST.get('gender', )
        address = request.POST.get('address', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        district = request.POST.get('District', )
        place = request.POST.get('Place', )
        account_type = request.POST.get('account_type', )
        materials_required = request.POST.get('materials_required', )
        form = Detail(name=name,dob=dob,age=age,gender=gender,address=address,phone=phone,email=email,district=district,
                      place=place,account_type=account_type,materials_required=materials_required)
        form = DetailForm(request.POST or None, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            return render(request, 'card.html')


    return render(request, 'detail.html', {'form': form})

def card(request):
    return render(request,'card.html')



def new(request):
    details = Detail.objects.all()
    return render(request,'new.html',{'details':details})

def logout(request):
    messages.info(request, "Logged out successfully!")
    return render(request,'index.html')

def person_create_view(request):
    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'detail.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Detail, pk=pk)
    form = DetailForm(instance=detail)
    if request.method == 'POST':
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'detail.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    places = Place.objects.filter(district_id=district_id).all()
    return render(request, 'dropdown.html', {'places': places})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

























