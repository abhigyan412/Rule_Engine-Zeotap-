from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RuleViewSet , index

router = DefaultRouter()
router.register(r'rules', RuleViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),

    path('rules/evaluate/', RuleViewSet.as_view({'post': 'evaluate_rule'}), name='evaluate_rule'),
]
