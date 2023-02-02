from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_dj, logout as logout_dj
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lembrete, Task, Goal, miniGoal
from datetime import date

# Create your views here.
def index(request):
    if request.user.is_authenticated:
       return redirect(reverse('checklist'))
    else:
        return render(request, 'checklist/index.html')


def checklist(request):
    if request.user.is_authenticated:
        t = Task.objects.filter(user=request.user).order_by('time')
        l = Lembrete.objects.filter(user=request.user)    
        return render(request, 'checklist/checklist.html', {
                    'lembretes': l,
                    'llen': len(l),
                    'tasks': t,
                    'tlen': len(t)
            })    
    else:
        return redirect(reverse('index'))        


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_dj(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, 'checklist/index.html', {
                'message': 'Username or Password incorrect'
            })

    else:
        return redirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']    
        email = request.POST['email']    
        password = request.POST['password'] 
        user = User.objects.create_user(username, email, password)
        user.save()
        if user:
            login_dj(request, user)
            return redirect(reverse('index'))
        else: 
            return render(request, 'checklist/index.html')      

def logout(request):
    logout_dj(request)
    return redirect('index')

def reminder(request, unique):
    l = Lembrete.objects.get(id=unique)
    print(l.title)
    return render(request, 'checklist/lembrete.html', {
        'lembrete': l
    })

def deleteReminder(request, unique):
    l = Lembrete.objects.get(id=unique)
    l.delete()
    return HttpResponse('DELETED')

def createReminder(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        l = Lembrete.objects.create(title=title, content=content, user=request.user)
        l.save()
        return redirect(reverse('index'))

def createTask(request):
    if request.method == 'POST':
        title = request.POST['title']
        time = request.POST['time']
        task = Task.objects.create(title=title, time=time, user=request.user)
        task.save()
        return render(request, 'checklist/checklist.html', {
            'tasks': Task.objects.filter(user=request.user).order_by('time'),
            'tlen': len(Task.objects.filter(user=request.user).order_by('time')),
            'lembretes': Lembrete.objects.filter(user=request.user),
            'llen': len(Lembrete.objects.filter(user=request.user)),
            'status': 'checklist',

        })

def deleteTask(request):
    if request.method == 'POST':
        task = Task.objects.get(id=request.POST['id'])
        task.delete()
        return render(request, 'checklist/checklist.html', {
            'tasks': Task.objects.filter(user=request.user).order_by('time'),
            'tlen': len(Task.objects.filter(user=request.user).order_by('time')),
            'lembretes': Lembrete.objects.filter(user=request.user),
            'llen': len(Lembrete.objects.filter(user=request.user)),
            'status': 'checklist',

        })

def toggleTask(request, unique):
    t = Task.objects.get(id=unique)
    if t.status == 'undone':
        t.status = 'done'
        t.save()
        return HttpResponse('marked to done')
    else: 
        t.status = 'undone'
        t.save()
        return HttpResponse('marked to undone')


def goals(request):
    if request.user.is_authenticated:
        g = Goal.objects.filter(user=request.user, status='undone').order_by('deadline')
        done = 0
        percentage = '0%'
        for i in g:
            # see if theres minigoals
            s = miniGoal.objects.filter(goal=i)
            #if true, how many? make the logic and calc the percentage
            if len(s) > 0:
                for x in s:
                    if x.status == 'done':
                        done = done + 1
                        print('opa, aqui não parça')
                        percentage = f'{round(100/len(s) * done)}% '
                        i.percentage = percentage
                        i.save()
                    else:
                        done = done

                if (100/len(s)) * done == 100.0:
                    print('falling here')
                    print(len(s))
                    print(done)
                    print(100/len(s)*done)
                    i.status = 'done'
                    i.save()
                else:
                    i.status = 'undone'
                    i.save()          
            # else: 
            #     percentage = '0%'    
        return render(request, 'checklist/goals.html', {
            'goals': g,
            'glen': len(g),
            # 'percentage': percentage
        })
    else:    
        return redirect(reverse('index'))

def newGoal(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        deadline = request.POST['deadline']
        l = Goal.objects.create(title=title, description=description, user=request.user, deadline=deadline)
        l.save()
        return redirect(reverse('goals'))
    else:
        return render(request, 'checklist/newGoal.html')

def goalPage(request, unique):
    g = Goal.objects.get(id=unique)
    m = miniGoal.objects.filter(goal=g).order_by('deadline')
    return render(request, 'checklist/goal.html', {
        'goal': g,
        'minigoals': m
    })

def addMiniGoal(request):
    if request.method == 'POST':
        goalid = request.POST['goal']
        goal = Goal.objects.get(id=goalid)
        user = request.user
        title = request.POST['title']
        description = request.POST['description']
        deadline = request.POST['deadline']
        status = 'undone'
        m = miniGoal(goal=goal, user=user, title=title, description=description, deadline=deadline, status=status)
        m.save()
        mini = miniGoal.objects.filter(goal=goal).order_by('deadline')
        return redirect('goals')
        # return render(request, 'checklist/goal.html', {
        #     'goal': goal,
        #     'minigoals': mini
        # })

def toggleMiniGoal(request, unique):
    mg = miniGoal.objects.get(id=unique)
    test = mg.goal.id
    if mg.status == 'undone':
        mg.status = 'done'
        mg.save()

        g = Goal.objects.filter(user=request.user).order_by('deadline')
        done = 0
        percentage = '0%'
        for i in g:
            # see if theres minigoals
            s = miniGoal.objects.filter(goal=i)
            #if true, how many? make the logic and calc the percentage
            if len(s) > 0:
                for x in s:
                    if x.status == 'done':
                        done = done + 1
                        percentage = f'{round(100/len(s) * done)}% '
                        i.percentage = percentage
                        i.deadline = date.today()
                        i.save()
                if 100/len(s) * done == 100.0:
                    i.status = 'done'
                    i.save()
                else:
                    i.status = 'undone'
                    i.save()   

        # goall = mg.goal 
        # minigoalss = miniGoal.objects.filter(goal=goall).order_by('deadline')
        # return render(request, 'checklist/goal.html', {
        #     'goal': goall,
        #     'minigoals': minigoalss
        # })
        return HttpResponse('done')
        # return redirect(reverse('goalPage'), args={'unique': test })
    else: 
        mg.status = 'undone'
        mg.save()
        g = Goal.objects.filter(user=request.user).order_by('deadline')
        done = 0
        percentage = '0%'
        for i in g:
            # see if theres minigoals
            s = miniGoal.objects.filter(goal=i)
            #if true, how many? make the logic and calc the percentage
            if len(s) > 0:
                for x in s:
                    if x.status == 'done':
                        done = done + 1
                        # percentage = f'{round(100/len(s) * done)}% '
                        # i.percentage = percentage
                        # i.save()
                    else:
                        done = done
                        # if done > 0:
                        #     done = done - 1
                        # else:
                        #     done = 0    
                        # percentage = f'{round(100/len(s) * done)}% '
                        # i.percentage = percentage
                        # i.save() 

                percentage = f'{round(100/len(s) * done)}% '
                i.percentage = percentage
                i.save()           
                if 100/len(s) * done == 100.0:
                    i.status = 'done'
                    i.save()
                else:
                    i.status = 'undone'
                    i.save()        

        # return HttpResponse('n')
        # goall = mg.goal 
        # minigoalss = miniGoal.objects.filter(goal=goall).order_by('deadline')
        # return render(request, 'checklist/goal.html', {
        #     'goal': goall,
        #     'minigoals': minigoalss
        # })
        return HttpResponse('undone')

        # return redirect(reverse('goalPage'), args={'unique': test })

        
def deleteMiniGoal(request, unique):
    g = miniGoal.objects.get(id=unique)
    g.delete()
    return redirect('goals')
    
def deleteGoal(request, unique):
    g = Goal.objects.get(id=unique)
    g.delete()
    return redirect('goals')

def completeGoal(request, unique):
        g = Goal.objects.get(id=unique)
        g.status = 'done'
        g.percentage == '100%'
        g.save()
        m = miniGoal.objects.filter(goal=g)
        for i in m:
            i.status = 'done'

        return redirect('goals')        

def profile(request, unique):
    u = User.objects.get(id=unique)
    g = Goal.objects.filter(user=u, status='done')
    return render(request, 'checklist/profile.html', {
        'user': u,
        'completedGoals': g
    })    