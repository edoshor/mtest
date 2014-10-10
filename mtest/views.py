from django.contrib.auth import login
from django.shortcuts import render_to_response
from django.template import RequestContext
from social.apps.django_app.utils import psa


def home(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('home.html', context_instance=context)


@psa('social:complete')
def register_by_access_token(request, backend):
    # This view expects an access_token GET parameter, if it's needed,
    # request.backend and request.strategy will be loaded with the current
    # backend and strategy.
    user = backend.do_auth(request.GET.get('access_token'))
    if user:
        login(request, user)
        return 'OK'
    else:
        return 'ERROR'