from django.shortcuts import redirect, render
from .models import Project
from .forms import Project, ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# =================================
# Projects List View
# =================================
def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects, paginator = paginateProjects(request, projects, 6)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


# =================================
# Single Project View
# =================================
def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.user = request.user.profile
        review.save()

        project.getVoteCount
        return redirect('project', pk=project.id)

    context = {
        'project': project,
        'form': form
    }
    return render(request, 'projects/single-project.html', context)


# =================================
# Create Project View
# =================================
@login_required(login_url='/login')
def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profile
            project.save()
        form.save_m2m()
        return redirect('projects')
    context = {
        'form': form
    }
    return render(request, 'projects/project-form.html', context)


# =================================
# Edit Project View
# =================================
@login_required(login_url='/login')
def editProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form
    }
    return render(request, 'projects/project-form.html', context)


# =================================
# Delete Project View
# =================================
@login_required(login_url='/login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {
        'object': project
    }
    return render(request, 'delete.html', context)
