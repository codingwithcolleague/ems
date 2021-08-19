
from django.urls import path
from poll.views import index,details,poll


urlpatterns = [
    path('' , index , name="home" ),
    path('details/<int:id>' , details , name="details" ),
    path('<int:id>/' , poll , name="poll" )

    
]
