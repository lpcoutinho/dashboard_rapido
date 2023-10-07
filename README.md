# Dashboard rápido com Python e Streamlit

Essenciais para a visualização de dados e tomada de decisão. Dashboards permitem a visualizaçãp rápida e fácil de dados facilitando a identificação de tendências e padrões que podem ser usados para melhorar os negócios.

A construção de dashboards pode ser um processo demorado e caro, especialmente se você estiver usando uma ferramenta de BI tradicional. No entanto, com Python e Streamlit, podemos criar dashboards de maneira rápida e com maior facilidade, sem a necessidade de um conhecimento profundo de ferramentas de BI.

No mundo dos negócios, onde agilidade é a chave para o sucesso. As empresas precisam tomar decisões informadas em tempo real, acompanhar métricas importantes e comunicar resultados de maneira eficaz. E quando se trata de construir dashboards, o Python tem se tornado uma escolha popular entre os profissionais de análise de dados e desenvolvedores.

## Vantagens de usar Python para criar dashboards

Uma das maiores vantagens de optar pelo Python é a vasta quantidade de bibliotecas de análise de dados disponíveis, como Pandas, Matplotlib, Seaborn e muitas outras. Isso permite que você manipule, visualize e analise seus dados de maneira flexível e personalizada, atendendo às necessidades exclusivas da sua empresa.

Além disso, o Python é uma linguagem de programação de código aberto, o que significa que você não precisa se preocupar com custos de licença. Isso pode ser uma economia significativa, especialmente quando comparado a soluções proprietárias de Business Intelligence (BI).

## Velocidade na Entrega de Valor

A principal razão pela qual muitos profissionais optam por usar Python e Streamlit é a rapidez com que é possível criar dashboards funcionais. Com o Streamlit, você pode transformar seu código Python em um aplicativo web interativo em questão de minutos. Isso significa que você pode entregar valor aos seus stakeholders mais rapidamente, permitindo que eles tomem decisões mais informadas e reajam às mudanças de mercado em tempo real.

Em resumo, este tutorial xplorará como é possível criar dashboards de forma rápida e eficiente usando Python e Streamlit. Ao fazer isso, você estará equipado para tomar decisões mais informadas, comunicar dados de maneira eficaz e fornecer valor aos seus negócios de maneira mais rápida e econômica. Vamos começar a construir dashboards que farão a diferença!

## O Problema

Imagine-se trabalhando em uma rede de varejo, onde sua empresa lida diariamente com uma vasta quantidade de dados. Estes dados abrangem informações cruciais, como filiais, tipos de clientes, gênero, categoria de produtos, preços, quantidade de itens vendidos, taxas, datas de compra, horários das transações, etc.

Aqui, entra o desafio: seu chefe quer que você apresente um dashboard que forneça uma visão abrangente das operações da empresa. Especificamente, ele deseja informações detalhadas sobre o faturamento mensal e por unidade, o tipo de produto mais vendido e a contribuição financeira de cada filial, além de uma análise do desempenho dos métodos de pagamento e a avaliação média dada pelos clientes para cada filial.

Este é um problema comum que muitas empresas enfrentam hoje em dia: como transformar um mar de dados em informações acionáveis que possam impulsionar a tomada de decisões estratégicas. É um desafio que envolve coletar, processar e visualizar dados de maneira eficaz, permitindo que as partes interessadas obtenham insights cruciais para o sucesso do negócio.

Agora que compreendemos o desafio é hora de iniciar o processo de desenvolvimento. Passo a passo, vamos explorar as etapas para criar um dashboard eficaz. Inicialmente, abordaremos as configurações iniciais do projeto, garantindo que tudo esteja pronto para a construção. Em seguida, mergulharemos na manipulação de dados, trabalhando para garantir que as informações sejam organizadas de maneira adequada e útil. Por fim, nos concentraremos na criação de visualizações interativas que permitirão que você extraia insights valiosos a partir dos dados. Portanto, vamos começar!

## O Repositório

Navegue até o [repositório do projeto](https://github.com/lpcoutinho/dashboard_rapido) no GitHub para acessar todos os recursos relacionados a este tutorial. Lá, você encontrará o código-fonte, o arquivo de dados de exemplo e qualquer outra informação importante para o desenvolvimento do seu dashboard.

## Configurando o Ambiente

Para dar início ao projeto, estou utilizando uma máquina Ubuntu. Pensando na organização adequada e para garantir que todas as dependências sejam gerenciadas de forma isolada, começamos criando uma estrutura básica.

Criamos uma pasta dedicada para armazenar todos os arquivos relacionados ao projeto. Dentro dessa pasta, estabelecemos um ambiente virtual, uma prática recomendada em desenvolvimento Python, que nos permite isolar as bibliotecas e pacotes específicos deste projeto.

Aqui estão os comandos essenciais para criar e ativar o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

Isso nos permite manter um ambiente limpo e independente para o nosso projeto, garantindo que as dependências sejam gerenciadas de forma eficaz e evitando conflitos com outras aplicações ou projetos em execução em nossa máquina. Com essa base sólida, estamos prontos para prosseguir com a configuração e desenvolvimento do dashboard.

## Instalação das Bibliotecas

Agora que configuramos o ambiente e estamos prontos para avançar, o próximo passo importante é garantir que todas as bibliotecas e dependências necessárias estejam instaladas. Fundamental para garantir que nosso projeto funcione sem problemas.

Você pode utilizar o seguinte comando para instalar as bibliotecas essenciais para o nosso projeto:

```bash
pip install streamlit pandas plotly-express
```

Para simplificar esse processo, podemos usar o comando abaixo para instalar todas as bibliotecas listadas no arquivo `requirements.txt`, caso você tenha baixado o repositório do tutorial:

```bash
pip install -r requirements.txt
```

Essas bibliotecas são fundamentais para criar nosso dashboard de forma eficiente e interativa. O Streamlit é a ferramenta principal que utilizaremos para construir a interface, enquanto o Pandas e o Plotly Express nos ajudarão a manipular e visualizar os dados de maneira eficaz. Com as bibliotecas instaladas, estamos prontos para contiunar!

## Sobre as Ferramentas Utilizadas

Neste projeto, contamos com um conjunto poderoso de ferramentas que desempenham papéis fundamentais na criação do nosso dashboard. Vamos dar uma olhada mais detalhada em cada uma delas:

### Pandas: Sua Aliada na Manipulação de Dados

**Pandas** é uma biblioteca Python amplamente utilizada para manipulação e análise de dados. Com ele, podemos realizar tarefas essenciais, como importar, limpar, transformar e explorar nossos dados de forma eficiente. O Pandas fornece estruturas de dados flexíveis, como DataFrames e Series, que nos permitem organizar e analisar nossos dados de maneira intuitiva.

### Streamlit: Transformando Código em Aplicativos Web

**Streamlit** é uma ferramenta poderosa que nos permite transformar nosso código Python em aplicativos web interativos com facilidade. Com uma abordagem simples e orientada a scripts, o Streamlit permite que você crie interfaces de usuário atraentes e funcionais para seu projeto sem a necessidade de conhecimento avançado em web design. É a escolha perfeita para a criação rápida de dashboards interativos.

### Plotly Express: Visualizações Impactantes em Poucas Linhas de Código

**Plotly Express** é uma biblioteca de visualização que simplifica a criação de gráficos e visualizações de dados interativas. Com apenas algumas linhas de código, podemos criar gráficos atraentes que ajudam a comunicar insights de forma eficaz. O Plotly Express é especialmente útil quando desejamos enriquecer nosso dashboard com gráficos dinâmicos e informativos.

Cada uma dessas ferramentas desempenha um papel essencial na criação do nosso dashboard, e à medida que avançamos no projeto, você verá como elas se combinam para criar uma experiência de análise de dados eficaz e envolvente. Vamos explorar cada uma delas em detalhes ao longo deste tutorial para que você possa utilizá-las com confiança no desenvolvimento do seu próprio dashboard.

## Observando os dados

## Direto para a Construção do Dashboard

Neste tutorial, o foco principal é a construção do dashboard interativo. Como nosso objetivo não é aprofundar-se na análise exploratória dos dados, iremos pular esta etapa e seguir diretamente para a criação dos gráficos e da interface do dashboard.

No entanto, sempre que necessário e relevante, faremos menções sobre qualquer tratamento de informações ou insights importantes que possam surgir durante o desenvolvimento. A prioridade é guiar você na construção eficaz do dashboard, permitindo que você explore os dados de maneira interativa e eficiente.

## Importando Bibliotecas e Criando a Primeira Visualização

Para começar nosso projeto de dashboard, crie um arquivo chamado `dashboard.py` e adicione o código a seguir a ele:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar o layout da página
st.set_page_config(layout="wide")

# Carregar os dados do arquivo "vendas.csv" (certifique-se de que o arquivo está no mesmo diretório)
df = pd.read_csv("vendas.csv", sep=";", decimal=",")

# Exibir o DataFrame
st.write(df)
```

Execute o seguinte comando para iniciar o aplicativo do Streamlit e visualizar o dashboard:

```bash
streamlit run dashboard.py
```

O Streamlit irá abrir automaticamente o seu navegador padrão com o dashboard em execução. Você verá a tabela de dados carregada a partir do arquivo "vendas.csv" exibida na interface.

Esta é a nossa primeira visualização no dashboard. A partir deste ponto, iremos adicionar recursos de visualização interativos e personalizados para tornar o dashboard mais informativo e útil para análise de dados.

## Criando um Filtro de Seleção de Meses

Para criar um filtro de seleção de meses em nosso dashboard, precisamos realizar algumas etapas para garantir que os dados sejam tratados adequadamente. Vamos seguir as instruções a seguir:

```python
# Converter a coluna "Date" para o formato de data
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Criar uma nova coluna "Month" que contém o ano e o mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Criar uma seleção de meses na barra lateral do dashboard
month = st.sidebar.selectbox("Selecione o Mês", df["Month"].unique())

# Filtrar os dados com base no mês selecionado
df_filtered = df[df["Month"] == month]

# Exibir o DataFrame filtrado
st.write(df_filtered)
```

Agora, o código faz o seguinte:

1. Primeiro, convertemos a coluna "Date" para o formato de data usando `pd.to_datetime()`, garantindo que possamos trabalhar com datas de forma apropriada.

2. Em seguida, criamos uma nova coluna chamada "Month" que contém o ano e o mês da data correspondente. Isso nos permite agrupar os dados por mês mais facilmente.

3. Utilizamos `st.sidebar.selectbox()` para criar uma caixa de seleção na barra lateral do dashboard, permitindo que o usuário escolha o mês desejado a partir da lista de meses únicos presentes no DataFrame.

4. Filtramos os dados com base no mês selecionado pelo usuário, criando um novo DataFrame chamado `df_filtered` contendo apenas os dados correspondentes ao mês escolhido.

5. Finalmente, exibimos o DataFrame filtrado com `st.write()`, permitindo que o usuário veja os dados específicos do mês selecionado.

Agora, quando você executa o aplicativo do Streamlit usando `streamlit run dashboard.py`, você verá um filtro de seleção de meses na barra lateral do dashboard. Isso permite que você escolha o mês desejado para análise, tornando nosso dashboard mais interativo e personalizado. Continue acompanhando para adicionar mais recursos e funcionalidades ao projeto!

## Configurando o Layout

No Streamlit, você pode configurar o layout do seu dashboard usando colunas e linhas. Isso permite organizar e estruturar os elementos da interface do usuário de maneira eficiente.

Por exemplo, você pode dividir a tela em colunas e atribuir cada uma a uma variável para posterior preenchimento com elementos como gráficos, tabelas ou widgets interativos. No código abaixo, dividimos a tela em duas colunas, `col1` e `col2`, na primeira linha, e em três colunas, `col3`, `col4` e `col5`, na segunda linha:

```python
col1, col2 = st.columns(2)  # Primeira linha com duas colunas
col3, col4, col5 = st.columns(3)  # Segunda linha com três colunas
```

Isso facilita a organização e disposição dos elementos no seu dashboard, permitindo uma estrutura clara e personalizada para a apresentação de informações. Dessa forma, você pode criar interfaces de usuário mais atraentes e funcionais para suas análises de dados.

## Começando a Construir os Gráficos

Até este ponto, seu código deve estar assim:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar o layout da página
st.set_page_config(layout="wide")

# Carregar os dados do arquivo "vendas.csv" (certifique-se de que o arquivo está no mesmo diretório)
df = pd.read_csv("vendas.csv", sep=";", decimal=",")

# Converter a coluna "Date" para o formato de data
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Criar uma nova coluna "Month" que contém o ano e o mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Criar uma seleção de meses na barra lateral do dashboard
month = st.sidebar.selectbox("Mês", df["Month"].unique())
df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)  # Primeira linha com duas colunas
col3, col4, col5 = st.columns(3)  # Segunda linha com três colunas
```

Neste ponto, vamos remover a última linha do código e começar a construir os gráficos e elementos interativos que comporão nosso dashboard. Vamos explorar como criar visualizações impactantes e personalizadas para os dados do seu projeto. Continue acompanhando para ver como isso será feito!

## Faturamento por Dia

Vamos construir um gráfico que nos mostra o faturamento por dia. Útil para entender como as vendas variam ao longo do tempo e se há tendências ou padrões específicos.

Aqui está o código:

```python
# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")

# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)
```

Neste código:

- Usamos a biblioteca Plotly Express (`px.bar`) para criar um gráfico de barras que mostra o faturamento (`Total`) em relação à data (`Date`). Também adicionamos uma diferenciação de cores com base na cidade (`City`) para destacar os diferentes locais de vendas.

- Definimos um título para o gráfico usando `title`.

- Usamos `col1.plotly_chart()` para exibir o gráfico na primeira coluna do layout que configuramos anteriormente.

Agora, ao executar seu aplicativo Streamlit, você verá o gráfico de faturamento por dia na primeira coluna do dashboard.

## Faturamento por Tipo de Produto

Agora, vamos criar um gráfico que nos mostra o faturamento por tipo de produto. Isso nos ajudará a entender quais tipos de produtos estão gerando mais receita e se há variações significativas entre as cidades.

Aqui está o código para criar o gráfico de faturamento por tipo de produto:

```python
# Criar o gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")

# Exibir o gráfico na segunda coluna
col2.plotly_chart(fig_prod, use_container_width=True)
```

Neste código:

- Usamos a biblioteca Plotly Express (`px.bar`) para criar um gráfico de barras horizontal. O eixo x (`x="Date"`) representará as datas, o eixo y (`y="Product line"`) representará os tipos de produto e usamos a diferenciação de cores com base na cidade (`color="City"`) para destacar as diferentes localidades de vendas.

- Definimos um título para o gráfico usando `title`.

- Usamos `orientation="h"` para criar um gráfico de barras horizontal.

- Por fim, usamos `col2.plotly_chart()` para exibir o gráfico na segunda coluna do layout.

Agora, ao executar seu aplicativo Streamlit, você verá o gráfico de faturamento por tipo de produto na segunda coluna do dashboard. Isso proporciona uma visão valiosa da contribuição de diferentes tipos de produtos para o faturamento geral. Continue aprimorando seu dashboard adicionando mais gráficos e interatividade!

## Contribuição por Cidade

Vamos analisar a contribuição de cada cidade para o faturamento total. Isso nos ajudará a identificar quais cidades estão desempenhando um papel mais significativo em termos de receita.

Aqui está o código:

```python
# Calcular o faturamento total por cidade
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()

# Criar o gráfico de barras para exibir o faturamento por cidade
fig_city = px.bar(city_total, x="City", y="Total",
                   title="Faturamento por cidade")

# Exibir o gráfico na terceira coluna
col3.plotly_chart(fig_city, use_container_width=True)
```

Neste código:

- Começamos calculando o faturamento total por cidade usando `df_filtered.groupby("City")[["Total"]].sum().reset_index()`. Isso agrupa os dados por cidade e calcula a soma do faturamento para cada uma delas.

- Em seguida, criamos um gráfico de barras (`px.bar`) que mostra o faturamento por cidade. O eixo x (`x="City"`) representa as cidades, o eixo y (`y="Total"`) representa o faturamento e definimos um título para o gráfico.

- Por fim, usamos `col3.plotly_chart()` para exibir o gráfico na terceira coluna do layout.

Ao executar seu aplicativo Streamlit, você verá o gráfico de faturamento por cidade na terceira coluna do dashboard.

## Faturamento por Tipo de Pagamento

Agora, vamos explorar como o faturamento se distribui pelos diferentes métodos de pagamento. Isso nos ajudará a entender quais métodos de pagamento são mais populares entre os clientes e contribuem mais para a receita.

Aqui está o código para criar o gráfico de faturamento por tipo de pagamento:

```python
# Criar o gráfico de pizza para exibir o faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Faturamento por tipo de pagamento")

# Exibir o gráfico na quarta coluna
col4.plotly_chart(fig_kind, use_container_width=True)
```

Neste código:

- Usamos a biblioteca Plotly Express (`px.pie`) para criar um gráfico de pizza que mostra como o faturamento (`Total`) está distribuído entre os diferentes métodos de pagamento (`Payment`).

- Definimos um título para o gráfico usando `title`.

- Usamos `col4.plotly_chart()` para exibir o gráfico na quarta coluna do layout.

Ao executar seu aplicativo Streamlit, você verá o gráfico de faturamento por tipo de pagamento na quarta coluna do dashboard. Isso proporciona uma visão importante sobre as preferências de pagamento dos clientes e ajuda a identificar os métodos mais utilizados.

## Avaliação Média por Cidade

Agora, vamos explorar a avaliação média por cidade para entender como as diferentes localidades estão sendo avaliadas pelos clientes. Isso nos ajudará a identificar quais cidades têm a melhor classificação média.

Aqui está o código:

```python
# Calcular a avaliação média por cidade
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()

# Criar o gráfico de barras para exibir a avaliação média
fig_rating = px.bar(df_filtered, y="Rating", x="City",
                   title="Avaliação Média")

# Exibir o gráfico na quinta coluna
col5.plotly_chart(fig_rating, use_container_width=True)
```

Neste código:

- Calculamos a avaliação média por cidade usando `df_filtered.groupby("City")[["Rating"]].mean().reset_index()`. Isso agrupa os dados por cidade e calcula a média das avaliações para cada uma delas.

- Em seguida, criamos um gráfico de barras (`px.bar`) que mostra a avaliação média por cidade. O eixo y (`y="Rating"`) representa as avaliações, o eixo x (`x="City"`) representa as cidades e definimos um título para o gráfico.

- Usamos `col5.plotly_chart()` para exibir o gráfico na quinta coluna do layout.

Ao executar seu aplicativo Streamlit, você verá o gráfico de avaliação média por cidade na quinta coluna do dashboard.

## Conclusão

Neste tutorial, percorremos o processo de construção de um dashboard interativo de análise de dados usando Python e a biblioteca Streamlit. Ao longo do tutorial, exploramos várias visualizações, incluindo faturamento por dia, faturamento por tipo de produto, contribuição por filial, contribuição por cidade e faturamento por tipo de pagamento. Cada visualização ofereceu insights valiosos para a análise de dados da nossa empresa de varejo.

A construção de dashboards com Python apresenta inúmeras vantagens. A flexibilidade oferecida pela linguagem de programação Python permite customizações infinitas e a criação de dashboards totalmente adaptados às necessidades específicas do seu projeto. Além disso, Python é uma linguagem de programação amplamente usada na comunidade de análise de dados, o que significa que você pode aproveitar uma ampla gama de bibliotecas e ferramentas para aprimorar suas análises.

Você pode encontrar o código completo deste projeto no [repositório no GitHub](https://github.com/lpcoutinho/dashboard_rapido). Lá, você pode baixar o código-fonte, explorar os arquivos e experimentar o dashboard por conta própria.

Além disso, espero que você leia a documentação oficial das bibliotecas utilizadas neste projeto. Isso proporcionará um entendimento mais profundo das funcionalidades e possibilidades de customização que cada biblioteca oferece.

A construção de dashboards é uma habilidade valiosa para qualquer profissional de análise de dados e pode ser aplicada em uma variedade de cenários de negócios. Espero que este tutorial tenha lhe fornecido uma base para começar a criar seus próprios dashboards com Python. Continue explorando e aprimorando suas habilidades!

## Referências

[Streamlit](https://docs.streamlit.io/)
[Pandas](https://pandas.pydata.org/docs/index.html)
[Plotly Express in Python](https://plotly.com/python/plotly-express/)
[AsimovAcademy](https://www.youtube.com/watch?v=P6E_Kts9pxE&t=953s)
