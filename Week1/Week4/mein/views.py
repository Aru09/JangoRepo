from django.shortcuts import render


def book(request):

	return render(request, 'book.html')
# Create your views here.




def author(request):
	return render(request, 'author.html')

# Create your views here.
def publisher(request):

	return render(request, 'publisher.html')