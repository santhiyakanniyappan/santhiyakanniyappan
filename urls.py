from django.urls import path
from .views import TodoItemCreateView, TodoItemListView, TodoItemDetailView, TodoItemUpdateView, TodoItemDeleteView

urlpatterns = [
   path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),
]
