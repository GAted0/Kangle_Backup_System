from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10, unique=True, null=False)
    password = models.CharField(max_length=256, null=False)
    c_time = models.DateTimeField(auto_now_add=True)
    node_name = models.CharField(max_length=30, default='node1')
    down_times = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        ordering = ['-c_time']
        verbose_name = "用户"
        verbose_name_plural = "用户"