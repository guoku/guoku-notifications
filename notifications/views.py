from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template import loader

from apps.core.extend.paginator import ExtentPaginator, PageNotAnInteger, EmptyPage
from apps.core.models import Entity_Like, Entity, Sub_Category
from django.db.models import Count
from apps.core.utils.http import JSONResponse

from datetime import datetime
import random

@require_GET
@login_required
def messages(request, template='notifications/messages/message.html'):
    _user = request.user
    _page = request.GET.get('page', 1)
    _timestamp = request.GET.get('timestamp',None)
    if _timestamp != None:
        _timestamp = datetime.fromtimestamp(float(_timestamp))
    else:
        _timestamp = datetime.now()

    el = Entity_Like.objects.popular()
    cids = Entity.objects.filter(pk__in=list(el)).annotate(dcount=Count('category')).values_list('category_id', flat=True)

    _categories = Sub_Category.objects.filter(id__in=list(cids), status=True)

    message_list = _user.notifications.filter(timestamp__lt=_timestamp)

    paginator = ExtentPaginator(message_list, 10)

    try:
        _messages = paginator.page(_page)
    except PageNotAnInteger:
        _messages = paginator.page(1)
    except EmptyPage:
        raise Http404

    _user.notifications.mark_all_as_read()
    if request.is_ajax():
        res = {
            'status' : 0,
            'msg' : 'no data'
        }
        if len(res) > 0:
            _t = loader.get_template('notifications/messages/partial/ajax_notification.html')
            _c = RequestContext(request, {
                    'messages': _messages,
            })
            _data = _t.render(_c)
            res = {
                'status': 1,
                'data': _data,
            }
            return JSONResponse(data=res, content_type='text/html; charset=utf-8',)

    return render_to_response(
        template,
        {
            'messages': _messages,
            'categories': random.sample(_categories, 6),
            # 'category': category,
        },
        context_instance = RequestContext(request),
    )


__author__ = 'edison'
