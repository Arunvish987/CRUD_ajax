from django.shortcuts import render
from .forms import UserForm
from .models import *
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    form = UserForm()
    obj = User.objects.all()

    return render(request, 'enroll/home.html', {'form':form, 'obj':obj})

# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            sid = request.POST['stuid']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            
            if sid == "":
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=sid, name=name, email=email, password=password) 
            usr.save()
            std = User.objects.values()
            # print(std)
            usr_data = list(std)

            return JsonResponse({'status':'Save', 'usr_data':usr_data})
        else:
            return JsonResponse({'status':0})

 #   delete data
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        #print(id)
        pi = User.objects.get(pk=id)
        pi.delete()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

# edit data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        #print(id)
        obj1 = User.objects.get(pk=id)
        obj1_data = {'id':obj1.id, 'name':obj1.name, 'email':obj1.email, 'password':obj1.password}

        return JsonResponse(obj1_data)




        


