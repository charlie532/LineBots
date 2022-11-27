from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .models import Location

line_bot_api = LineBotApi(settings.LINE_CHANNEL_TRIP_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_TRIP_SECRET)
 
 
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):

                locations = Location.objects.filter(area=event.message.text)
 
                content = ''
                for location in locations:
                    content += location.name + '\n' + location.address + '\n\n'
 
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=content)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()