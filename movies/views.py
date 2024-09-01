from django.shortcuts import render,get_object_or_404
from .models import Email,Movie
# Create your views here.
def home(request):
    email_id = request.GET.get('email')
    movies = Movie.objects.all()
    searchTerm = request.GET.get("searchMovie")
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    if email_id:
        email = Email.objects.create(emailid = email_id)
        email.save()
        return render(request,'email.html',{'email':email_id})
    return render(request, 'home.html', {'movies':movies})

def email(request):
    return render(request,'email.html')

def detail(request,movie_id):
    movies = get_object_or_404(Movie,pk=movie_id)
    return render(request,'detail.html',{'movies':movies})