from django.urls import path
from . import views

# Paths defined here would be read in ordinally.
urlpatterns = [
    # path for https://ankard.jp/challenges/
    path("", views.index, name="index"),
    # The word "month" in "<month>" has to be correspondent to
    # the argument name in views.monthly_challenge function.
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
