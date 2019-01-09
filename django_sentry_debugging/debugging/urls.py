from django.conf.urls import url

from django_sentry_debugging.debugging import views

urlpatterns = [
    url(r'^works/', views.uploads_to_sentry),
    url(r'^broken/', views.no_body),
]
