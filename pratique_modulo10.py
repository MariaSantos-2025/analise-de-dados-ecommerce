
#ANÁLISE DE DADOS DO ARQUIVO "ecommerce_preparados.csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Gráfico Histogramas marca e temporada
# Carregando os dados
df = pd.read_csv("ecommerce_preparados.csv")
print(df.head(10).to_string())

# Conferir se foi importado e o nome das colunas
#print(df.dtypes)

# Selecão as 5 marcas com mais produtos
marcas_top = df['Marca'].value_counts().nlargest(5).index
df_filtrado = df[df['Marca'].isin(marcas_top)]

# Histograma - Avaliações entre as marcas mais populares ao longo das estações do ano.
plt.figure(figsize=(8,4))
sns.histplot(data=df_filtrado, x='N_Avaliações', hue='Marca', bins=40, kde=True)
plt.title( 'Histograma - Distribuição de Avaliações por Marca')
plt.xlabel('Número de Avaliações')
plt.ylabel('Quantidade de Produtos')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma - Avaliações por Temporada ao longo das estações do ano
plt.figure(figsize=(8,4))
sns.histplot(data=df, x='N_Avaliações', hue='Temporada', bins=40, kde=True)
plt.title('Histograma - Distribuição de Avaliações por Temporada')
plt.xlabel('Número de Avaliações')
plt.ylabel('Quantidade de Produtos')
plt.grid(True)
plt.tight_layout()
plt.show()


#Gráfico de Dispersão - Identifica padrões de preço conforme a sazonalidade
#Carregando os dados
df = pd.read_csv("ecommerce_preparados.csv")
# Excluindo valores "não definidos" na coluna Temporada
# Caso o valor seja exatamente "não definido" como string
df = df[df['Temporada'] != 'não definido']

# Gráfico usando sns.stripplot
plt.figure(figsize=(10,6))
sns.stripplot(x='Preço', y='Temporada', data=df, jitter=True, alpha=0.8,
     hue='Temporada', palette='PiYG', size=6, legend=False)

plt.title('Dispersão - Análise de Preço por Temporada')
plt.xlabel('Preço do Produto')
plt.ylabel('Temporada')
plt.grid(True, axis='x')
plt.tight_layout()
plt.show()


#Mapa de Calor - Correlações entre Número de Avaliações e Notas'
# Carregando os dados
df = pd.read_csv("ecommerce_preparados.csv")
print(df.head(10).to_string())

# Excluindo valores "não definidos" na coluna Temporada
#Caso o valor seja exatamente "não definido" como string
df = df[df['Nota'].notna()]

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Spectral')
plt.title(' Mapa de Calor - Correlações entre Número de Avaliações e Notas')
plt.tight_layout()
plt.show()


#Gráfico de Barras - Descontos com base no público-alvo: Feminino, Masculino e Infantil.
# Carregando os dados
df = pd.read_csv("ecommerce_preparados.csv")
print(df.head(10).to_string())

# Filtrando gêneros válidos
df= df[df['Gênero'].isin(['Masculino', 'Feminino', 'infantil'])]

# Definindo ordem personalizada
order = ['Feminino', 'Masculino', 'infantil']

plt.figure(figsize=(14, 6))
sns.countplot(x='Desconto', hue='Gênero', hue_order=order,
data=df)
plt.title('Distribuição de descontos nos produtos vendidos por gênero: Masculino, Feminino e infantil')
plt.xlabel('Desconto - Produtos Vendidos')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de Pizza - Criando um dicionário para padronizar os valores
mapeamento_temporadas = {
    'não definido': 'Indefinido',
    'outono/inverno': 'Outono-Inverno',
    'outono-inverno': 'Outono-Inverno',
    'primavera/verão': 'Primavera-Verão',
    'primavera-verão': 'Primavera-Verão',
    'primavera/verão/outono/inverno': 'Todas as Estações',
    'primavera/verão outono/inverno': 'Todas as Estações',
    'primavera-verão outono-inverno': 'Todas as Estações',
    'primavera-verão - outono-inverno': 'Todas as Estações'
}
# Aplicando a substituição
df['Temporada'] = df['Temporada'].replace(mapeamento_temporadas)

# Removendo valores irrelevantes como "2021"
df = df[df['Temporada'] != '2021']

x= df['Temporada'].value_counts().index
y= df['Temporada'].value_counts().values

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title("Distribuição de Vendas por Estação do Ano")
plt.show()

#Gráfico de Densidade - Indica a faixa de preço mais comum entre os produtos disponíveis.
# Carregando os dados
df = pd.read_csv("ecommerce_preparados.csv")
print(df.head(10).to_string())

sns.kdeplot(df['Preço'], fill=True, color='Orange', alpha=0.5)
plt.title('Distribuição dos Preços dos Produtos')
plt.xlabel('Preço dos Produtos')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()


#Grafico de Regressão - Relação estatística entre o valor dos produtos e os descontos aplicados.
# Carregando os dados - Preço mais comum entre os produtos
df = pd.read_csv("ecommerce_preparados.csv")
print(df.head(10).to_string())

plt.figure(figsize=(8, 5))
sns.regplot(x='Preço', y='Desconto', data=df)
plt.title('Regressão - Preços vs Descontos')
plt.xlabel('Preço (R$)')
plt.ylabel('Desconto')
plt.tight_layout()
plt.show()






