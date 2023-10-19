from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

# import the built in User forms
from Project.Forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print("User Signup Successful!")
            print('Username:', user)
            print('Password:', user)
            print('User:', user)
            return redirect('signin')  # Replace 'success_page' with the appropriate URL or view name
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'Project/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('inputUserame')
        passw = request.POST.get('inputPassword')
        user = authenticate(request, username=uname, password=passw)
        
        if user:
            if user.is_active:
                if request.POST.get("chk", "NA") == "Remember Me":
                    response = render(request, "Project/userhome.html")
                    # create the cookie:
                    response.set_cookie("cookie_uname", uname, 3*60)
                    response.set_cookie("cookie_passw", passw, 3*60)
                    request.session['name'] = uname  # Set the 'name' session variable to the user's name
                    login(request, user)
                else:
                    request.session['name'] = uname  # Set the 'name' session variable to the user's name
                    login(request, user)
                    print("User is authenticated!")
                    return redirect('userhome')


            else:
                print('User is inactive')
            
        else:
            print('Invalid user credentials')
            user = authenticate(request, username=uname, password=passw)
    else:
        if request.COOKIES.get('cookie_uname' , 'NA') != 'NA':
            # cookie is already created
            # create an empty dictionary
            mydata = {}
            # retrieve cookie values and insert in the dictionary
            mydata['cookie_uname_value'] = request.COOKIES['cookie_key_uname']
            mydata['cookie_passw_value'] = request.COOKIES['cookie_key_pass']
            # display the form and send the dictionary with retrieved username and password
            return render(request, 'Project/signin.html' , mydata)
    
    return render(request, 'Project/signin.html')
    
@login_required(login_url='signin')
def userhome(request):
    print('You are ', request.session.get('name'))
    return render(request, 'Project/userhome.html')

def logoutUser(request):
    # Check if the 'name' session variable exists before attempting to delete it
    if 'name' in request.session:
        del request.session['name']

    # Flush the session
    request.session.flush()
    
    # Log the user out
    logout(request)
    
    # Redirect the user to the 'signin' page
    return redirect('signin')

