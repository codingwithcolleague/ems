
from django.urls import path
from employee.views import employee_delete, employee_list, employee_details, employee_add, employee_edit


urlpatterns = [
    path('' , employee_list , name="list" ),
    path('<int:id>/' , employee_details , name="employee_detail" ),
    path('add/' , employee_add , name="employee_add" ),
    path('<int:id>/edit/' , employee_edit , name="employee_edit" ),
    path('<int:id>/delete/' , employee_delete , name="employee_delete" ),


   

]
