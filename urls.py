from django.urls import path, include

urlpatterns = [
    path('data/', include('etl.urls')),
    path('models/', include('mlmodels.urls')),
]
