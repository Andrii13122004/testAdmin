from django.shortcuts import render, redirect
from .forms import FileUploadForm


def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success_page")  # Після завантаження йде редірект
    else:
        form = FileUploadForm()

    return render(request, "uploads/upload.html", {"form": form})


def success_page(request):
    return render(request, "uploads/success.html")
