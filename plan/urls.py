from django.conf.urls import url
from .import views#当前目录下，引入views

urlpatterns = [
    url(r'^$',views.index),
    url(r"^plans/$",views.plans),
    url(r'students/$',views.students),
    url(r'^students/(\d+)$',views.studentsplan),
]