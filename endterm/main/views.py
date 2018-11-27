from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

"""@login_required
def author_list(request):
    # if request.user.is_authenticated:
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/list.html', context)
    # return redirect('login')"""