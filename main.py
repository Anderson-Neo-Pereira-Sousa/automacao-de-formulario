#Aprendendo a usar selenium para automatizar o preenchimento de formulários
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

#Entrar no site
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(3)

#colocar email
email = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(2)
email.send_keys('admin@contabilidade.com.br')

#colocar senha
senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(2)
senha.send_keys('123456789')

#Clicar no botão entrar
entrar_botao = driver.find_element(By.XPATH,"//button[@id='Entrar']")
sleep(2)
entrar_botao.click()
sleep(3)

#extrair informações da planilha
empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina_empresas = empresas['dados empresas']

#preencher os campos com os dados da planilha
for linha in pagina_empresas.iter_rows(min_row=2, values_only=True):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionario, data_fundacao = linha

    driver.find_element(By.ID,"nomeEmpresa").send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID,"emailEmpresa").send_keys(email)
    sleep(1)
    driver.find_element(By.ID,"telefoneEmpresa").send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID,"enderecoEmpresa").send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID,"cnpj").send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID,"areaAtuacao").send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID,"numeroFuncionarios").send_keys(quantidade_de_funcionario)
    sleep(1)
    driver.find_element(By.ID,"dataFundacao").send_keys(data_fundacao)
    sleep(1)

    driver.find_element(By.ID,"Cadastrar").click()
    sleep(3)

    
