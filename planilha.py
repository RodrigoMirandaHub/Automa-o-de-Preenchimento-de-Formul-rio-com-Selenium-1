from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time



# Lê os dados do Excel
df = pd.read_excel("civ_digital_simulado.xlsx").reset_index(drop=True)



# Abre o navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.implicitly_wait(2)

print("✅ Navegador aberto. Iniciando preenchimento...\n")

for i, row in df.iterrows():
    print(f"🔄 Preenchendo usuário {i+1}/{len(df)}...")

    # Preenche o formulário
    driver.find_element(By.NAME, "my-text").clear()
    driver.find_element(By.NAME, "my-text").send_keys(row["Nome"])

    driver.find_element(By.NAME, "my-password").clear()
    driver.find_element(By.NAME, "my-password").send_keys(str(row["Matricula"]))

    driver.find_element(By.NAME, "my-textarea").clear()
    driver.find_element(By.NAME, "my-textarea").send_keys(row["Observacoes"])

    # Clica no botão Submit
    driver.find_element(By.TAG_NAME, "button").click()

    # Aguarda a nova página carregar
    time.sleep(1)

    # Verifica se a página mudou e volta pro formulário
    if "Form submitted" in driver.page_source:
        print("✅ Formulário enviado! Voltando...")
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        time.sleep(2)
    else:
        print("⚠️ Não foi possível confirmar o envio do formulário.")

print("\n✅ Todos os usuários foram processados!")
input("Pressione Enter para fechar o navegador...")
driver.quit()
