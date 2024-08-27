from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    # Normalize the path to avoid issues with trailing slashes or case sensitivity
    path = request.path.rstrip('/').lower()

    # Log the current page visit
    PageVisit.objects.create(path=path)
    print("Path logged:", path)

    # Query to get all page visits and the visits for the current path
    total_count = PageVisit.objects.all().count()  # Count all visits
    current_page_count = PageVisit.objects.filter(path=path).count()  # Count visits to this specific path

    # Calculate the percentage of visits to this specific page
    if total_count > 0:
        percent = (current_page_count * 100.0) / total_count
    else:
        percent = 0

    # Define the context to pass to the template
    my_context = {
        "page_title": "My Page",
        "page_visit_count": current_page_count,
        "total_visit_count": total_count,
        "percent": percent,
    }

    # Render the template with the context
    return render(request, "home.html", my_context)
