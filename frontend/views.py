from django.shortcuts import render
from django.http import HttpResponse

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# https://medium.com/a-layman/build-single-page-application-with-react-and-django-part-1-connect-react-app-with-django-app-dbf6b5ec52f4
index_file_path = BASE_DIR / 'frontend/lunch-frontend/build/index.html'

def index(request):
    # return render(request, 'frontend/lunch-frontend/build/index.html')
    try:
        with open(index_file_path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        logging.exception('Production build of app not found')
