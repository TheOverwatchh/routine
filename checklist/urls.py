from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('checklist', views.checklist, name="checklist"),
    path('reminder/<int:unique>', views.reminder, name="reminder"),
    path('deleteReminder/<int:unique>', views.deleteReminder, name="deleteReminder"),
    path('createReminder', views.createReminder, name="createReminder"),
    path('createTask', views.createTask, name="createTask"),
    path('deleteTask', views.deleteTask, name="deleteTask"),
    path('toggleTask/<int:unique>', views.toggleTask, name="toggleTask"),
    path('goals', views.goals, name="goals"),
    path('goals/newGoal', views.newGoal, name="newGoal"),
    path('goals/<int:unique>', views.goalPage, name='goalPage'),
    path('goals/addMiniGoal', views.addMiniGoal, name='addMiniGoal'),
    path('goals/toggleMiniGoal/<int:unique>', views.toggleMiniGoal, name='toggleMiniGoal'),
    path('goals/deleteMiniGoal/<int:unique>', views.deleteMiniGoal, name='deleteMiniGoal'),
    path('goals/deleteGoal/<int:unique>', views.deleteGoal, name='deleteGoal'),
    path('profile/<int:unique>', views.profile, name='profile'),
    path('completeGoal/<int:unique>', views.completeGoal, name='completeGoal')

]
