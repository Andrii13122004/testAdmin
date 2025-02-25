from django import forms
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ["first_name", "last_name", "middle_name", "phone", "email", "pdf_files", "image_files"]
