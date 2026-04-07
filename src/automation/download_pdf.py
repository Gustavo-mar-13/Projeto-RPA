import os
import requests

# Configuração de pastas (Você já mestre nisso!)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_RAW = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "raw"))
os.makedirs(CAMINHO_RAW, exist_ok=True)

def salvar_pdf(url, nome_arquivo):
    caminho_final = os.path.join(CAMINHO_RAW, nome_arquivo)
    
    # DISFARCE: Dizemos ao site que somos um navegador Chrome no Windows
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    try:
        print(f"Tentando baixar: {nome_arquivo}...")
        # Passamos o disfarce aqui no 'headers'
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            with open(caminho_final, "wb") as f:
                f.write(response.content)
            print(f"✅ {nome_arquivo} salvo com sucesso!")
        else:
            print(f"❌ Falha no site: Status {response.status_code} (Bloqueio ou Link quebrado)")
            
    except Exception as e:
        print(f"⚠️ Erro de conexão: {e}")
if __name__ == "__main__":
    # Agora você pode baixar 1 ou 50 PDFs só aumentando essa lista
    meus_downloads = {
        "documento_teste.pdf": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "manual_ifam.pdf": "https://www.orimi.com/pdf-test.pdf" # Outro link de teste
    }

    for nome, link in meus_downloads.items():
        salvar_pdf(link, nome)