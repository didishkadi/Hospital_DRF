from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('account.urls')),
    path('meet/', include('timetable.urls')),
    path('docs/', include('docs.urls')),
]
