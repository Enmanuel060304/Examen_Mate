from __future__ import with_statement
import pyautogui as pg
import time
import webbrowser as web
phone_no="+50557619670"
parsedMessage=" "
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(8)

for i in range(1000):
    pg.write('orlando furro')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    

pg.alert('Bomba de mensajes finalizada')



