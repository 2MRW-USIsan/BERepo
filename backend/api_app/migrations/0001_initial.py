# Generated by Django 5.1.4 on 2024-12-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BASIS",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("request_id", models.IntegerField()),
                ("theme", models.IntegerField()),
                ("race", models.CharField(max_length=255)),
                ("species", models.CharField(max_length=255)),
                ("attributes", models.CharField(max_length=255)),
                ("jobs", models.CharField(max_length=255)),
                ("outfits", models.CharField(max_length=255)),
                ("equips", models.CharField(max_length=255)),
                ("period", models.IntegerField()),
                ("period_details", models.CharField(max_length=255)),
                ("weather", models.IntegerField()),
                ("weather_details", models.CharField(max_length=255)),
                ("times", models.IntegerField()),
                ("times_details", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="BODIES",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("request_id", models.IntegerField()),
                ("thickness", models.IntegerField()),
                ("boob_size", models.IntegerField()),
                ("body_size", models.IntegerField()),
                ("butt_size", models.IntegerField()),
                ("skin_details", models.CharField(max_length=255)),
                ("areola_size", models.IntegerField()),
                ("nipple_size", models.IntegerField()),
                ("inverted_nipples", models.IntegerField()),
                ("public_hair", models.IntegerField()),
                ("male_genital", models.IntegerField()),
                ("sheath_foreskin", models.IntegerField()),
                ("genital_size", models.IntegerField()),
                ("genital_details", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="COLORS",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("request_id", models.IntegerField()),
                ("eyes_color", models.CharField(max_length=255)),
                ("hair_color", models.CharField(max_length=255)),
                ("skin_color", models.CharField(max_length=255)),
                ("skin_sub_color", models.CharField(max_length=255)),
                ("outfits_color", models.CharField(max_length=255)),
                ("outfits_sub_color", models.CharField(max_length=255)),
                ("equips_color", models.CharField(max_length=255)),
                ("equips_sub_color", models.CharField(max_length=255)),
                ("painting_color", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Configs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("parameters", models.JSONField()),
                ("promptsLists", models.JSONField()),
                ("textPhrases", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="FACES",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("request_id", models.IntegerField()),
                ("face_looks", models.IntegerField()),
                ("eyes_shape", models.IntegerField()),
                ("personality", models.IntegerField()),
                ("mood", models.IntegerField()),
                ("hair_size", models.IntegerField()),
                ("bangs_size", models.IntegerField()),
                ("hair_style", models.IntegerField()),
                ("bangs_style", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Parameters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("value", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("task_id", models.IntegerField()),
                ("input_story", models.CharField(max_length=255)),
                ("title_en", models.CharField(max_length=255)),
                ("title_jp", models.CharField(max_length=255)),
                ("title_symbol", models.CharField(max_length=255)),
                ("pic_size_lewd", models.CharField(max_length=255)),
                ("pic_size_soft", models.CharField(max_length=255)),
                ("url_lewd", models.CharField(max_length=255)),
                ("url_soft", models.CharField(max_length=255)),
                ("her_quotes", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Prompts",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("task_id", models.IntegerField()),
                ("basis_line", models.CharField(max_length=255)),
                ("faces_line", models.CharField(max_length=255)),
                ("bodies_line", models.CharField(max_length=255)),
                ("genital_line", models.CharField(max_length=255)),
                ("fluids_line", models.CharField(max_length=255)),
                ("outfits_line", models.CharField(max_length=255)),
                ("scenes_line", models.CharField(max_length=255)),
                ("emotes_line", models.CharField(max_length=255)),
                ("actions_line", models.CharField(max_length=255)),
                ("camera_line", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PromptsLists",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=255)),
                ("isLewd", models.BooleanField()),
                ("name", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Requests",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("task_id", models.IntegerField()),
                ("basis_data", models.JSONField()),
                ("faces_data", models.JSONField()),
                ("bodies_data", models.JSONField()),
                ("colors_data", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Taskgroups",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Tasks",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("group_id", models.IntegerField()),
                ("index", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TextPhrases",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headerPrompt", models.CharField(max_length=255)),
                ("footerPrompt", models.CharField(max_length=255)),
                ("negativePrompt", models.CharField(max_length=255)),
                ("requestOrderPhrase", models.CharField(max_length=255)),
                ("scenesOrderPhrase", models.CharField(max_length=255)),
                ("postingTemplate", models.CharField(max_length=255)),
            ],
        ),
    ]
