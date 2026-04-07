# 🤖 RPA - Automação de Coleta e Processamento de Dados Climáticos

## 📌 Sobre o Projeto

Este projeto é uma automação (RPA) desenvolvida em Python com o objetivo de coletar, processar e organizar dados climáticos de forma automática.

Ele integra **consumo de API + web scraping + processamento de dados**, criando um fluxo completo de coleta até a geração de informações tratadas.

---

## 🚀 Funcionalidades

* 🌐 Coleta de dados climáticos via API
* 🤖 Web scraping automatizado (Playwright)
* 📄 Download automatizado de arquivos (PDF)
* 🔄 Processamento e análise de dados
* 🖥️ Interface simples para execução do sistema
* 📊 Organização de dados em formato estruturado

---

## 🧠 Como o sistema funciona

Fluxo do projeto:

Usuário → Interface → Coleta de Dados → Processamento → Armazenamento

1. O usuário inicia o sistema pela interface
2. O robô coleta dados via API e scraping
3. Os dados são tratados e analisados
4. Os resultados são organizados e armazenados

---

## 🛠️ Tecnologias utilizadas

* Python 3.x
* Playwright
* Requests
* Pandas
* JSON

---

## 📁 Estrutura do Projeto

```
src/
 ├── automation/
 │    ├── data_collection/
 │    │    └── weather_api.py
 │    ├── analysis/
 │    │    └── analyze_data.py
 │    ├── weather_scraper.py
 │    ├── processar_dados.py
 │    ├── download_pdf.py
 │    └── main_loop.py
 └── interface.py
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```
git clone https://github.com/Gustavo-mar-13/Projeto-RPA.git
cd Projeto-RPA
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Execute o sistema

```
python src/interface.py
```

---

## 📊 Possíveis aplicações

* Monitoramento climático automatizado
* Coleta de dados para análise estatística
* Automação de tarefas repetitivas (RPA)
* Base para sistemas mais complexos de análise de dados

---

## 🔮 Melhorias futuras

* Dashboard visual para exibição dos dados
* Integração com banco de dados
* Agendamento automático (cron jobs)
* Deploy em ambiente cloud
* Logs estruturados e monitoramento

---

## 👨‍💻 Autor

Desenvolvido por **Gustavo Martins Luz**

---

## 📌 Observações

Este projeto foi desenvolvido com foco em aprendizado prático de:

* Automação (RPA)
* Web scraping
* Organização de código
* Estruturação de projetos reais

---

# 💡 Consideração final

Este projeto representa não apenas um script, mas um **fluxo automatizado completo**, demonstrando capacidade de integrar múltiplas tecnologias em uma solução funcional.
