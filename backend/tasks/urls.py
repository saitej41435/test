from django.urls import path
from .views import taskUpdate, userList,userCreate,userUpdate,userTasks,taskCreate, taskDelete


urlpatterns = [
    path('users/',userList),
    path('user/update/<str:userId>',userUpdate),
    path('user/create',userCreate),
    path('user/<int:userId>/tasks',userTasks),
    path('task/create',taskCreate),
    path('task/update/<int:taskId>',taskUpdate),
    path('task/delete/<int:taskId>',taskDelete)
]