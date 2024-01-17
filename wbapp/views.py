from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from datetime import datetime

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def dashboard(request):
    user_name = request.user
    res_data = {"exist":False, "edit":False, "data":""}

    if request.method == 'POST':
        if 'create' in request.POST:
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            username = str(user_name)

            # Create a UserProfile instance
            user_profile = UserProfile.objects.create(
                username=username, 
                address=address, 
                phone=phone,
                email=email,
                created=datetime.now().date()
            )

            # Save the UserProfile instance to the database
            user_profile.save()
        
        elif 'delete' in request.POST:
            delete_id = request.POST['delete']
            # Retrieve the UserProfile instance based on the primary key
            user_profile = UserProfile.objects.get(pk=delete_id)
            # Delete the instance from the database
            user_profile.delete()
        else:
            pass

    
    try:
        user_profile = UserProfile.objects.get(username=user_name)
        res_data["data"] = user_profile
        res_data["exist"] = True
    except UserProfile.DoesNotExist:
        pass
    finally:
        return render(request, 'dashboard.html', res_data)
    

def user_profile(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    form = UserProfileForm(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        # return redirect('user_profile', user_id=user.id)
        return redirect('dashboard')

    return render(request, 'user_profile.html', {'form': form, 'user': user})