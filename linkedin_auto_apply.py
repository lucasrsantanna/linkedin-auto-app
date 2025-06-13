# linkedin_auto_apply.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    print("Iniciando bot do LinkedIn...")

    # Configuração do Chrome
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--incognito")  # opcional para segurança

    # Inicializando driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Acessa a página de login do LinkedIn
        driver.get("https://www.linkedin.com/login")
        print("Por favor, faça o login manualmente no navegador aberto.")
        input("Após concluir o login, pressione ENTER aqui no terminal para continuar...")

        # Vai para a página de vagas
        driver.get("https://www.linkedin.com/jobs/search/?keywords=python")
        print("Página de vagas carregada.")

        time.sleep(5)

        # Clica na primeira vaga
        vaga_element = driver.find_element(By.CSS_SELECTOR, ".job-card-container__link")
        vaga_element.click()
        print("Primeira vaga clicada.")

        time.sleep(5)

        # Aguarda e captura a descrição da vaga com WebDriverWait
        try:
            descricao_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-description-content__text"))
            )
            descricao_vaga = descricao_element.text
            print(f"\nDescrição da vaga:\n{descricao_vaga[:1000]}...\n")  # Mostra até 1000 caracteres

        except Exception as e:
            print(f"Erro ao tentar capturar a descrição da vaga: {e}")

        print("Bot finalizado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro geral: {e}")

    finally:
        # PAUSA para você inspecionar manualmente se quiser
        input("🛑 Inspecione o navegador. Pressione ENTER aqui no terminal quando terminar...")
        driver.quit()
        print("Navegador fechado.")

if __name__ == "__main__":
    main()
