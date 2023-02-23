import pyautogui as p
import webbrowser
import rpa

url= "https://externo.proway.com.br/login-aluno"

p.alert("O código está começando!")

webbrowser.register("chrome",
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get("chrome").open(url)

p.sleep(2)
acessar = p.locateCenterOnScreen('acessar.png')
p.click(acessar)
p.sleep(2)
avaliar = p.locateCenterOnScreen('avaliar.png')
p.click(avaliar)

# p.sleep(2)
# p.moveTo(x=762, y=1043)
# p.click(x=762, y=1043)
# p.moveTo(x=1006, y=70)
# p.click(x=1006, y=70)
# p.typewrite("https://externo.proway.com.br/login-aluno")
# p.hotkey('enter')
# p.sleep(2)
# p.moveTo(x=866, y=776)
# p.click(x=866, y=776)
# p.click(x=866, y=776)
# p.moveTo(x=1755, y=362)
# p.click(x=1755, y=362)
p.sleep(1)
p.click(x=1085, y=383)
p.click(x=1106, y=582)
p.click(x=1068, y=743)
p.click(x=1082, y=854)
p.scroll(-1000)
p.click(x=1080, y=360)
p.click(x=1076, y=506)
p.click(x=1078, y=640)
p.click(x=815, y=790)
p.typewrite("Aula massa!")
p.click(x=1154, y=961)
