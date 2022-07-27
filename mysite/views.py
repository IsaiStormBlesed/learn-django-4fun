from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the polls index")

def tweets(request, id):
  return HttpResponse(f"Your post: {id}")