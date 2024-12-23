import re
import yaml
import json

props = [
  ["GET"   ,"list"          ],
  ["POST"  ,"create"        ],
  ["GET"   ,"retrieve"      ],
  ["PUT"   ,"update"        ],
  ["PATCH" ,"partial_update"],
  ["DELETE","destroy"       ],
]

def getPathNames(path):
    path_parts = re.sub(r'/|\{.*?\}', '', path)
    if path_parts:
        return path_parts
    return 'default'

def load_swagger_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
      return yaml.safe_load(file)
    elif file_path.endswith('.json'):
      return json.load(file)
    else:
      raise ValueError("対応していないファイル形式です。JSONまたはYAMLを使用してください。")

def getSwaggerObject(swagger, key):
  swgObject = swagger.get(key, {})
  if not swgObject:
    print("Swaggerファイルにpathsが見つかりません。")
    return
  return swgObject