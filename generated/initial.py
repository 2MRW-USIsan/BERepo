
from core_schema import *
from core_path import *

def generateWithPaths(swagger):
  pathData = getSwaggerObject(swagger, 'paths')
  generateUrlsList(pathData)
  generateViewSets(pathData)

def generateWithSchemas(swagger):
  schemaData = getSwaggerObject(
    getSwaggerObject(swagger, 'components'),
    'schemas'
  )
  generateModels(schemaData)
  generateSerializer(schemaData)

if __name__ == "__main__":
  # Swaggerファイルの読み込みとモデル生成
  try:
    swaggerData = load_swagger_file("./swagger.yaml")
    generateWithSchemas(swaggerData)
    generateWithPaths(swaggerData)

  except Exception as e:
    print(f"エラー: {e}")


