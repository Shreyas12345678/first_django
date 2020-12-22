from django.shortcuts import render,HttpResponse,auth


def index(request):
    
    return render(request,'index.html')
    #return HttpResponse("this is django project")


def about(request):
    return render(request,'about.html')
    #return HttpResponse('this is about sec')  


def contact(request):
    return render (request,'contact.html')      


def login(request):
    if request.method== 'POST':
      login_user= request.POST['username']
      login_password = request.POST['password']
      
      user= auth.authenticate(username= login_user,password='login_password')

    else:
      return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

#def profile(request):
    #return render(request,'')        

# Create your views here.

