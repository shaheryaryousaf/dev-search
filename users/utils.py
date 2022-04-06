from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    developers = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(
            short_intro__icontains=search_query) | Q(skill__in=skills)
    ).order_by('created_at')
    return developers, search_query


def paginateUsers(request, developers, results):
    page = request.GET.get('page')
    paginator = Paginator(developers, results)

    try:
        developers = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        developers = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        developers = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, developers, paginator
