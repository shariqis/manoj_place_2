from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from accounts.models import Shop
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def home(request):
   
    return render(request,'accounts/home.html')


def UserSignUp(request):
    if request.method=="POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        uname= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pass')
        
        new_user = User.objects.create_user(username = uname, password = password)
        new_user.is_active  = True
        new_user.email      = email
        new_user.first_name = first_name
        new_user.last_name=last_name
        new_user.save()              
        return HttpResponse("<script>window.alert('Sucessfully  Registerd!');window.location.href='/UserSignUp/'</script>")
    return render(request,'accounts/UsersiginUp.html')




def ShopSignUp(request):
    if request.method=="POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        uname= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pass')
        
        new_user = User.objects.create_user(username = uname, password = password)
        new_user.is_active  = False
        new_user.is_staff  = True
        new_user.email      = email
        new_user.first_name = first_name
        new_user.last_name=last_name
        new_user.save()            
        
        shop_name= request.POST.get('shop_name')
        shop_reg_id= request.POST.get('shop_reg_id')
        
        
        
        new_shop=Shop(shop_name=shop_name,shop_reg_id=shop_reg_id,user=new_user)
        new_shop.save()
          
        return HttpResponse("<script>window.alert('Sucessfully  Registerd!');window.location.href='/ShopSignUp/'</script>")
    return render(request,'accounts/ShopsiginUp.html')


def SignIn(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ''
        return render(request,'accounts/SignIn.html',context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
      
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("adminhome")
            else:
                if user.is_staff == 0: # user
                    request.session["userid"]=user.id
                    
                    return redirect("userhome")
                elif user.is_staff == 1: # ration shop
                    if user.is_active==1:
                        shopid=Shop.objects.filter(user_id=user.id).values()
                        print('..............')
                        print(shopid[0]["id"])
                        request.session["shopid"]=shopid[0]["id"]
                        
                        return redirect("shop_home")
                    else:
                        print('................')
                        return HttpResponse("<script>window.alert('Not Yet Approved!');window.location.href='/SignIn/'</script>")
               
        else:
            context = {}
            context['error'] = 'Invalid User or Admin not approved'
            return render(request,'accounts/SignIn.html',context)
        
   
    return render(request,'accounts/SignIn.html')


def accounts_logout(request):
    logout(request)
    return redirect('SignIn')