from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Club(BaseModel):
    slug = models.CharField(max_length=500, unique=True)
    name = models.CharField(max_length=500)
    upfit_id = models.IntegerField()
    level = models.CharField(max_length=200)
    sync = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Class(BaseModel):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500)
    day = models.DateField(db_index=True)
    hours = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    trainers = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "classes"

    def __str__(self):
        return self.title
