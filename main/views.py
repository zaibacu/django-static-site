import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join


def get_page_or_404(name):
    try:
        fpath = safe_join(settings.SITE_PAGES_DIRECTORY, "{0}.md".format(name))
    except ValueError:
        raise Http404("Page not found")
    else:
        if not os.path.exists(fpath):
            raise Http404("Page not found")

    with open(fpath, "r") as f:
        page = Template(f.read())

    return page

def page(request, slug):
    page = get_page_or_404(slug)
    context = {"page": page}
    return render(request, "base.html", context)

