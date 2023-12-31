from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
import requests

from .urls_api import URLS_API
from .models import Faq, Gym, GymMembership, News, Review, Schedule, GroupClass
from .forms import GymMembershipForm, GroupClassForm, ReviewForm
from cart.forms import AddGroupClassForm
from login.models import Client

def gym_list(request):
    gym_list = Gym.objects.all()

    return render(request, 'fitnessclub_core/gym_list.html', {'gym_list': gym_list})

def gym_detail(request, id):
    gym = get_object_or_404(Gym, id=id)
    group_class_list = gym.group_classes.all()

    return render(request, 'fitnessclub_core/gym_detail.html', {'gym': gym, 'group_class_list': group_class_list})

# def gym_membership_detail(request, id):
#     gym_membership = get_object_or_404(GymMembership, id=id)

#     return render(request, 'fitnessclub_core/gym_membership_detail.html', {'gym_membership': gym_membership})

# def create_gym_membership(request):
#     if not request.user.is_staff:
#         raise PermissionDenied("You are not allowed to access this page.")
    
#     form = GymMembershipForm()

#     if request.method == 'POST':
#         form = GymMembershipForm(request.POST)

#         if form.is_valid():
#             gym_membership = form.save()
#             return redirect('gym_membership_detail', id=gym_membership.id)

#     return render(request, 'fitnessclub_core/create_gym_membership.html', {'form': form})

def group_class_list(request, id):
    gym = get_object_or_404(Gym, id=id)
    group_class_list = gym.group_classes.all()

    return render(request, 'fitnessclub_core/group_class_list.html', {'group_class_list': group_class_list})

def group_class_detail(request, id):
    group_class = get_object_or_404(GroupClass, id=id)

    return render(request, 'fitnessclub_core/group_class_detail.html', {'group_class': group_class, 'add_to_cart_form': AddGroupClassForm()})

def create_group_class(request):
    if not request.user.is_staff:
        raise PermissionDenied("You are not allowed to access this page.")
    
    form = GroupClassForm()

    if request.method == 'POST':
        form = GroupClassForm(request.POST)

        if form.is_valid():
            group_class = form.save()
            return redirect('group_class_detail', id=group_class.id)
    
    return render(request, 'fitnessclub_core/create_group_class.html', {'form': form})

def edit_group_class(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    
    group_class = None
    try:
        group_class = get_object_or_404(GroupClass, id=id)
    except:
        return HttpResponseNotFound('<h1>Group class not found</h1>')

    if request.method == 'POST':
        form = GroupClassForm(request.POST, instance=group_class)
        if form.is_valid():
            form.save()
            return redirect(f'/group_class/{group_class.id}')
    else:
        form = GroupClassForm(instance=group_class)

    return render(request, 'fitnessclub_core/edit_group_class.html', {'form': form, 'group_class': group_class})

def delete_group_class(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    
    group_class = None
    try:
        group_class = get_object_or_404(GroupClass, id=id)
        group_class.delete()
        return redirect('/')
    except:
        return HttpResponseNotFound('<h1>Group class not found</h1>')
    
def fclub(request):
    latest_news = News.objects.latest('created_at')

    context = { 'latest_news': latest_news }

    return render(request, 'fitnessclub_core/fclub.html', context)

def about_us(request):
    return render(request, 'fitnessclub_core/about_us.html')

def promotions (request):
    return render(request, 'fitnessclub_core/promotions.html')

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'fitnessclub_core/news_list.html', {'news_list': news_list})

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'fitnessclub_core/news_detail.html', {'news': news})

def employee_list(request):
    employees = Client.objects.filter(is_staff=True)
    return render(request, 'fitnessclub_core/employee_list.html', {'employees': employees})

def privacy_policy(request):
    return render(request, 'fitnessclub_core/privacy_policy.html')

def vacancies(request):
    return render(request, 'fitnessclub_core/vacancies.html')

def faq(request):
    faq = Faq.objects.all()
    return render(request, 'fitnessclub_core/faq.html', {'faq': faq})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'fitnessclub_core/review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.save() 
            return redirect('fitnessclub_core/review_list') 
    else:
        form = ReviewForm()
    return render(request, 'fitnessclub_core/add_review.html', {'form': form})

def experimental_page(request):
    dog_response = requests.get(URLS_API['random_dog'])
    joke_response = requests.get(URLS_API['random_joke'])
    
    dog_img_url = ''
    if dog_response.status_code == 200:
        dog_img_url = dog_response.json()['message']

    joke = ''
    if joke_response.status_code == 200:
        joke = joke_response.json()['setup'] + ' ' + joke_response.json()['punchline']

    return render(request, 'fitnessclub_core/experimental_page.html', {'dog_img_url': dog_img_url, 'joke': joke})
