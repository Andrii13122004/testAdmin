from django.db import models
from django.core.exceptions import ValidationError

# Функція перевірки розміру файлу (максимум 10MB)
def validate_file_size(value):
    max_size = 10 * 1024 * 1024  # 10MB
    if value.size > max_size:
        raise ValidationError(f"Розмір файлу {value.name} перевищує 10 МБ.")

class FileUpload(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    pdf_files = models.FileField(upload_to="pdfs/", blank=True, null=True, validators=[validate_file_size])
    image_files = models.ImageField(upload_to="images/", blank=True, null=True, validators=[validate_file_size])

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
