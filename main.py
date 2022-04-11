import vk_api
from datetime import datetime
import pytz
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
TOKEN = '7626cc706d445b332615f283f17a6eb3de8a8c9d3276f2772e7626dec920c43fb29dfb28b7baa0d1edcfa'
sp = ["начать"]
moscow_time = str(datetime.now(pytz.timezone('Europe/Moscow'))).split()[0]
week = datetime.now().strftime('%a')


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, 193462541)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            vk = vk_session.get_api()
            text = event.obj.message['text'].lower().split()
            flag = 0
            for item in sp:
                if item in text:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"""Привет!🙌
Вот что я умею:
- игра
- трек
- картинка""",
                                     random_id=random.randint(0, 2 ** 64))
                    flag = 1
                    break
                if "игра" in text:
                    user = event.obj.message['from_id']
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"Давайте играть!",
                                     random_id=random.randint(0, 2 ** 64))
                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['from_id'] == user:
                            print(event)
                            vk = vk_session.get_api()
                            text = event.obj.message['text'].lower().split()
                            n = 0
                            for item in sp:
                                if item in text:
                                    vk.messages.send(user_id=event.obj.message['from_id'],
                                                     message=f"ehf",
                                                     random_id=random.randint(0, 2 ** 64))
                                    n = 1
                            if n == 0:
                                vk.messages.send(user_id=event.obj.message['from_id'],
                                                 message=f"Перехотели играть?",
                                                 random_id=random.randint(0, 2 ** 64))
                                if 'нет' in text:
                                    vk.messages.send(user_id=event.obj.message['from_id'],
                                                     message=f";(",
                                                     random_id=random.randint(0, 2 ** 64))
                                    break
                            flag = 1
                if 'трек' in text:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"песня",
                                     random_id=random.randint(0, 2 ** 64))
                    flag = 1
                if 'картинка' in text:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"Лови топ пикчу!",
                                     random_id=random.randint(0, 2 ** 64))
                    flag = 1

            if flag == 0:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Напишите '""начать""'",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
