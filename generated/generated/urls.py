from django.urls import path, include
from rest_framework.routers import DefaultRouter
from @@@@@.views import *

router = DefaultRouter()

router.register(r'configs', ConfigsViewSet, basename='configs')
router.register(r'taskGroups', TaskgroupsViewSet, basename='taskGroups')
router.register(r'tasks', TasksViewSet, basename='tasks')
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'prompts', PromptsViewSet, basename='prompts')
router.register(r'requests', RequestsViewSet, basename='requests')

urlpatterns = [
    path('', include(router.urls)),
]
