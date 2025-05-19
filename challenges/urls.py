from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),

    # The word "month" in "<month>" has to be correspondent to
    # the argument name in views.monthly_challenge function.
    path("<month>", views.monthly_challenge)
]
