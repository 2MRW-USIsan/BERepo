from django.db import models

class Parameters(models.Model):
    name = models.CharField(max_length=255) #パラメータ名
    value = models.IntegerField() #パラメータ値

class PromptsLists(models.Model):
    category = models.CharField(max_length=255) #プロンプトリストのカテゴリー
    isLewd = models.BooleanField() #NSFWフラグ
    name = models.CharField(max_length=255) #プロンプト情報（キー）
    value = models.CharField(max_length=255) #プロンプト情報（バリュー）

class TextPhrases(models.Model):
    headerPrompt = models.CharField(max_length=255) #ヘッダープロンプト
    footerPrompt = models.CharField(max_length=255) #フッタープロンプト
    negativePrompt = models.CharField(max_length=255) #ネガティブプロンプト
    requestOrderPhrase = models.CharField(max_length=255) #リクエスト用Chatプロンプト
    scenesOrderPhrase = models.CharField(max_length=255) #脚本用Chatプロンプト
    postingTemplate = models.CharField(max_length=255) #投稿用テンプレート

class Configs(models.Model):
    parameters = models.JSONField() #-
    promptsLists = models.JSONField() #-
    textPhrases = models.JSONField() #-

class Taskgroups(models.Model):
    id = models.IntegerField() #-
    name = models.CharField(max_length=255) #-

class Tasks(models.Model):
    id = models.IntegerField() #-
    group_id = models.IntegerField() #-
    index = models.IntegerField() #-
    name = models.CharField(max_length=255) #-

class Posts(models.Model):
    id = models.IntegerField() #-
    task_id = models.IntegerField() #-
    input_story = models.CharField(max_length=255) #-
    title_en = models.CharField(max_length=255) #-
    title_jp = models.CharField(max_length=255) #-
    title_symbol = models.CharField(max_length=255) #-
    pic_size_lewd = models.CharField(max_length=255) #-
    pic_size_soft = models.CharField(max_length=255) #-
    url_lewd = models.CharField(max_length=255) #-
    url_soft = models.CharField(max_length=255) #-
    her_quotes = models.JSONField() #-

class Prompts(models.Model):
    id = models.IntegerField() #-
    task_id = models.IntegerField() #-
    basis_line = models.CharField(max_length=255) #-
    faces_line = models.CharField(max_length=255) #-
    bodies_line = models.CharField(max_length=255) #-
    genital_line = models.CharField(max_length=255) #-
    fluids_line = models.CharField(max_length=255) #-
    outfits_line = models.CharField(max_length=255) #-
    scenes_line = models.CharField(max_length=255) #-
    emotes_line = models.CharField(max_length=255) #-
    actions_line = models.CharField(max_length=255) #-
    camera_line = models.CharField(max_length=255) #-

class BASIS(models.Model):
    id = models.IntegerField() #-
    request_id = models.IntegerField() #-
    theme = models.IntegerField() #テーマ情報
    race = models.CharField(max_length=255) #人種／動物種情報
    species = models.CharField(max_length=255) #人なら民族／種族、獣人なら品種／亜種の情報を記載
    attributes = models.CharField(max_length=255) #属性情報
    jobs = models.CharField(max_length=255) #職業情報
    outfits = models.CharField(max_length=255) #服装情報
    equips = models.CharField(max_length=255) #所持品情報
    period = models.IntegerField() #時代情報
    period_details = models.CharField(max_length=255) #時代詳細情報
    weather = models.IntegerField() #天候情報
    weather_details = models.CharField(max_length=255) #天候詳細情報
    times = models.IntegerField() #時間帯情報
    times_details = models.CharField(max_length=255) #時間帯詳細情報
    location = models.CharField(max_length=255) #場所情報

class FACES(models.Model):
    id = models.IntegerField() #-
    request_id = models.IntegerField() #-
    face_looks = models.IntegerField() #顔つき情報
    eyes_shape = models.IntegerField() #目つき情報
    personality = models.IntegerField() #性格情報
    mood = models.IntegerField() #雰囲気情報
    hair_size = models.IntegerField() #毛髪量
    bangs_size = models.IntegerField() #前髪量
    hair_style = models.IntegerField() #ヘアスタイル
    bangs_style = models.IntegerField() #前髪スタイル

class BODIES(models.Model):
    id = models.IntegerField() #-
    request_id = models.IntegerField() #-
    thickness = models.IntegerField() #太さ
    boob_size = models.IntegerField() #バスト
    body_size = models.IntegerField() #ウエスト
    butt_size = models.IntegerField() #ヒップ
    skin_details = models.CharField(max_length=255) #肌特徴
    areola_size = models.IntegerField() #乳輪
    nipple_size = models.IntegerField() #乳首
    inverted_nipples = models.IntegerField() #陥没乳首
    public_hair = models.IntegerField() #陰毛
    male_genital = models.IntegerField() #男性器
    sheath_foreskin = models.IntegerField() #埋没包茎
    genital_size = models.IntegerField() #男性器サイズ
    genital_details = models.IntegerField() #男性器特徴

class COLORS(models.Model):
    id = models.IntegerField() #-
    request_id = models.IntegerField() #-
    eyes_color = models.CharField(max_length=255) #目色情報
    hair_color = models.CharField(max_length=255) #髪色情報
    skin_color = models.CharField(max_length=255) #肌色情報
    skin_sub_color = models.CharField(max_length=255) #肌サブ色情報
    outfits_color = models.CharField(max_length=255) #服装色情報
    outfits_sub_color = models.CharField(max_length=255) #服装サブ色情報
    equips_color = models.CharField(max_length=255) #所持品色情報
    equips_sub_color = models.CharField(max_length=255) #所持品サブ色情報
    painting_color = models.CharField(max_length=255) #ペイントカラー情報

class Requests(models.Model):
    id = models.IntegerField() #-
    task_id = models.IntegerField() #-
    basis_data = models.JSONField() #構成情報データ
    faces_data = models.JSONField() #構成情報データ
    bodies_data = models.JSONField() #構成情報データ
    colors_data = models.JSONField() #構成情報データ

