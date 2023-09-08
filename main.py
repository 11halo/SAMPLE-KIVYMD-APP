import random, pyautogui as pyauto
import time, rotatescreen as rs
for i in range(100000):
    h = random.randint(0, 1080)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration = 0.1)
    pyauto.hotkey('winleft', 'm')
    pd = rs.get_primary_display()
    angle_list = [90, 180, 270, 0]
    for x in range(100000):
        for x in angle_list:
         pd.rotate_to(x)
         time.sleep(0.1)
 