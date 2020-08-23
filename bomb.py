# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests


vk_token = "token ot vk me"
vk_session = vk_api.VkApi(token=vk_token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        message = event.text.lower()
        if '!б' in message and event.from_me:
            bomb_sec = message.split(" ")[1]
            bomb_text = message.replace(f"!б {bomb_sec} ", "")
            try:
                vk.messages.delete(
                    message_ids=event.message_id,
                    delete_for_all=1
                )
                vk.messages.send(
                    peer_id=event.peer_id,
                    message=bomb_text,
                    expire_ttl=bomb_sec,
                    random_id=0
                )
            except BaseException as br:
                vk.messages.send(
                    peer_id=event.peer_id,
                    message=f"error: {b}",
                    random_id=0
                )
        if '!скрин' in message and event.from_me:
            sec = message.replace("!скрин ", "")
            vk.messages.edit(
                peer_id=event.peer_id,
                message="улыбаемся, скрин",
                message_id=event.message_id
            )
            vk.messages.delete(
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
        if '!off' in message and event.from_me:
            url = 'https://api.vk.me/method/account.setPrivacy?'
            parms= {
                'v': '5.109',
                'key': 'online',
                'value': 'only_me',
                'access_token': vk_token
            }
            r = requests.get(url, params=parms)
            vk.messages.edit(peer_id=event.peer_id,message="оффлайн поставлен",message_id=event.message_id)
        if '!on' in message and event.from_me:
            url = 'https://api.vk.me/method/account.setPrivacy?'
            parms = {
                'v': '5.109',
                'key': 'online',
                'value': 'all',
                'access_token': vk_token
            }
            r = requests.get(url, params=parms)
            vk.messages.edit(peer_id=event.peer_id, message="онлайн поставлен", message_id=event.message_id)

