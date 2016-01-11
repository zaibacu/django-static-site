from django.conf.urls import url
from main.views import page, home

urlpatterns = (
    url(r"^(?P<slug>[\w-]+)([.]md)?$", page, name="page"),
    url(r"^$", home, name="home"),
)
