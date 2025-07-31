from django.shortcuts import redirect, render


def homepage(request):
    # return render(request, 'home.html')
    return redirect('posts/')


def about(request):
    # return HttpResponse("This is the about page of the project authentication system.")
    return render(request, 'about.html')
