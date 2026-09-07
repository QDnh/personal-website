from django.shortcuts import render

mylist = [
    {"name": "Buy groceries", "completed": True},
    {"name": "Get gas", "completed": True},
    {"name": "Mow lawn", "completed": False},
    {"name": "Work on project", "completed": True},
    {"name": "Take quiz", "completed": False},
]


def home(request):
    return render(request, "home.html", {"mylist": mylist})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")