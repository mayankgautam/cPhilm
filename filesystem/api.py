from django.template.loader import render_to_string
from django.conf.urls import patterns

def tiles():
    return [
        (100, render_to_string('tile.html', {
            'url': '/browse/',
            'image': '/site-media/folders.svg',
            'title': 'Browse files',
            'content': ''
        })),
    ]

def urls():
    return patterns('filesystem.views',
        (r'^browse/$', 'browse'),
    )
