from django.conf.urls import url
from main.views import page

urlpatterns = (
    url(r"(?P<slug>[\w./-]+)/$", page, name="page"),
)
