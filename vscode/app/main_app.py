# Importando as bibliotecas
import pathlib
import textwrap
import google.generativeai as genai # pip install google-generativeai

# Importando as variáveis de ambiente do usuário
from IPython.display import display # pip install ipython
from IPython.display import Markdown

# Converting .txt to Markdown
def to_markdown(text):
  text = text.replace("•", "*")
  return Markdown(textwrap.indent(text, ">", predicate = lambda _:True))

# Recovering the google_api_key user variable
google_api_key = "AIzaSyD-uhcMqDBhAEVCGFBftBr5jATyixdPhyE"

genai.configure(api_key = google_api_key)

# Selecting the Generative AI to be Used, in this case, the Gemini Pro
model = genai.GenerativeModel("gemini-pro")

# Building the Requested Prompt
meu_prompt = "Qual o sentimento do mercado em relação às ações da Petrobras com base nas seguintes informações? Petrobras (PETR4) paga hoje 2a parcela de R$ 15. Petrobras desiste da venda de suas ações da Usina Elétrica a Gás de Araucária. Petrobras (PETR4): ações fecham em alta em dia de pregão volátil, As ações preferenciais da Petrobras (PETR4) subiram 0,23% nesta sexta-feira (15/12/2023), cotadas a R$ 35,40. O Ibovespa, por sua vez, recuou 0,49%, aos 130.197,10 pontos. Petróleo fecha em baixa, com dólar impulsionando a sessão. Perspectivas sobre o relaxamento monetário nas principais economias ajudaram a conter a queda hoje (15/12/2023). Os contratos futuros de petróleo fecharam com modestas perdas nesta sexta-feira (15/12/2023), em correção após os ganhos das duas últimas sessões, mas de forma insuficiente para impedir uma valorização semanal. Dados mistos e a recuperação do dólar amplificaram a pressão, embora perspectivas por relaxamento monetário nas principais economias ajudem a conter queda."

# Show the Analysis Result
response = model.generate_content(meu_prompt)
print(response.text)