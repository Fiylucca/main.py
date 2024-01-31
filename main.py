# main.py

from datetime import datetime, timedelta
import random
import telebot
import time

chat_id = "6818380622:AAHsO_NYd6O8qvyQ8M2-VmW-xrYUmJy83nw"
user_id = "-1002047776448"

LINK_SITE = '[JOGUE AGORA](https://1wowei.xyz/?open=register#hdew)'
LINK_SITE1 = '[Cadastre-se aqui](https://go.aff.7k-partners.com/e3i8ubqc)'
LINK_SITE2 = '[Instagram](https://www.instagram.com/fiy.lucca_/)'

bot = telebot.TeleBot(token=chat_id)

check_date = 0

while True:

    date_now = int(datetime.now().strftime("%H"))

    try:
        resultados = range(1, 15)
        aposta = random.sample(resultados, 1)
        dc1 = {

            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
            14: '14',
            15: '15',}
        for i in dc1:
            if i in aposta:
                dc1[i] = "⚽"
            else:
                dc1[i] = "🟢"
        
        resultados = range(1, 15)
        aposta = random.sample(resultados, 1)
        dc = {

            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
            14: '14',
            15: '15',}
        for i in dc:
            if i in aposta:
                dc[i] = "⚽"
            else:
                dc[i] = "🟢"

        resultados = range(1, 15)
        aposta = random.sample(resultados, 1)
        dc2 = {

            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
            14: '14',
            15: '15',}
        for i in dc1:
            if i in aposta:
                dc2[i] = "⚽"
            else:
                dc2[i] = "🟢"

        bb = random.randint(2, 4)

        tt = 2
        ha = datetime.now()
        na = random.randint(3, 5)
        ta = timedelta(minutes=na)
        nh = ha + ta
        nh = nh.strftime('%H:%M')

        palavras = ["Brasil","Argentina","Áustria","Bélgica","Urugual","Croácia","Portugal","Dinamarca","Inglaterra","Finlândia","França","Alemanha","Itália","Holanda","Espanha"]
        palavra_aleatorio = random.choice(palavras)
        print(palavra_aleatorio)
        msg  = (f'''

💰Entrada Confirmada 💰
🏁Seleção: {palavra_aleatorio}
🕗Valido até: {nh}
🔄N° de tentativas: {tt}

{dc1[1]}{dc1[2]}{dc1[3]}{dc1[4]}{dc1[5]}
{dc1[6]}{dc1[7]}{dc1[8]}{dc1[9]}{dc1[10]}
{dc1[11]}{dc1[12]}{dc1[13]}{dc1[14]}{dc1[15]}

{dc[1]}{dc[2]}{dc[3]}{dc[4]}{dc[5]}
{dc[6]}{dc[7]}{dc[8]}{dc[9]}{dc[10]}
{dc[11]}{dc[12]}{dc[13]}{dc[14]}{dc[15]}

{dc2[1]}{dc2[2]}{dc2[3]}{dc2[4]}{dc2[5]}
{dc2[6]}{dc2[7]}{dc2[8]}{dc2[9]}{dc2[10]}
{dc2[11]}{dc2[12]}{dc2[13]}{dc2[14]}{dc2[15]}

💰 {LINK_SITE} {LINK_SITE1}

''')
        msg2 = (f'''
✔️ Entrada Finalizada!
''')
        
        editmsg = bot.send_message(chat_id=user_id, text=msg, parse_mode='MARKDOWN', disable_web_page_preview=True)
        
        while True:
            hc = datetime.now().strftime('%H:%M')
            if hc == nh:
                # bot.delete_message(chat_id=user_id , message_id)
                bot.send_message(chat_id=user_id, text=msg2, parse_mode='MARKDOWN')
                na = random.randint(100, 200)
                time.sleep(na)
                break
    except Exception as e:
        print(e)
        pass
    try:
        resultados = range(1, 15)
        aposta = random.sample(resultados, 1)
        dc2 = {

            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
             14: '14',
            15: '15',}
        for i in dc1:
            if i in aposta:
                dc2[i] = "⚽"
            else:
                dc2[i] = "🟢"

        bb = random.randint(2, 4)

        tt = 2
        ha = datetime.now()
        na = random.randint(3, 5)
        ta = timedelta(minutes=na)
        nh = ha + ta
        nh = nh.strftime('%H:%M')

        palavras = ["Brasil","Argentina","Áustria","Bélgica","Urugual","Croácia","Portugal","Dinamarca","Inglaterra","Finlândia","França","Alemanha","Itália","Holanda","Espanha"]
        palavra_aleatorio = random.choice(palavras)
        print(palavra_aleatorio)
        msg  = (f'''

💰Entrada Confirmada 💰
🏁Seleção: {palavra_aleatorio}
🕗Valido até: {nh}
🔄N° de tentativas: {tt}

{dc1[1]}{dc1[2]}{dc1[3]}{dc1[4]}{dc1[5]}
{dc1[6]}{dc1[7]}{dc1[8]}{dc1[9]}{dc1[10]}
{dc1[11]}{dc1[12]}{dc1[13]}{dc1[14]}{dc1[15]}

{dc[1]}{dc[2]}{dc[3]}{dc[4]}{dc[5]}
{dc[6]}{dc[7]}{dc[8]}{dc[9]}{dc[10]}
{dc[11]}{dc[12]}{dc[13]}{dc[14]}{dc[15]}

💰 {LINK_SITE}

''')
        msg2 = (f'''
✔️ Entrada Finalizada!
''')
        
        editmsg = bot.send_message(chat_id=user_id, text=msg, parse_mode='MARKDOWN', disable_web_page_preview=True)
        
        while True:
            hc = datetime.now().strftime('%H:%M')
            if hc == nh:
                # bot.delete_message(chat_id=user_id , message_id)
                bot.send_message(chat_id=user_id, text=msg2, parse_mode='MARKDOWN')
                na = random.randint(100, 200)
                time.sleep(na)
                break
    except Exception as e:
        print(e)
        pass
    try:
        resultados = range(1, 15)
        aposta = random.sample(resultados, 1)
        dc2 = {

            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
            14: '14',
            15: '15',}
        for i in dc1:
            if i in aposta:
                dc2[i] = "⚽"
            else:
                dc2[i] = "🟢"

        bb = random.randint(2, 4)

        tt = 2
        ha = datetime.now()
        na = random.randint(3, 5)
        ta = timedelta(minutes=na)
        nh = ha + ta
        nh = nh.strftime('%H:%M')

        palavras = ["Brasil","Argentina","Áustria","Bélgica","Urugual","Croácia","Portugal","Dinamarca","Inglaterra","Finlândia","França","Alemanha","Itália","Holanda","Espanha"]
        palavra_aleatorio = random.choice(palavras)
        print(palavra_aleatorio)
        msg  = (f'''

💰Entrada Confirmada 💰
🏁Seleção: {palavra_aleatorio}
🕗Valido até: {nh}
🔄N° de tentativas: {tt}

{dc1[1]}{dc1[2]}{dc1[3]}{dc1[4]}{dc1[5]}
{dc1[6]}{dc1[7]}{dc1[8]}{dc1[9]}{dc1[10]}
{dc1[11]}{dc1[12]}{dc1[13]}{dc1[14]}{dc1[15]}

💰 {LINK_SITE2}

''')
        msg2 = (f'''
✔️ Entrada Finalizada!
''')
        
        editmsg = bot.send_message(chat_id=user_id, text=msg, parse_mode='MARKDOWN', disable_web_page_preview=True)
        
        while True:
            hc = datetime.now().strftime('%H:%M')
            if hc == nh:
                # bot.delete_message(chat_id=user_id , message_id)
                bot.send_message(chat_id=user_id, text=msg2, parse_mode='MARKDOWN')
                na = random.randint(100, 200)
                time.sleep(na)
                break
    except Exception as e:
        print(e)
        pass
