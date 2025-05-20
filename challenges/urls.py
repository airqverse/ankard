from django.urls import path
from . import views

# Paths defined here would be read in ordinally.
urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),

    # The word "month" in "<month>" has to be correspondent to
    # the argument name in views.monthly_challenge function.
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
