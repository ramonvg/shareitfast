from django.shortcuts import render, render_to_response
from .forms import FileForm
from django.template import RequestContext


def index(request):
    file = FileForm(request.POST or None, request.FILES or None)
    form = FileForm()
    context = {
        'form': form,

    }
    if file.is_valid():
        instance = file.save()
        context['url'] = '/file/' + str(instance.file.name)[2:]

    return render(request, 'index.html', context)


def handler404(request):
    response = render_to_response('index.html', {'error': 'Error: 404.'},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('index.html', {'error': 'Error: 500.'},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
