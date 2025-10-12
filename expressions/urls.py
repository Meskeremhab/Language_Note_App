from django.urls import path
from .views import ExpressionListCreate, ExpressionDetail

urlpatterns = [
    path('expressions/', ExpressionListCreate.as_view(), name='expression-list'),
    path('expressions/<int:pk>/', ExpressionDetail.as_view(), name='expression-detail'),
]
