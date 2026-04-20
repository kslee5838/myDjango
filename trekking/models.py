from django.db import models

class YourTrekking(models.Model):
    id = models.BigAutoField(primary_key=True)
    trek_date = models.DateField()
    weekday = models.CharField(max_length=128, null=True, blank=True)
    meeting_type = models.CharField(max_length=128, null=True, blank=True)
    meeting_type_id = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=128, null=True, blank=True)
    companion1 = models.CharField(max_length=128, null=True, blank=True)
    companion2 = models.CharField(max_length=128, null=True, blank=True)
    companion3 = models.CharField(max_length=128, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'trekking'  # Add this line!
        db_table = 'yourtrekking'
        managed = False

    def __str__(self):
        return f"{self.trek_date} - {self.location}"