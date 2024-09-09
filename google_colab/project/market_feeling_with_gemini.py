## Article: [Using the Gemini Pro from Google to analyse the Stock Market Feeling](https://softwarelivre-br.aomega.com.br/index.php/2023/12/16/usando-o-gemini-pro-da-google-para-analisar-o-sentimento-do-mercado-de-acoes/)

## Importing Libraries
"""

import pathlib
import textwrap
import google.generativeai as genai

"""## Importing my user enviroment variables"""

from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown

"""## Converting .txt to Markdown"""

def to_markdown(text):
  text = text.replace("•", "*")
  return Markdown(textwrap.indent(text, ">", predicate = lambda _:True))

"""## Recover the google_apy_key user variable"""

google_api_key = "AIzaSyD-uhcMqDBhAEVCGFBftBr5jATyixdPhyE"

genai.configure(api_key = google_api_key)

# google_api_key = userdata.get(google_api_key)

# Caso deseja listar todos os modelos de IA generativa disponíveis pode utilizar
# o seguinte trecho de código, dentro do FOR, caso contrário, não precisa.

#for m in genai.list_models():
#  if generateContent in m.supported_generation_methods:
#    print(m.name)

"""## Selecting the Gernerative AI to be used, in this case, the Gemini-Pro"""

model = genai.GenerativeModel("gemini-pro")

# O gemini-pro não trabalha com textos multimodais mas existe a opção de trabalhar
# com o recurso de embeddings que permitiria quebrar esta restrição do gemini-pro.
# Neste exemplo para manter a coisa simples coloquei todo o string de texto numa
# linha só, desta forma driblo a restrição do texto não ser multimodal e mantenho
# o exemplo simples. Claro que para textos maiores o recurso de embeddings é a
# única alternativa possível

"""## Bulding the Requested Prompt"""

meu_promt = "Qual o sentimento do mercado em relação às ações da Petrobras com base nas seguintes informações? Petrobras (PETR4) paga hoje 2a parcela de R$ 15. Petrobras desiste da venda de suas ações da Usina Elétrica a Gás de Araucária. Petrobras (PETR4): ações fecham em alta em dia de pregão volátil, As ações preferenciais da Petrobras (PETR4) subiram 0,23% nesta sexta-feira (15/12/2023), cotadas a R$ 35,40. O Ibovespa, por sua vez, recuou 0,49%, aos 130.197,10 pontos. Petróleo fecha em baixa, com dólar impulsionando a sessão. Perspectivas sobre o relaxamento monetário nas principais economias ajudaram a conter a queda hoje (15/12/2023). Os contratos futuros de petróleo fecharam com modestas perdas nesta sexta-feira (15/12/2023), em correção após os ganhos das duas últimas sessões, mas de forma insuficiente para impedir uma valorização semanal. Dados mistos e a recuperação do dólar amplificaram a pressão, embora perspectivas por relaxamento monetário nas principais economias ajudem a conter queda."

"""## Show the Analysis Results"""

response = model.generate_content(meu_prompt)
print(response.text)

# Não foi necessário o uso da função criada anteriormente, to_markdown,
# ela gerou um texto com formatação falha. A instrução response.text
# já foi suficiente para gerar um texto legível.

"""## All code Structured"""

import pathlib
import textwrap
import google.generativeai as genai

from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace("•", "*")
  return Markdown(textwrap.indent(text, ">" , predicate=lambda _: True))

google_api_key = "AIzaSyD-uhcMqDBhAEVCGFBftBr5jATyixdPhyE"

genai.configure(api_key=google_api_key)


# google_api_key=userdata.get("google_api_key")

# Caso deseje listar todos os modelos de IA generativa disponíveis pode utilizar
# o seguinte trecho de código, dentro do FOR, caso contrário, não precisa.

#for m in genai.list_models():
#  if generateContent in m.supported_generation_methods:
#    print(m.name)

model = genai.GenerativeModel("gemini-pro")

meu_prompt = "Qual o sentimento do mercado em relação às ações da Petrobras com base nas seguintes informações? Petrobras (PETR4) paga hoje 2a parcela de R$ 15. Petrobras desiste da venda de suas ações da Usina Elétrica a Gás de Araucária. Petrobras (PETR4): ações fecham em alta em dia de pregão volátil, As ações preferenciais da Petrobras (PETR4) subiram 0,23% nesta sexta-feira (15/12/2023), cotadas a R$ 35,40. O Ibovespa, por sua vez, recuou 0,49%, aos 130.197,10 pontos. Petróleo fecha em baixa, com dólar impulsionando a sessão. Perspectivas sobre o relaxamento monetário nas principais economias ajudaram a conter a queda hoje (15/12/2023). Os contratos futuros de petróleo fecharam com modestas perdas nesta sexta-feira (15/12/2023), em correção após os ganhos das duas últimas sessões, mas de forma insuficiente para impedir uma valorização semanal. Dados mistos e a recuperação do dólar amplificaram a pressão, embora perspectivas por relaxamento monetário nas principais economias ajudem a conter queda."

response = model.generate_content(meu_prompt)
print(response.text)