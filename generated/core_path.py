from utils import *

def generateUrlsList(pathData):
  with open("./generated/urls.py", 'w', encoding='utf-8') as f:
    f.write("from django.urls import path, include\n")
    f.write("from rest_framework.routers import DefaultRouter\n")
    f.write("from @@@@@.views import *\n")
    f.write("\n")
    f.write("router = DefaultRouter()\n\n")

    dupCheck = []
    for path, methods in pathData.items():
      for method, _ in methods.items():
        if method.lower() in ['get', 'post', 'patch', 'put', 'delete']:
          urlPattern   = getPathNames(path)
          viewSetClass = getPathNames(path).capitalize() + "ViewSet"
          if urlPattern not in dupCheck:
            dupCheck.append(urlPattern)
            f.write(f"router.register(r'{urlPattern}', {viewSetClass}, basename='{urlPattern}')\n")

    f.write("\n")
    f.write("urlpatterns = [\n")
    f.write("    path('', include(router.urls)),\n")
    f.write("]\n")
  print(f"Django URLパターンが './generated/urls.py' に生成されました。")

def generateViewSets(pathData):
  with open("./generated/views.py", 'w', encoding='utf-8') as f:
    f.write("from rest_framework.viewsets import ViewSet\n")
    f.write("from rest_framework.response import Response\n")
    f.write("from .models import *\n")
    f.write("from .serializers import *\n")
    f.write("\n")

    method_map = {
      "get"    : "list",
      "post"   : "create",
      "patch"  : "partial_update",
      "put"    : "update",
      "delete" : "destroy",
    }
    dupCheck = []
    for path, methods in pathData.items():
      viewSetClass = getPathNames(path).capitalize() + "ViewSet"
      if viewSetClass not in dupCheck:
        dupCheck.append(viewSetClass)
        f.write(f"class {viewSetClass}(ViewSet):\n")
      else:
        f.write(f"\n")
      for method, _ in methods.items():
        if method.lower() in ['get', 'post', 'patch', 'put', 'delete']:
          method_name = method_map[method.lower()]
          f.write(f"  def {method_name}(self, request):\n")
          f.write(f"    # {method.capitalize()} {path}\n")
          f.write(f"    data = 'something_scripts'\n")
          f.write(f"    return Response(data)\n")
          f.write("\n")

  print(f"Django ViewSetが './generated/views.py' に生成されました。")

# def generateTestData(pathData):
#   with open("./generated/test_data.json", 'w', encoding='utf-8') as f:
#     test_data = {}
#     for path, methods in pathData.items():
#       if getPathNames(path) not in test_data: test_data[getPathNames(path)] = { "test_data1": {}, "test_data2": {}}
#       for method, _ in methods.items():
#         if method.lower() in ['get', 'post', 'patch', 'put', 'delete']:
#           test_data[getPathNames(path)][method_name] = {}

#     json.dump(test_data, f, indent=2, ensure_ascii=False)
#   print(f"Django テストデータが './generated/test_data.json' に生成されました。")

# def generateTestList(pathData):
#   with open("./generated/api_tests.py", 'w', encoding='utf-8') as f:
#     f.write("from django.forms.models import model_to_dict\n")
#     f.write("from rest_framework.test import APITestCase\n")
#     f.write("from rest_framework import status\n")
#     f.write("from .models import *\n")
#     f.write("\n")

#     dupCheck = []
#     for path, methods in pathData.items():
#       for method, _ in methods.items():
#         if method.lower() in ['get', 'post', 'put', 'delete']:
#           modelClass = getPathNames(path).capitalize()
#           testClass  = modelClass + "ViewSetTest"
#           if testClass not in dupCheck:
#             dupCheck.append(testClass)
#             with open("./generated/test_data.json", "r") as jf:
#               data = json.load(jf)

#               f.write(f"class {testClass}(APITestcase):\n")
#               f.write(f"  @classmethod\n")
#               f.write(f"  # テスト用データの準備\n")
#               f.write(f"  def setupTestData(cls):\n")
#               f.write(f"    cls.example1 = {modelClass}.objects.create({data[f"td_{getPathNames(path)}"]["test_data_1"]})\n")
#               f.write(f"    cls.example2 = {modelClass}.objects.create({data[f"td_{getPathNames(path)}"]["test_data_2"]})\n")
#               f.write(f"\n")
#               f.write(f"  # GET /example/ - 一覧取得のテスト\n")
#               f.write(f"  def test_list_endpoint(self):\n")
#               f.write(f"    response = self.client.get('{path}')\n")
#               f.write(f"    self.assertEqual(response.status_code, status.HTTP_200_OK)\n")
#               f.write(f"    self.assertEqual(len(response.data), 2)  # データ数を確認\n")
#               f.write(f"\n")
#               f.write(f"  # POST /example/ - 新規作成のテスト\n")
#               f.write(f"  def test_create_endpoint(self):\n")
#               f.write(f"    data = {data[f"td_{getPathNames(path)}"]["tc_create"]}\n")
#               f.write(f"    response = self.client.post('{path}', data)\n")
#               f.write(f"    self.assertEqual(response.status_code, status.HTTP_201_CREATED)\n")
#               f.write(f"    self.assertEqual({modelClass}.objects.count(), 3)  # レコード数を確認\n")
#               f.write(f"\n")
#               f.write(f"  # GET /example/<pk>/ - 特定のデータ取得テスト\n")
#               f.write(f"  def test_retrieve_endpoint(self):\n")
#               f.write(f"      response = self.client.get(f'{path}/{data[f"td_{getPathNames(path)}"]["tc_retrieve_params"]}')\n")
#               f.write(f"      self.assertEqual(response.status_code, status.HTTP_200_OK)\n")
#               for field, value in data[f"td_{getPathNames(path)}"]["tc_retrieve"]:
#                 f.write(f"      self.assertEqual(response.data['{field}'], {value})  # フィールドを確認\n")
#               f.write(f"\n")
#               f.write(f"  # PATCH /example/<pk>/ - 一部更新のテスト\n")
#               f.write(f"  def test_update_endpoint(self):\n")
#               f.write(f"    data = {data[f"td_{getPathNames(path)}"]["tc_patch"]}\n")
#               f.write(f"    response = self.client.patch(f'{path}/{data[f"td_{getPathNames(path)}"]["tc_patch_params"]}', data)\n")
#               f.write(f"    self.assertEqual(response.status_code, status.HTTP_200_OK)\n")
#               f.write(f"    self.example1.refresh_from_db()\n")
#               for field, value in data[f"td_{getPathNames(path)}"]["tc_retrieve"]:
#                 f.write(f"    self.assertEqual(self.example1.{field}, {value})\n")
#               f.write(f"\n")
#               f.write(f"  # PUT /example/<pk>/ - 全体更新のテスト\n")
#               f.write(f"  def test_update_endpoint(self):\n")
#               f.write(f"    data = {data[f"td_{getPathNames(path)}"]["tc_put"]}\n")
#               f.write(f"    response = self.client.patch(f'{path}/{data[f"td_{getPathNames(path)}"]["tc_put_params"]}', data)\n")
#               f.write(f"    self.assertEqual(response.status_code, status.HTTP_200_OK)\n")
#               f.write(f"    self.example1.refresh_from_db()\n")
#               f.write(f"    self.assertEqual(model_to_dict(self.example1), data)\n")
#               f.write(f"\n")
#               f.write(f"  # DELETE /example/<pk>/ - 削除のテスト\n")
#               f.write(f"  def test_delete_endpoint(self):\n")
#               f.write(f"    response = self.client.delete(f'{path}/{data[f"td_{getPathNames(path)}"]["tc_delete_params"]}')\n")
#               f.write(f"    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)\n")
#               f.write(f"    self.assertEqual({modelClass}.objects.count(), 1)  # レコード数を確認\n")
#               f.write(f"\n")

#   print(f"Django テストクラスが './generated/api_test.py' に生成されました。")

