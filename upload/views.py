from . import models
from django.shortcuts import render, redirect

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        try : uploadedFile = request.FILES["uploadedFile"]
        except : uploadedFile = ""

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()
        return redirect("upload:uploadFile")

    documents = models.Document.objects.all()

    return render(request, "upload/upload-file.html", context = {
        "files": documents
    })