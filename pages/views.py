from django.shortcuts import render

mylist = [
    {"title": "Buy groceries", "done": True},
    {"title": "Get gas", "done": True},
    {"title": "Mow lawn", "done": False},
    {"title": "Work on project", "done": True},
    {"title": "Take quiz", "done": False},
]


def home(request):
    return render(request, "home.html", {"mylist": mylist})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")