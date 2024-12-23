from rest_framework import serializers
from .models import *
class ParametersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Parameters
    fields = ['id', 'name', 'value', 'created_at', 'update_at', 'delete_at']

class PromptsListsSerializer(serializers.ModelSerializer):
  class Meta:
    model = PromptsLists
    fields = ['id', 'category', 'isLewd', 'name', 'value', 'created_at', 'update_at', 'delete_at']

class TextPhrasesSerializer(serializers.ModelSerializer):
  class Meta:
    model = TextPhrases
    fields = ['id', 'headerPrompt', 'footerPrompt', 'negativePrompt', 'requestOrderPhrase', 'scenesOrderPhrase', 'postingTemplate', 'created_at', 'update_at', 'delete_at']

class ConfigsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Configs
    fields = ['id', 'parameters', 'promptsLists', 'textPhrases', 'created_at', 'update_at', 'delete_at']

class TaskgroupsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Taskgroups
    fields = ['id', 'id', 'name', 'created_at', 'update_at', 'delete_at']

class TasksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tasks
    fields = ['id', 'id', 'group_id', 'index', 'name', 'created_at', 'update_at', 'delete_at']

class PostsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Posts
    fields = ['id', 'id', 'task_id', 'input_story', 'title_en', 'title_jp', 'title_symbol', 'pic_size_lewd', 'pic_size_soft', 'url_lewd', 'url_soft', 'her_quotes', 'created_at', 'update_at', 'delete_at']

class PromptsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prompts
    fields = ['id', 'id', 'task_id', 'basis_line', 'faces_line', 'bodies_line', 'genital_line', 'fluids_line', 'outfits_line', 'scenes_line', 'emotes_line', 'actions_line', 'camera_line', 'created_at', 'update_at', 'delete_at']

class BASISSerializer(serializers.ModelSerializer):
  class Meta:
    model = BASIS
    fields = ['id', 'id', 'request_id', 'theme', 'race', 'species', 'attributes', 'jobs', 'outfits', 'equips', 'period', 'period_details', 'weather', 'weather_details', 'times', 'times_details', 'location', 'created_at', 'update_at', 'delete_at']

class FACESSerializer(serializers.ModelSerializer):
  class Meta:
    model = FACES
    fields = ['id', 'id', 'request_id', 'face_looks', 'eyes_shape', 'personality', 'mood', 'hair_size', 'bangs_size', 'hair_style', 'bangs_style', 'created_at', 'update_at', 'delete_at']

class BODIESSerializer(serializers.ModelSerializer):
  class Meta:
    model = BODIES
    fields = ['id', 'id', 'request_id', 'thickness', 'boob_size', 'body_size', 'butt_size', 'skin_details', 'areola_size', 'nipple_size', 'inverted_nipples', 'public_hair', 'male_genital', 'sheath_foreskin', 'genital_size', 'genital_details', 'created_at', 'update_at', 'delete_at']

class COLORSSerializer(serializers.ModelSerializer):
  class Meta:
    model = COLORS
    fields = ['id', 'id', 'request_id', 'eyes_color', 'hair_color', 'skin_color', 'skin_sub_color', 'outfits_color', 'outfits_sub_color', 'equips_color', 'equips_sub_color', 'painting_color', 'created_at', 'update_at', 'delete_at']

class RequestsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Requests
    fields = ['id', 'id', 'task_id', 'basis_data', 'faces_data', 'bodies_data', 'colors_data', 'created_at', 'update_at', 'delete_at']

