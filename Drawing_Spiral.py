import pyautogui as bot

distance = 500

bot.PAUSE = 2
bot.press("win")
bot.write("paint")
bot.press("enter")
bot.moveTo(358, 169)
while distance > 20:
    bot.dragRel(distance, 0, button="left")
    distance -= 20
    bot.dragRel(0, distance, button="left")
    distance -= 20
    bot.dragRel(-distance, 0, button="left")
    distance -= 20
    bot.dragRel(0, -distance, button="left")
    distance -= 20