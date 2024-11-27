from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Circuits(models.Model):
    circuitid = models.AutoField(db_column='circuitId', primary_key=True)  # Field name made lowercase.
    circuitref = models.CharField(db_column='circuitRef', max_length=255)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    alt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuits'


class CommonProduct(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_product'


class Constructors(models.Model):
    constructorid = models.AutoField(db_column='constructorId', primary_key=True)  # Field name made lowercase.
    constructorref = models.CharField(db_column='constructorRef', max_length=255)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=255)
    nationality = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'constructors'


class Constructorstandings(models.Model):
    constructorstandingsid = models.AutoField(db_column='constructorStandingsId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    points = models.FloatField()
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(db_column='positionText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'constructorstandings'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryResultsChordcounter(models.Model):
    group_id = models.CharField(unique=True, max_length=255)
    sub_tasks = models.TextField()
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'django_celery_results_chordcounter'


class DjangoCeleryResultsGroupresult(models.Model):
    group_id = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_done = models.DateTimeField()
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_groupresult'


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    worker = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()
    periodic_task_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drivers(models.Model):
    driverid = models.AutoField(db_column='driverId', primary_key=True)  # Field name made lowercase.
    driverref = models.CharField(db_column='driverRef', max_length=255)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    dob = models.DateTimeField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'


class Driverstandings(models.Model):
    driverstandingsid = models.AutoField(db_column='driverStandingsId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    points = models.FloatField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(db_column='positionText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'driverstandings'


class HomeFileinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=200)
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'home_fileinfo'


class Laptimes(models.Model):
    raceid = models.IntegerField(db_column='raceId', primary_key=True)  # Field name made lowercase. The composite primary key (raceId, driverId, lap) found, that is not supported. The first column is selected.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    lap = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    milliseconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laptimes'
        unique_together = (('raceid', 'driverid', 'lap'),)


class Pitstops(models.Model):
    raceid = models.IntegerField(db_column='raceId', primary_key=True)  # Field name made lowercase. The composite primary key (raceId, driverId, stop) found, that is not supported. The first column is selected.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    stop = models.IntegerField()
    lap = models.IntegerField()
    duration = models.CharField(max_length=255, blank=True, null=True)
    milliseconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pitstops'
        unique_together = (('raceid', 'driverid', 'stop'),)


class Qualifying(models.Model):
    qualifyid = models.AutoField(db_column='qualifyId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    q1 = models.CharField(max_length=255, blank=True, null=True)
    q2 = models.CharField(max_length=255, blank=True, null=True)
    q3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qualifying'


class Races(models.Model):
    raceid = models.AutoField(db_column='raceId', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField()
    round = models.IntegerField()
    circuitid = models.IntegerField(db_column='circuitId')  # Field name made lowercase.
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'races'


class Results(models.Model):
    resultid = models.AutoField(db_column='resultId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    grid = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(db_column='positionText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    points = models.FloatField(blank=True, null=True)
    laps = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    fastestlaptime = models.CharField(db_column='fastestLapTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statusid = models.IntegerField(db_column='statusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'results'


class Seasons(models.Model):
    year = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'seasons'


class Sprintresults(models.Model):
    sprintresultid = models.AutoField(db_column='sprintResultId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    number = models.IntegerField()
    grid = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(db_column='positionText', max_length=255)  # Field name made lowercase.
    points = models.FloatField()
    laps = models.IntegerField()
    time = models.CharField(max_length=255, blank=True, null=True)
    fastestlaptime = models.CharField(db_column='fastestLapTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statusid = models.IntegerField(db_column='statusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sprintresults'


class Status(models.Model):
    statusid = models.AutoField(db_column='statusId', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'


class User(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=255)  # Field name made lowercase.
    userpw = models.CharField(db_column='userPw', max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UsersProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_profile'