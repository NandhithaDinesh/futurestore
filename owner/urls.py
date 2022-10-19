from unicodedata import name
from django.urls import path
from owner import views
urlpatterns=[
    path("index",views.AdminDashBoardView.as_view(),name="dashboard"),
    path("orders/latest",views.OrderListView.as_view(),name="neworders"),
    path("orders/details/<int:id>",views.OrderDetailView.as_view(),name="order-details")
]