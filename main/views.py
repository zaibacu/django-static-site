import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join


def get_pages():
    from collections import namedtuple
    page = namedtuple("page", ["url", "title"])

    def get_title(file):
        with open(safe_join(settings.SITE_PAGES_DIRECTORY, file), "r") as f:
            return f.readline()

    for name in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if name.endswith(".md"):
            yield page(name, get_title(name))


def get_page_or_404(name):
    try:
        fpath = safe_join(settings.SITE_PAGES_DIRECTORY, "{0}.md".format(name))
    except ValueError:
        raise Http404("Page not found")
    else:
        if not os.path.exists(fpath):
            raise Http404("Page not found")

    with open(fpath, "r") as f:
        import markdown as md
        page = Template(md.markdown(f.read()))

    return page


def page(request, slug):
    page = get_page_or_404(slug)
    context = {"page": page, "pages": get_pages()}
    return render(request, "base.html", context)


def home(request):
    return page(request, "about")
