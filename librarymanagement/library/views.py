from django.http import HttpResponseRedirect
from django.shortcuts import render

from library.models import Book

def index(request):
    if request.method == "POST":
        book_name = request.POST["book"]
        bk = Book(namee=book_name)
        bk.save()
    bkk = Book.objects.all()
    context = {
        'books' : bkk,
    }
    return render(request,"library/index.html",context)
def delete(request,id):
    book = Book.objects.filter(id=id)
    book.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method== "POST":
        updated_name = request.POST['book']
        book  = Book.objects.get(id=id)
        print(f"old name was {book.namee}")
        book.namee =updated_name
        book.save()
        return HttpResponseRedirect("/")
    bkk = Book.objects.get(id=id)
    context = {
        'book' : bkk,
    }
    return render(request,"library/update.html",context)