from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *

class ConfigsViewSet(ViewSet):
  def list(self, request):
    # Get /configs
    data = 'something_scripts'
    return Response(data)

  def update(self, request):
    # Put /configs
    data = 'something_scripts'
    return Response(data)

class TaskgroupsViewSet(ViewSet):
  def list(self, request):
    # Get /taskGroups
    data = 'something_scripts'
    return Response(data)

  def create(self, request):
    # Post /taskGroups
    data = 'something_scripts'
    return Response(data)


  def partial_update(self, request):
    # Patch /taskGroups/{index}
    data = 'something_scripts'
    return Response(data)

  def destroy(self, request):
    # Delete /taskGroups/{index}
    data = 'something_scripts'
    return Response(data)

class TasksViewSet(ViewSet):
  def list(self, request):
    # Get /tasks
    data = 'something_scripts'
    return Response(data)

class PostsViewSet(ViewSet):
  def create(self, request):
    # Post /posts
    data = 'something_scripts'
    return Response(data)


  def partial_update(self, request):
    # Patch /posts/{id}
    data = 'something_scripts'
    return Response(data)

class PromptsViewSet(ViewSet):
  def create(self, request):
    # Post /prompts
    data = 'something_scripts'
    return Response(data)


  def partial_update(self, request):
    # Patch /prompts/{id}
    data = 'something_scripts'
    return Response(data)

class RequestsViewSet(ViewSet):
  def create(self, request):
    # Post /requests
    data = 'something_scripts'
    return Response(data)


  def partial_update(self, request):
    # Patch /requests/{id}
    data = 'something_scripts'
    return Response(data)

