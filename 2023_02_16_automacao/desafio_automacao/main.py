import pyautogui as p
import rpa as r
import webbrowser

p.alert("O código vai começar!!")

url = "https://github.com/"

webbrowser.register("chrome",
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get("chrome").open(url)

p.sleep(2)

close_translate = p.locateOnScreen('close_translate_button.png')

p.click(close_translate)

p.sleep(2)

acessar = p.locateCenterOnScreen('sign_up_button.png')
p.click(acessar)

p.sleep(2)

r.click('''//*[@id="login_field"]''')

p.sleep(1)

p.hotkey("ctrl", "a")
p.typewrite("jvoliveira2005@gmail.com")

p.sleep(1)

p.click(882, 419)

p.sleep(1)

p.hotkey("ctrl", "a")
p.typewrite("Caminhoneiro16!")

p.sleep(1)

p.click(888, 472)

p.sleep(3)

p.click(1841, 116)

p.sleep(1)

p.click(1693, 181)

p.sleep(3)

respositories = p.locateCenterOnScreen('repositories.png')
p.click(respositories)

p.sleep(1)

new_repositorie = p.locateCenterOnScreen('new.png')
p.click(new_repositorie)

p.sleep(1)

repo_name = p.locateCenterOnScreen('repository_name.png')
p.click(repo_name)
p.typewrite('Projeto Louco')
p.scroll(-900)

p.sleep(1)

p.click(557, 478)

p.sleep(1)

p.click(634, 873)

##############

p.sleep(5)

code = p.locateCenterOnScreen('code.png')
p.click(code)

copy = p.locateCenterOnScreen('copy.png')
p.click(copy)

p.click(568, 1047)

p.sleep(3)

p.rightClick(100, 236)

p.sleep(3)

p.click(x=181, y=384)

p.sleep(2)

p.typewrite(f"git clone ")
p.hotkey("ctrl", "v")
p.hotkey("enter")

p.sleep(2)

p.typewrite("cd Projeto-Louco")
p.hotkey("enter")
p.typewrite("code .")
p.hotkey("enter")

p.sleep(3)
p.click(1510, 87)

p.sleep(3)

p.rightClick(109, 141)

p.click(128, 159)

p.typewrite("main.py")

p.hotkey("enter")

p.sleep(2)

p.typewrite("print('Oi')")

p.click(1771, 55)

p.sleep(3)

p.alert("Acabou")

# p.sleep(4)
# print(p.position())