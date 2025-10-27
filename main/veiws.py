from django.shortcuts import render



def home_page(request):

    print(request.user)

    return render(request,'core/home_page.html')