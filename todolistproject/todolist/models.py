from django.db import models
from django.utils.timezone import now


class Thing(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    done_at = models.DateTimeField(default=None, null=True)

    def make_as_done(self):
        self.done_at = now()
        self.save()
