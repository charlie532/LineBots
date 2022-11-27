from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent, 
    TextSendMessage,
    TemplateSendMessage, 
    ButtonsTemplate, 
    MessageTemplateAction,
    PostbackEvent, 
    PostbackTemplateAction,
)

from .scraper import IFoodie

line_bot_api = LineBotApi(settings.LINE_CHANNEL_FOOD_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_FOOD_SECRET)
 
 
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        # parse event
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        # repeat event message
        for event in events:
            if isinstance(event, MessageEvent):
                if event.message.text == "點餐":
                    line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text = 'Buttons template',
                            template = ButtonsTemplate(
                                title = 'Region',
                                text = '請選擇地區',
                                actions = [
                                    PostbackTemplateAction(
                                        label = '台北市',
                                        text = '\n',
                                        data = 'A&台北市',
                                    ),
                                    PostbackTemplateAction(
                                        label = '新北市',
                                        text = '\n',
                                        data = 'A&新北市',
                                    ),
                                    PostbackTemplateAction(
                                        label = '新竹市',
                                        text = '\n',
                                        data = 'A&新竹市',
                                    ),
                                ]
                            )
                        )
                    )
                else:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(
                            text = "使用方法:\n輸入[點餐]->選擇地區->選擇種類->顯示推薦美食\n"
                        )
                    )
            elif isinstance(event, PostbackEvent):
                if event.postback.data[0] == 'A':
                    area = event.postback.data[2:]
                    line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text = 'Buttons template',
                            template = ButtonsTemplate(
                                title = 'Category',
                                text = '請選擇美食類別',
                                actions = [
                                    PostbackTemplateAction(
                                        label = '火鍋',
                                        text = '\n',
                                        data = 'B&' + area + '&火鍋'
                                    ),
                                    PostbackTemplateAction(
                                        label = '日本料理',
                                        text = '\n',
                                        data = 'B&' + area + '&日本料理'
                                    ),
                                    PostbackTemplateAction(
                                        label = '燒烤',
                                        text = '\n',
                                        data = 'B&' + area + '&燒烤'
                                    )
                                ]
                            )
                        )
                    )
                elif event.postback.data[0] == "B":
                    # result1:area, result2: restaurant category
                    result = event.postback.data[2:].split('&')
                    food = IFoodie(
                        result[0],
                        result[1]
                    )
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=food.scrape())
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()