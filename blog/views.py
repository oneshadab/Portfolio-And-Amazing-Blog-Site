from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import UserBlogForm
from .models import Blog

# Create your views here.
def home(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-created_on')[:2] #Prothom 5 taah show korbe. And create korar time onujayi shajabe
    return render(request, "blog/home.html", {"blogs":blogs})

#Details view. blog_id parameter nichhe karon url e blog_id parameter disi jeita integer value nibe. 
def details(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, "blog/details.html", {"blog":blog} )


#Shob blog dekha jaabe eikhane descending order e
def all_blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-created_on')
    return render(request, "blog/all_blogs.html", {"blogs":blogs})

#Shob blog dekha jaabe eikhane ascending order e
def all_blogs_ascending(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('created_on')
    return render(request, "blog/all_blogs_ascending.html", {"blogs":blogs})


#User signup page

def signupUser(request):
    if request.method == "GET":
        return render(request, "blog/signupUser.html", {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]: #Post req hoile test korbe password duita milse kina

            try: #jodi mile jaay and username unique hoy then user saved hobe
                user = User.objects.create_user(request.POST["username"],password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect("blog:userhome")
                # return redirect(reverse('blog:userhome'))
                
            except IntegrityError: #jodi unique name na thaake tahole aabar notun kore choose korbe
                error = "That user name is already taken"
                return render(request, "blog/signupUser.html",{"form":UserCreationForm, "error": error})    
        else: #password match na korle
            error= "Your Password didn't match!!"
            return render(request, "blog/signupUser.html",{"form":UserCreationForm, "error": error})  

#User sign up sheshe jeikhaney jaabe

def userhome(request):
   return render(request, "blog/userhome.html")


#Logout er view
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect("blog:home")


#Login er view
def loginUser(request):
    if request.method == "GET":
        return render (request, "blog/loginUser.html",{ "form": AuthenticationForm()}) #jodi get hoy than login page ashbe with authentication form

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        # user = authenticate(request, username=request.POST["username"],password=request.POST['password'])
        user = authenticate(request, username = username, password = password)


        # if user is None:
        #     #jodi kono user na thaake then aabar login page e send korbe but with an error message
        #     return render (request, "blog/loginUser.html",{ "form": AuthenticationForm(),"error":"Username or password not found!!"}) 

        # else: #aar jodi mile jaay then login done and userhome e redirect korbe
        #     login(request,user)
        #     return redirect ('blog:userhome')
        if user is not None:
            login(request,user)
            return redirect ('blog:userhome')
            
            #return render (request, "blog/loginUser.html",{ "form": AuthenticationForm(),"error":"Username or password not found!!"}) 

        else:

            return render (request, "blog/loginUser.html",{ "form": AuthenticationForm(),"error":"Username or password not found!!"}) 
            


#Create Blogs Views

def createBlogs(request):
    if request.method == "GET":
        return render(request, "blog/createBlogs.html", {"form":UserBlogForm()})
    else:
        try:
            form = UserBlogForm(request.POST)
            newBlog = form.save(commit=False) #Not saving to the db yet
            newBlog.user = request.user
            newBlog.save() #now it's saved to the user.
            return redirect ("blog:currentBlogs")
        except ValueError:
            return render(request, "blog/createBlogs.html", {"form":UserBlogForm(),"error": "Bad Data"})

        

# gjsgfkjsgfjksgfkjsgf














#eigula test views. don't need to give much attention
def random(request):
    return render(request, "blog/random.html", {})

def again(request):
    return render(request, "blog/again.html", {})    