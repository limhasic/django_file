import csv
import pandas as pd
from django.http import HttpResponse
from . import models
from django.shortcuts import render, redirect

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        try : uploadedFile = request.FILES["uploadedFile"]
        except : uploadedFile = ""

        if not fileTitle:
            fileTitle = uploadedFile.name

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


def view_csv(request, file_id):
    # 데이터베이스에서 파일 정보를 가져옵니다.
    document = models.Document.objects.get(id=file_id)

    # 업로드된 파일의 경로를 가져옵니다.
    file_path = document.uploadedFile.path

    # pandas를 이용해 CSV 파일을 읽어와 데이터프레임으로 변환합니다.
    df = pd.read_csv(file_path)

    # head() 메서드를 사용해 데이터프레임의 상위 5개 행을 가져옵니다.
    df_head = df.head()

    # 데이터프레임을 HTML 표 형태로 변환합니다.
    html_table = df_head.to_html()
    popup_html = f'<html><body>{html_table}</body></html>'
    # HttpResponse 객체를 생성해 JavaScript 코드를 반환합니다.
    return HttpResponse(popup_html)
