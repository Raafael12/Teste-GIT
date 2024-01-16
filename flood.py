import pyautogui as ag
from time import sleep


vai = True
iter = 0
print('Contagem de 3')
sleep(3)
print('Init')
ag.write('Oi')
ag.press('enter')
sleep(10)
while vai:
    print(iter)
    ag.write('mor')
    ag.press('enter')
    iter += 1
    if iter >= 10:
        break