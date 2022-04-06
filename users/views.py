from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserCreationForm, editProfileForm, skillForm, messageForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles, paginateUsers
from django.core.mail import EmailMessage


# =================================
# Users List View
# =================================
def users(request):
    developers, search_query = searchProfiles(request)
    custom_range, developers, paginator = paginateUsers(request, developers, 6)
    context = {
        'developers': developers,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'users/profiles.html', context)


# =================================
# Profile Detail View
# =================================
def user(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
    }
    return render(request, 'users/single-profile.html', context)


# =================================
# Register User View
# =================================
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # to = email
            # message = f"Thanks for registering on DevSearch."
            # msg = EmailMessage(
            #     'Welcome to DevSearch',
            #     message,
            #     'msdeveloper1122@gmail.com',
            #     [to],
            # )
            # msg.content_subtype = "html"
            # msg.send()

            messages.success(
                request, f"Account has been created for {username}")
            return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


# =================================
# My Profile View
# =================================
@login_required(login_url='/login')
def myAccount(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'users/my-profile.html', context)


# =================================
# Update Profile View
# =================================
@login_required(login_url='/login')
def updateProfile(request):
    profile = request.user.profile
    form = editProfileForm(instance=profile)
    if request.method == "POST":
        form = editProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my-account')
    context = {
        'form': form
    }
    return render(request, 'users/update-profile.html', context)


# =================================
# Add Skill View
# =================================
@login_required(login_url='/login')
def addSkill(request):
    form = skillForm()
    if request.method == "POST":
        form = skillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user.profile
            skill.save()
            return redirect('my-account')
    context = {
        'form': form
    }
    return render(request, 'users/skill-form.html', context)


# =================================
# Edit Skill View
# =================================
@login_required(login_url='/login')
def editSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = skillForm(instance=skill)
    if request.method == "POST":
        form = skillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('my-account')
    context = {
        'form': form
    }
    return render(request, 'users/skill-form.html', context)


# =================================
# Delete Skill View
# =================================
@login_required(login_url='/login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        return redirect('my-account')
    context = {
        'object': skill
    }
    return render(request, 'delete.html', context)


# =================================
# User Inbox View
# =================================
@login_required(login_url='/login')
def inbox(request):
    profile = request.user.profile
    userMessages = profile.messages.all()
    unreadMessages = userMessages.filter(is_read=False).count()
    context = {
        'messages': userMessages,
        'unreadMessages': unreadMessages,
    }
    return render(request, 'messages/inbox.html', context)


# =================================
# Single Message View
# =================================
@login_required(login_url='/login')
def singleMessage(request, pk):
    profile = request.user.profile
    userMessage = profile.messages.get(id=pk)
    userMessage.is_read = True
    userMessage.save()
    context = {
        'message': userMessage,
    }
    return render(request, 'messages/message.html', context)


# =================================
# Create Message View
# =================================
def createMessage(request, pk):
    form = messageForm()

    recipient = Profile.objects.get(id=pk)

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email

            message.save()
            messages.success(request, "Your message has been sent")
            return redirect('single-user', pk=recipient.id)

    context = {
        'form': form
    }
    return render(request, 'messages/create-message.html', context)
