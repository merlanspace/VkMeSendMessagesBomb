# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests


vk_token = "token"
vk_session = vk_api.VkApi(token=vk_token)
longpoll = VkLongPoll(vk_session)
bomb = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print("new messages")
        response = event.text.lower()

    if event.from_me and response.startswith('!бомб'):
        bomb_text = response.replace("!бомб ", "")
        try:
            bomb.messages.edit(
                peer_id=event.peer_id,
                message="Бомба, ложись!",
                message_id=event.message_id
            )
            bomb.messages.delete(
                message_ids=event.message_id,
                delete_for_all=1
            )
            bomb.messages.send(
                peer_id=event.peer_id,
                message=bomb_text,
                expire_ttl=5,
                random_id=0
            )
        except vk_api.exceptions.ApiError:
            pass
    if event.from_me and response.startswith('!скрин'):
        sec = response.replace("!скрин ", "")
        bomb.messages.edit(
            peer_id=event.peer_id,
            message="улыбаемся, скрин",
            message_id=event.message_id
        )
        bomb.messages.delete(
            message_ids=event.message_id,
            delete_for_all=1
        )
        url = 'https://api.vk.com/method/messages.sendService'
        parms= {
            'peer_id': event.peer_id,
            'action_type': 'chat_screenshot',
            'v': '5.103',
            'access_token': vk_token
        }
        for x in range(int(sec)):
            r = requests.get(url, params=parms)
