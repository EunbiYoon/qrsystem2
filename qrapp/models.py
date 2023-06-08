from django.db import models

# Create your models here.
class QRCodeData(models.Model):
    data=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.data)+ ' | Updated at ' + str(self.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    class Meta:
        verbose_name_plural='QR Scanning Data'

