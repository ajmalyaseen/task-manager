from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# 1. DASHBOARD
@login_required
def index(request):
    user = request.user
    tasks = Task.objects.filter(user=user).order_by('-created')
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    total_tasks = tasks.count()
    completed_count = tasks.filter(status='Completed').count()
    in_progress_count = tasks.filter(status='In Progress').count()
    todo_count = tasks.filter(status='To Do').count()

    filter_type = request.GET.get('filter')

    if filter_type == 'completed':
        tasks = tasks.filter(status='Completed')
    elif filter_type == 'inprogress':
        tasks = tasks.filter(status='In Progress')
    elif filter_type == 'todo':
        tasks = tasks.filter(status='To Do')
    elif filter_type == 'total':
        pass
    else:
        if not search_query:
            tasks = tasks.exclude(status='Completed')

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_count': completed_count,
        'in_progress_count': in_progress_count,
        'todo_count': todo_count,
        'current_filter': filter_type,
    }
    return render(request, 'index.html', context)

# 2. ADD TASK
@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                status=status,
                priority=priority,
                due_date=due_date if due_date else None
            )
            return redirect('index')

    return render(request, 'add_task.html')


# 3. EDIT TASK 
@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')

        date = request.POST.get('due_date')
        if date:
            task.due_date = date

        task.save()
        return redirect('index')

    return render(request, 'add_task.html', {'task': task})


# 4. DELETE TASK 
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')


# 5. HISTORY
@login_required
def history(request):
    tasks = Task.objects.filter(user=request.user, status='Completed').order_by('-created')
    return render(request, 'history.html', {'tasks': tasks})


# 6. REGISTER
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.status = 'Completed' 
    task.save()
    return redirect('index') 


@login_required
def profile(request):
    from .models import Profile 
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image'):
            profile.image = request.FILES['image']
            profile.save()
            return redirect('profile')

    return render(request, 'profile.html', {'user': request.user})