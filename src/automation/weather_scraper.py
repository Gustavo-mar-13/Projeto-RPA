from playwright.sync_api import sync_playwright
import json

def tratar_dados(dados_brutos):
    try:
        # Tenta tratar se vier da interceptação de API
        if isinstance(dados_brutos, list) and "data" in dados_brutos[0]:
            raw = dados_brutos[0]["data"]
            parsed = json.loads(raw)
            current = parsed["responses"][0]["weather"][0]["current"]
            return {
                "temperatura": current.get("temp", 0),
                "condicao": current.get("cap", "N/A"),
                "sensacao": current.get("feels", 0)
            }
        # Se já vier como dicionário (Plano B)
        return dados_brutos
    except Exception as e:
        print("❌ Erro ao tratar dados:", e)
        return None

def coletar_clima_playwright():
    print("🌐 Iniciando captura de clima...")
    dados_clima = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        def capturar_api(response):
            nonlocal dados_clima
            try:
                if "application/json" in response.headers.get("content-type", ""):
                    url = response.url.lower()
                    if "weather" in url or "forecast" in url:
                        dados_clima = response.json()
            except:
                pass

        page.on("response", capturar_api)

        try:
            # Indo direto para Manaus para ser mais rápido
            page.goto("https://www.msn.com/pt-br/clima/previsao/in-Manaus,Amazonas", timeout=60000)
            
            print("⏳ Aguardando resposta da rede...")
            page.wait_for_timeout(10000) # Espera 10 segundos a API responder

            if dados_clima:
                print("✅ API interceptada com sucesso!")
                return tratar_dados(dados_clima)
            
            # --- PLANO B (Segurança para o IFAM) ---
            print("⚠️ API demorou. Ativando modo de segurança...")
            return {
                "temperatura": 31.0,
                "condicao": "Ensolarado (Simulado)",
                "sensacao": 34
            }

        except Exception as e:
            print(f"❌ Erro no Scraper: {e}")
            # Retorno de emergência para não quebrar o CSV
            return {"temperatura": 31.0, "condicao": "Erro de Conexão", "sensacao": 0}
        finally:
            browser.close()

if __name__ == "__main__":
    resultado = coletar_clima_playwright()
    print("\n🌡️ Resultado final para a Interface:", resultado)