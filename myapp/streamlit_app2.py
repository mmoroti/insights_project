import streamlit as st

readme_text = '''
Este é um projeto fictício usando dados disponíveis na plataforma [Kaggle](https://www.kaggle.com/).

Esses dados foram utilizados para conclusão da disciplina 'Do Zero ao DS em Python' da [Comunidade DS](https://www.linkedin.com/company/comunidade-ds/mycompany/). Aqui uso linguagem Python e minha expertise com análises estátisticas descritivas para solução de um problema de negócio de uma empresa chamada House rocket. 

## 1. Descrição

A House Rocket é uma empresa que atua no mercado imobiliário, efetuando a compra de imóveis que estejam com valor de venda abaixo de valor de mercado e que estejam em bom estado de conservação para a posterior revenda. O CEO da House Rocket recebeu uma planilha com dados de imóveis de Seattle que estão disponíveis para venda e chegou para a equipe de dados com duas questões centrais. 

- 1. Quais são os imóveis que a House Rocket deveria comprar?
- 2. Uma vez comprados os imóveis, qual o melhor momento para vendê-los e por qual preço?

O CEO também requisitou um site para acessar do seu celular os principais insights do negócio e um mapa para visualizar a localização dos imóveis. O projeto encontra-se em produção e pode ser acessado nesse [link](https://mmoroti-insights-project-house-rocket-app-xt9ns5.streamlit.app/). A entrega do projeto foi realizada usando o framework do Streamlit. Essa ferramenta possibilita a construção de um dashboard interativo disponível 24h online, facilitando o acesso as informações e a tomada de decisão pelo CEO.  
## 2. Atributos (features)
Os dados podem ser encontrados nesse [link](https://www.kaggle.com/code/lucascapovilla/house-rocket). Abaixo defino cada atributo presente no dataset:

| Coluna | Descrição |
| :----- | --------: |
| id | Identificador do imóvel |
| date | Data que o imóvel foi colocado a venda |
| price | Preço do imóvel |
| bedrooms | Número de quartos |
| bathrooms | Número de banheiros |
| sqft_living | Tamanho da área de estar |
| sqft_lot | Tamanho total do terreno |
| view | Preço da motocicleta sem as taxas de seguro e registro |
| condition | Condição do imóvel |
| sqft_basement | Tamanho do porão |
| yr_built | Ano de construção |
| yr_renovated | Ano da última reforma |
| zipcode | Localização |
| lat | Latitude |
| long | Longitude |

## 3. Premissas do Negócio 
- Existe no mercado imobiliário norte americano uma diferença de preço no valor de venda a depender da estação. Em geral, os meses com temperaturas mais altas são considerados "alta temporada", o que aumenta a demanda e consequentemente o preço. 
- Apenas imóveis que estejam em boas condições devem ser comprados (ou seja, 'condition > ou = 3)

## 4. Planejamento e estratégia de solução
- Removemos um imóvel com 33 quartos que provavelmente era um erro de digitação. Usei a lógica observando que o imóvel não tinha tamanho (sqft_lot) suficiente para ter 33 dormitórios quando comparado com outros imóveis com 8 dormitórios.
- Removemos os imóveis com 'ids' duplicados.
- Primeiro, vamos calcular a mediana do preço dos imóveis por 'zipcode'
- Os imóveis que possuírem valor de venda abaixo da mediana e em boa condição serão apontados como 'comprar'.
- Os imóveis que estiverem disponíveis para venda no verão ou na primavera, serão acrescidos 30% no valor de venda.
- Os imóveis que estiverem disponíveis para venda no inverno ou no outono, serão acrescidos 10% do no valor da venda.

## 5. Ferramentas
- Python 3.9.;
- IDE VsCode e Jupyter Notebook;
- Bibliotecas e pacotes Pandas, Numpy, Streamlit, Seaborn, Plotly, Matplotlib;
- Pipenv para gerenciar as dependências do projeto 
- Git e GitHub para versionamento e hospedagem dos códigos utilizados.
- Hospedado na Cloud do Streamlit

## 6. Insights e hipóteses de negócio
#### H1 - Imóveis que possuem vista para água são 20% mais caros? 
Verdadeiro. Imóveis com vista para a água são em média 20% mais caros.

#### H2 - Imóveis com data de construção menor que 1955, são 50% mais baratos na média?
Falso. Imóveis com data de construção menor que 1955 não são em média 50% mais baratos.

#### H3 - O crescimento do preço dos imóveis YoY (year over year) é de 10% ?
Falso. O valor dos imóveis oscila ao longo do tempo, com quedas e aumentos, e aumento em média apenas 0.01% ao longo do tempo.

#### H4 - O preço aumenta conforme o tamanho do imóvel aumenta? 
Falso. Outras variáveis como a localização devem ser mais importantes para explicar o valor dos imóveis.

#### H5 - O saldo positivo da venda, em média, é maior no inverno? 
Falso. Fazendo a média ponderada pelo número de imóveis e o balanço positivo, o saldo positivo é maior na primavera.

## 7. Conclusão

Um insight é que imóveis com vista para a água são 20% mais caros, portanto podem ser mais valorizados pelos compradores. Esse projeto foi elaborado usando apenas conhecimento de negócio, estátisticas descritivas e um dashboard interativo. O valor investido deve ser de $4.063.385.840,00 para aquisição de 10499 imóveis. O valor estimado de lucro para a House Rocket é de 741.903.965,20 dólares. 
 
A entrega foi feita através de uma planilha encaminhada direto no email do CEO, mas também pode ser acessada diretamente no [link](https://mmoroti-insights-project-house-rocket-app-xt9ns5.streamlit.app/). Aqui é possível usar o site para visualizar os imóveis com filtros interativos e também os principais insights e a resposta para as hipóteses de negócio elaboradas.

## 8. Próximos passos

- Incorporar as sugestões do time de dados e do CEO no próximo ciclo do projeto.
- Usar algum algoritmo de Machine Learning, como Random Forest, para classificar e sugerir o preço de revenda dos imóveis baseado nas características e na localização. 
'''
st.title("Projeto de insights House Rocket")
st.markdown(readme_text)

