from django.urls import path
from . import views

urlpatterns = [
    path('addtask/',views.AddTask,name='addtask'),
    path('mark-as-done/<int:nk>',views.MarkAsDone,name='markasdone'),
    path('mark-as-undo/<int:pk>',views.MarkAsUndo,name='markasundo'),
    path('mark-edit/<int:pk>',views.MarkEdit,name='edit'),
    path('mark-delete/<int:pk>',views.Delete,name='markdelete')
]
