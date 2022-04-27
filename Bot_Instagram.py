from selenium import webdriver
import time
navegador = webdriver.Chrome('chromedriver.exe')

#entrar no site do instragram
navegador.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

#preencher o nome e a senha do login
usuario = navegador.find_element_by_name('username')
usuario.send_keys('---') #coloque seu login
time.sleep(0.5)
senha = navegador.find_element_by_name('password')
senha.send_keys('---')  #coloque sua senha
time.sleep(2)

#pressionar o botão de login
Button_login = navegador.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[3]/button/div')
Button_login.click()
time.sleep(3)

#não salvar senha parte 1 para contas novas - se a conta for antiga desative esse comando!
agora_nao_contaNova = navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)

#não salvar a senha - esse aparece padrão mesmo se for antiga ou nova a conta 
agora_nao = navegador.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
time.sleep(3)

#clickar na aba de pesquisa e digitar 
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div/span').click()
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('#onepice')
time.sleep(1)
#pegar na lista de pesquisa o nome
navegador.find_element_by_class_name('-qQT3').click()
time.sleep(4)

#seguir a conta
seguir = navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/button').click()
time.sleep(2)