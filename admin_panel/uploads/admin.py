from django.contrib import admin
from django.utils.html import format_html
from .models import FileUpload


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone', 'view_pdf', 'view_image')
    readonly_fields = ('pdf_files', 'image_files')

    def view_pdf(self, obj):
        if obj.pdf_files:
            return format_html('<a href="{}" target="_blank">📄 Переглянути PDF</a>', obj.pdf_files.url)
        return "Немає файлу"

    def view_image(self, obj):
        if obj.image_files:
            return format_html('<img src="{}" style="max-width:100px;">', obj.image_files.url)
        return "Немає зображення"

    view_pdf.short_description = "PDF-файл"
    view_image.short_description = "Зображення"


admin.site.register(FileUpload, FileUploadAdmin)
