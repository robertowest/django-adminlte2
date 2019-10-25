from django.shortcuts import render

# Create your views here.
def base(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, 'polls/results.html', {'question': question})


def example(request):
    pass


def login(request):
    pass
