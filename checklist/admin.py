from django.contrib import admin
from . models import User, Lembrete, Task, Goal, miniGoal
# Register your models here.
admin.site.register(Lembrete)
admin.site.register(Task)
admin.site.register(Goal)
admin.site.register(miniGoal)