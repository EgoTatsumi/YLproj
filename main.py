import vk_api
from datetime import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
TOKEN = '7626cc706d445b332615f283f17a6eb3de8a8c9d3276f2772e7626dec920c43fb29dfb28b7baa0d1edcfa'
sp = ["начать", 'давай', 'да', 'стартуем']
vk_session = vk_api.VkApi(
        token=TOKEN)
longpoll = VkBotLongPoll(vk_session, 193462541)
pics = ['11.jpg', '12.jpg', '22.jpg', '13.jpg', '21.jpg', '23.jpg', '32.jpg', '31.jpg', '33.jpg', '42.jpg']
answers = {'11.jpg': ['Nissan Silvia s14', 'Nissan Silvia s13', 'Nissan Silvia s15'],
           '12.jpg': ['Nissan Silvia s14', 'Nissan Silvia s15', 'Nissan Silvia s13'],
           '22.jpg': ['Mazda Rx-7 FD', 'Mazda Rx-7 FC', 'Mazda Mx-5'],
           '13.jpg': ['Nissan 350z', 'Honda s2000', 'Nissan 370z'],
           '21.jpg': ['Honda NSX', 'Honda Prelude-3', 'Nissan 180sx'],
           '23.jpg': ['Mazda Rx-7 FC', 'Toyota Supra Mk4', 'Mazda Rx-7 FD'],
           '32.jpg': ['Honda Prelude-3', 'Honda Civic', 'Toyota Celica'],
           '31.jpg': ['Toyota Altezza', 'Nissan 370z', 'Honda Civic'],
           '33.jpg': ['Toyota Cresta jzx100', 'Toyota Chaser jzx100', 'Toyota  Mark II  jzx100'],
           '42.jpg': ['Nissan Fairlady 240zx', 'Nissan Fairlady 300zx', 'Toyota Celica']}


audios = ['North Memphis Phonk Killer',
          'Vaas MAKAVELIGODD',
          'PROPHECY SHADXWBXRN',
          'Consumption PANICX, SH3TLVIZ',
          'OPTICAL RANGE Mista Playa',
          'Russian Phonk Impuls',
          'HATE LEYNCLOUD',
          'prolly my spookiest beat (sped up) prodby668',
          'uptown SACHIHIRO(幸福) feat. INASEH',
          'S.X.N.D. N.X.D.E.S. BADTRIP MUSIC, GREEN ORXNGE, Send 1']


phrases = ['Лови топ пикчу!', 'Держи фоточку!', 'Лови!', 'Вот еще!']

def send_photo(name):
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(f'data\{name}')
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


def send_game_photo(name):
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(f'data/test/{name}')
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


def send_audio(numb):
    attachment = audios[numb]
    return attachment


def main():
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
                                     message=f"""Давайте играть!
Правила таковы: я скидываю вам фотографию автомобиля и варианты ответов, а ваша задача угадать автомобиль
Если вы хотите начать напишите "стартуем", ну а если перехотите играть напишите "хватит"
Удачи!""",
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
                                                     message=f"Давайте же начнем!",
                                                     random_id=random.randint(0, 2 ** 64))
                                    n = 1
                            if n == 0:
                                vk.messages.send(user_id=event.obj.message['from_id'],
                                                 message=f"Перехотели играть?",
                                                 random_id=random.randint(0, 2 ** 64))
                                for event in longpoll.listen():
                                    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['from_id'] == user:
                                        text = event.obj.message['text'].lower().split()
                                        if 'да' in text:
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f";(",
                                                             random_id=random.randint(0, 2 ** 64))
                                        if 'нет' in text:
                                            n += 1
                                        break
                            if n == 1:
                                random.shuffle(pics)
                                number = 0
                                attachment = send_game_photo(pics[number])
                                cars = answers.get(pics[number])
                                print(cars)
                                vk.messages.send(user_id=event.obj.message['from_id'],
                                                 message=f'''1- {cars[0]}
                                                             2- {cars[1]}
                                                             3- {cars[2]}''',
                                                 attachment=attachment,
                                                 random_id=random.randint(0, 2 ** 64))
                                for event in longpoll.listen():
                                    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['from_id'] == user:
                                        print(event)
                                        right_num = 0
                                        all_num = 0
                                        vk = vk_session.get_api()
                                        text = event.obj.message['text'].lower().split()
                                        print(str(int(pics[number].split('.')[0]) % 10))
                                        if str(int(pics[number].split('.')[0]) % 10) in text:
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f"Правильно!",
                                                             random_id=random.randint(0, 2 ** 64))
                                            right_num += 1
                                            all_num += 1
                                        if str(int(pics[number].split('.')[0]) % 10) not in text:
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f"""К сожалению это неверно(
                                        Правильный ответ: {cars[int(pics[number].split('.')[0]) % 10 - 1]}""",
                                                             random_id=random.randint(0, 2 ** 64))
                                            all_num += 1
                                        while'хватит' not in text and number != 9:
                                            number += 1
                                            print(number)
                                            cars = answers.get(pics[number])
                                            attachment = send_game_photo(pics[number])
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f'''1- {cars[0]}
                                                                         2- {cars[1]}
                                                                         3- {cars[2]}''',
                                                             attachment=attachment,
                                                             random_id=random.randint(0, 2 ** 64))
                                            for event in longpoll.listen():
                                                if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['from_id'] == user:
                                                    print(event)
                                                    vk = vk_session.get_api()
                                                    text = event.obj.message['text'].lower().split()
                                                    print(str(int(pics[number].split('.')[0]) % 10))
                                                    if str(int(pics[number].split('.')[0]) % 10) in text and 'хватит'\
                                                            not in text:
                                                        vk.messages.send(user_id=event.obj.message['from_id'],
                                                                         message=f"Правильно!",
                                                                         random_id=random.randint(0, 2 ** 64))
                                                        right_num += 1
                                                        all_num += 1
                                                    if str(int(pics[number].split('.')[0]) % 10) not in text and \
                                                            'хватит' not in text:
                                                        vk.messages.send(user_id=event.obj.message['from_id'],
                                                                         message=f"""К сожалению это неверно(
                                                                                    Правильный ответ: {cars[int(pics[number].split('.')[0]) % 10 - 1]}""",
                                                                         random_id=random.randint(0, 2 ** 64))
                                                        all_num += 1
                                                    break
                                        result = right_num / all_num * 100
                                        if result < 50:
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f"""Фууух, хорошо поиграли😊
Твой результат: {right_num}/{all_num}
Тебе следует потренироваться и подписаться на наш паблик, ведь с ним ты будешь запоминать клевые тачки в два раза быстрее!""",
                                                             random_id=random.randint(0, 2 ** 64))
                                        elif result >= 50 and result <= 75:
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f"""Фууух, хорошо поиграли😊
Твой результат: {right_num}/{all_num}
Очень даже неплохо, но практика не помешает, а в этом я и наш паблик поможет!""",
                                                             random_id=random.randint(0, 2 ** 64))
                                        elif result > 75 and result <= 100:
                                            vk.messages.send(user_id=event.obj.message['from_id'],
                                                             message=f"""Фууух, хорошо поиграли😊
Твой результат: {right_num}/{all_num}
Братанчик, да ты просто машина!
Ты очень хорошо знаешь JDM автомобили!""",
                                                             random_id=random.randint(0, 2 ** 64))
                                        break
                            flag = 1
                            break
                if 'трек' in text:
                    numb = random.randint(0, 9)
                    attachment = send_audio(numb)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"{attachment}",
                                     random_id=random.randint(0, 2 ** 64))
                    flag = 1
                    break
                if 'картинка' in text:
                    numb = random.randint(1, 10)
                    attachment = send_photo(f'{numb}.jpg')
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"{phrases[random.randint(0, 3)]}",
                                     attachment=attachment,
                                     random_id=random.randint(0, 2 ** 64))
                    flag = 1
                    break
            if flag == 0:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Напишите '""начать""'",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
