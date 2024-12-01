# Generated by Django 5.1.3 on 2024-11-27 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
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
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
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
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthtokenToken",
            fields=[
                (
                    "key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("created", models.DateTimeField()),
            ],
            options={
                "db_table": "authtoken_token",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
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
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Circuits",
            fields=[
                (
                    "circuitid",
                    models.AutoField(
                        db_column="circuitId", primary_key=True, serialize=False
                    ),
                ),
                (
                    "circuitref",
                    models.CharField(db_column="circuitRef", max_length=255),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("alt", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "circuits",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CommonProduct",
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
                ("name", models.CharField(max_length=100)),
                ("info", models.CharField(max_length=100)),
                ("price", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "common_product",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Constructors",
            fields=[
                (
                    "constructorid",
                    models.AutoField(
                        db_column="constructorId", primary_key=True, serialize=False
                    ),
                ),
                (
                    "constructorref",
                    models.CharField(db_column="constructorRef", max_length=255),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "db_table": "constructors",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Constructorstandings",
            fields=[
                (
                    "constructorstandingsid",
                    models.AutoField(
                        db_column="constructorStandingsId",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("raceid", models.IntegerField(db_column="raceId")),
                ("constructorid", models.IntegerField(db_column="constructorId")),
                ("points", models.FloatField()),
                ("position", models.IntegerField(blank=True, null=True)),
                (
                    "positiontext",
                    models.CharField(
                        blank=True, db_column="positionText", max_length=255, null=True
                    ),
                ),
                ("wins", models.IntegerField()),
            ],
            options={
                "db_table": "constructorstandings",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
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
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoCeleryResultsChordcounter",
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
                ("group_id", models.CharField(max_length=255, unique=True)),
                ("sub_tasks", models.TextField()),
                ("count", models.PositiveIntegerField()),
            ],
            options={
                "db_table": "django_celery_results_chordcounter",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoCeleryResultsGroupresult",
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
                ("group_id", models.CharField(max_length=255, unique=True)),
                ("date_created", models.DateTimeField()),
                ("date_done", models.DateTimeField()),
                ("content_type", models.CharField(max_length=128)),
                ("content_encoding", models.CharField(max_length=64)),
                ("result", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "django_celery_results_groupresult",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoCeleryResultsTaskresult",
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
                ("task_id", models.CharField(max_length=255, unique=True)),
                ("status", models.CharField(max_length=50)),
                ("content_type", models.CharField(max_length=128)),
                ("content_encoding", models.CharField(max_length=64)),
                ("result", models.TextField(blank=True, null=True)),
                ("date_done", models.DateTimeField()),
                ("traceback", models.TextField(blank=True, null=True)),
                ("meta", models.TextField(blank=True, null=True)),
                ("task_args", models.TextField(blank=True, null=True)),
                ("task_kwargs", models.TextField(blank=True, null=True)),
                ("task_name", models.CharField(blank=True, max_length=255, null=True)),
                ("worker", models.CharField(blank=True, max_length=100, null=True)),
                ("date_created", models.DateTimeField()),
                (
                    "periodic_task_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "db_table": "django_celery_results_taskresult",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
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
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Drivers",
            fields=[
                (
                    "driverid",
                    models.AutoField(
                        db_column="driverId", primary_key=True, serialize=False
                    ),
                ),
                ("driverref", models.CharField(db_column="driverRef", max_length=255)),
                ("number", models.IntegerField(blank=True, null=True)),
                ("code", models.CharField(blank=True, max_length=3, null=True)),
                ("name", models.CharField(db_column="Name", max_length=255)),
                ("dob", models.DateTimeField(blank=True, null=True)),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "db_table": "drivers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Driverstandings",
            fields=[
                (
                    "driverstandingsid",
                    models.AutoField(
                        db_column="driverStandingsId", primary_key=True, serialize=False
                    ),
                ),
                ("raceid", models.IntegerField(db_column="raceId")),
                ("driverid", models.IntegerField(db_column="driverId")),
                ("points", models.FloatField(blank=True, null=True)),
                ("position", models.IntegerField(blank=True, null=True)),
                (
                    "positiontext",
                    models.CharField(
                        blank=True, db_column="positionText", max_length=255, null=True
                    ),
                ),
                ("wins", models.IntegerField()),
            ],
            options={
                "db_table": "driverstandings",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="HomeFileinfo",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("path", models.CharField(max_length=200)),
                ("info", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "home_fileinfo",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Laptimes",
            fields=[
                (
                    "raceid",
                    models.IntegerField(
                        db_column="raceId", primary_key=True, serialize=False
                    ),
                ),
                ("driverid", models.IntegerField(db_column="driverId")),
                ("lap", models.IntegerField()),
                ("position", models.IntegerField(blank=True, null=True)),
                ("time", models.CharField(blank=True, max_length=255, null=True)),
                ("milliseconds", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "laptimes",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Pitstops",
            fields=[
                (
                    "raceid",
                    models.IntegerField(
                        db_column="raceId", primary_key=True, serialize=False
                    ),
                ),
                ("driverid", models.IntegerField(db_column="driverId")),
                ("stop", models.IntegerField()),
                ("lap", models.IntegerField()),
                ("duration", models.CharField(blank=True, max_length=255, null=True)),
                ("milliseconds", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "pitstops",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Qualifying",
            fields=[
                (
                    "qualifyid",
                    models.AutoField(
                        db_column="qualifyId", primary_key=True, serialize=False
                    ),
                ),
                ("raceid", models.IntegerField(db_column="raceId")),
                ("driverid", models.IntegerField(db_column="driverId")),
                ("constructorid", models.IntegerField(db_column="constructorId")),
                ("number", models.IntegerField(blank=True, null=True)),
                ("position", models.IntegerField(blank=True, null=True)),
                ("q1", models.CharField(blank=True, max_length=255, null=True)),
                ("q2", models.CharField(blank=True, max_length=255, null=True)),
                ("q3", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "qualifying",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Races",
            fields=[
                (
                    "raceid",
                    models.AutoField(
                        db_column="raceId", primary_key=True, serialize=False
                    ),
                ),
                ("year", models.IntegerField()),
                ("round", models.IntegerField()),
                ("circuitid", models.IntegerField(db_column="circuitId")),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "races",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Results",
            fields=[
                (
                    "resultid",
                    models.AutoField(
                        db_column="resultId", primary_key=True, serialize=False
                    ),
                ),
                ("raceid", models.IntegerField(db_column="raceId")),
                ("driverid", models.IntegerField(db_column="driverId")),
                ("constructorid", models.IntegerField(db_column="constructorId")),
                ("number", models.IntegerField(blank=True, null=True)),
                ("grid", models.IntegerField(blank=True, null=True)),
                ("position", models.IntegerField(blank=True, null=True)),
                (
                    "positiontext",
                    models.CharField(
                        blank=True, db_column="positionText", max_length=255, null=True
                    ),
                ),
                ("points", models.FloatField(blank=True, null=True)),
                ("laps", models.IntegerField(blank=True, null=True)),
                ("time", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "fastestlaptime",
                    models.CharField(
                        blank=True,
                        db_column="fastestLapTime",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("statusid", models.IntegerField(db_column="statusId")),
            ],
            options={
                "db_table": "results",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Seasons",
            fields=[
                ("year", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "seasons",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Sprintresults",
            fields=[
                (
                    "sprintresultid",
                    models.AutoField(
                        db_column="sprintResultId", primary_key=True, serialize=False
                    ),
                ),
                ("raceid", models.IntegerField(db_column="raceId")),
                ("driverid", models.IntegerField(db_column="driverId")),
                ("constructorid", models.IntegerField(db_column="constructorId")),
                ("number", models.IntegerField()),
                ("grid", models.IntegerField()),
                ("position", models.IntegerField(blank=True, null=True)),
                (
                    "positiontext",
                    models.CharField(db_column="positionText", max_length=255),
                ),
                ("points", models.FloatField()),
                ("laps", models.IntegerField()),
                ("time", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "fastestlaptime",
                    models.CharField(
                        blank=True,
                        db_column="fastestLapTime",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("statusid", models.IntegerField(db_column="statusId")),
            ],
            options={
                "db_table": "sprintresults",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "statusid",
                    models.AutoField(
                        db_column="statusId", primary_key=True, serialize=False
                    ),
                ),
                ("status", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "status",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "userid",
                    models.CharField(
                        db_column="userId",
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("userpw", models.CharField(db_column="userPw", max_length=255)),
                ("username", models.CharField(db_column="userName", max_length=255)),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UsersProfile",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("role", models.CharField(max_length=20)),
                ("full_name", models.CharField(blank=True, max_length=255, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(blank=True, max_length=255, null=True)),
                ("avatar", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "users_profile",
                "managed": False,
            },
        ),
    ]