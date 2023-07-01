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
        return self.slug
