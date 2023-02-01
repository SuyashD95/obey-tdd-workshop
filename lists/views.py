from __future__ import annotations
from django.shortcuts import render
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


# Create your views here.
def homepage(request: HttpRequest) -> HttpResponse:
    """Renders the homepage of the application.

    Parameters
    ----------
    request: An object representing HTTP request sent to web server.

    Returns
    -------
    Object representing HTTP response containing HTML that can be used by
    browser to render the homepage.
    """
    return render(request, "lists/index.html")
