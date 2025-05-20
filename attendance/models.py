from django.db import models

class AttendanceRecord(models.Model):
    tag_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
