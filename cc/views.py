from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from django.conf import settings
from cc.models import Choice, Poll

def index(request):
    t = loader.get_template('frontend/base_site.tpl')
    c = Context({
        'title': getattr(settings, "CC_TITLE", None),
        'content': "Hello, World!",
    })
    return HttpResponse(t.render(c))
    
def polls(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('frontend/polls.tpl')
    c = Context({
        'latest_poll_list': latest_poll_list,
        'title': "Polls list",
    })
    return HttpResponse(t.render(c))
    
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('frontend/detail.tpl', {'poll': p, 'title': p.question},
                               context_instance=RequestContext(request))
    
def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('frontend/results.tpl', {'poll': p})
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('frontend/detail.tpl', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('cc.views.results', args=(p.id,)))