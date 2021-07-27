from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

f = open(r".\username.txt", 'r', encoding='utf8')
pw = f.readlines()

class ttBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r".\geckodriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://twitter.com/login')
        sleep(3)
        usuario = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        usuario.click()
        usuario.send_keys(self.username)
        senha = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        senha.click()
        senha.send_keys(self.password)
        senha.send_keys(Keys.RETURN)
        sleep(5)
        f.close()

    def post(self):
        driver = self.driver
        f = open(r".\palavras.txt", 'r', encoding="utf8")
        words = f.readlines()
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
        sleep(2)
        cx_txt = driver.find_element_by_class_name('notranslate')
        cx_txt.send_keys(random.choice(words))
        sleep(2)
        cx_txt.send_keys(Keys.CONTROL, Keys.RETURN)
        sleep(5)

    def delete(self):
        driver = self.driver
        driver.find_element_by_link_text("Profile").click()
        sleep(5)
        more_button = driver.find_element_by_css_selector('[aria-label="More"]')
        more_button.click()
        sleep(3)
        return_key = driver.find_element_by_tag_name('body')
        return_key.send_keys(Keys.RETURN)
        sleep(3)
        return_key.send_keys(Keys.RETURN)

opcao = int(input("1 para postar e 2 para deletar: "))
if opcao == 1:
    print("\nAbrindo o navegador ...")
    ttBot(pw[0], pw[1]).post()
elif opcao == 2:
    print("\nAbrindo o navegador ...")
    ttBot(pw[0], pw[1]).delete()
