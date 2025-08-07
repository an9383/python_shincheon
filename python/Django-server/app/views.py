from django.shortcuts import render
from django.http import HttpResponse

def main(request, number):
    if request.method == "POST":
        username = request.POST.get("username")  # 폼 데이터 가져오기
        context = {
            "username": f"{username} {number}입니다."
        }
        return render(request,"app.html", context)
    return render(request, 'app.html')  # GET 요청 시 폼 페이지 보여주기