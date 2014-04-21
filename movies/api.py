from django.template.loader import render_to_string
from django.conf.urls import patterns
from movies.models import Movie


def tiles():
    return [
        (20, render_to_string('tile.html', {
            'url': '/movies/',
            'image': '/site-media/movie.svg',
            'title': 'Movies',
            'content': '%s new / %s total' % (Movie.objects.filter(watched=False).count(),Movie.objects.filter().count())
        })),
    ]

def urls():
    return patterns('movies.views',
        (r'^movies/$', 'index'),
    )
