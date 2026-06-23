from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Project, Task


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

        return redirect('home')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('home')

    return render(request, 'register.html')


@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    tasks = Task.objects.filter(project__owner=request.user).order_by('-created_at')

    total_projects = projects.count()
    active_projects = projects.filter(status='Active').count()
    completed_projects = projects.filter(status='Completed').count()
    on_hold_projects = projects.filter(status='On Hold').count()

    total_tasks = tasks.count()
    todo_tasks = tasks.filter(status='To Do').count()
    in_progress_tasks = tasks.filter(status='In Progress').count()
    done_tasks = tasks.filter(status='Done').count()

    completion_rate = int((done_tasks / total_tasks) * 100) if total_tasks else 0

    context = {
        'projects': projects,
        'total_projects': total_projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'on_hold_projects': on_hold_projects,
        'total_tasks': total_tasks,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
        'completion_rate': completion_rate,
    }

    return render(request, 'dashboard.html', context)


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    search = request.GET.get('search', '').strip()

    if search:
        projects = projects.filter(title__icontains=search)

    return render(
        request,
        'project_list.html',
        {'projects': projects, 'search': search}
    )


@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Project.objects.create(
            owner=request.user,
            title=title,
            description=description,
            status=status
        )

        return redirect('project_list')

    return render(request, 'create_project.html')


@login_required
def project_detail(request, id):
    project = Project.objects.get(id=id, owner=request.user)
    tasks = Task.objects.filter(project=project).order_by('-created_at')

    total_tasks = tasks.count()
    todo_tasks = tasks.filter(status='To Do').count()
    in_progress_tasks = tasks.filter(status='In Progress').count()
    done_tasks = tasks.filter(status='Done').count()
    completion_rate = int((done_tasks / total_tasks) * 100) if total_tasks else 0

    context = {
        'project': project,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
        'completion_rate': completion_rate,
    }

    return render(request, 'project_detail.html', context)


@login_required
def update_project(request, id):
    project = Project.objects.get(id=id, owner=request.user)

    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.status = request.POST.get('status')
        project.save()
        return redirect('project_detail', id=project.id)

    return render(request, 'update_project.html', {'project': project})


@login_required
def delete_project(request, id):
    project = Project.objects.get(id=id, owner=request.user)

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')

    return render(request, 'delete_project.html', {'project': project})


@login_required
def create_task(request, project_id):
    project = Project.objects.get(id=project_id, owner=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            project=project,
            title=title,
            status=status,
            priority=priority,
            due_date=due_date
        )

        return redirect('project_detail', id=project.id)

    return render(request, 'create_task.html', {'project': project})


@login_required
def update_task(request, id):
    task = Task.objects.get(id=id, project__owner=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('project_detail', id=task.project.id)

    return render(request, 'update_task.html', {'task': task})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, project__owner=request.user)
    project_id = task.project.id

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', id=project_id)

    return render(request, 'delete_task.html', {'task': task})


def logout_user(request):
    logout(request)
    return redirect('home')
