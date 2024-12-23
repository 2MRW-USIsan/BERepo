def generateModels(schemaData):
  with open("./generated/models.py", 'w', encoding='utf-8') as f:
    f.write("from django.db import models\n\n")
    for schema_name, schema_details in schemaData.items():
      f.write(f"class {schema_name}(models.Model):\n")
      properties = schema_details.get('properties', {})
      if not properties:
          f.write("    pass\n\n")  # プロパティがない場合
          continue

      for prop_name, prop_details in properties.items():
          swagger_type = prop_details.get('type', 'string')
          swagger_desc = prop_details.get('description', '-')
          swagger_format = prop_details.get('format', '')
          if swagger_type == 'string' and swagger_format == 'date-time':
            django_field = 'models.DateTimeField()'
          else:
            type_mapping = {
              'integer': 'models.IntegerField()',
              'number': 'models.FloatField()',
              'string': 'models.CharField(max_length=255)',
              'boolean': 'models.BooleanField()',
              'object': 'models.JSONField()',
              'array': 'models.JSONField()',
            }
            django_field = type_mapping.get(swagger_type, 'models.TextField()')
          f.write(f"    {prop_name} = {django_field} #{swagger_desc}\n")

      f.write("\n")
  print(f"Django Modelクラスが './generated/models.py' に生成されました。")

def generateSerializer(schemaData):
  with open("./generated/serializer.py", 'w', encoding='utf-8') as f:
    f.write(f"from rest_framework import serializers\n")
    f.write(f"from .models import *\n")
    for schema_name, schema_details in schemaData.items():
      f.write(f"class {schema_name}Serializer(serializers.ModelSerializer):\n")
      f.write(f"  class Meta:\n")
      f.write(f"    model = {schema_name}\n")
      properties = schema_details.get('properties', {})
      if not properties:
          f.write("    pass\n\n")  # プロパティがない場合
          continue
      fields = ["id"]
      for prop_name, _ in properties.items(): fields.append(prop_name)
      fields.append("created_at")
      fields.append("update_at")
      fields.append("delete_at")
      f.write(f"    fields = {fields}\n")

      f.write("\n")
  print(f"Django Serializerクラスが './generated/serializer.py' に生成されました。")
