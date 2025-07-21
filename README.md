# Análise Visual de Dados de E-commerce (EBAC)

Este projeto foi desenvolvido para a plataforma **EBAC** (*Escola Britânica de Artes Criativas e Tecnologia*) e tem como foco  realizar uma **análise visual de dados de um e-commerce**, utilizando **Python** e bibliotecas especializadas como `matplotlib`, `seaborn` e `pandas`.

Os gráficos gerados facilitam a compreensão de métricas relevantes e padrões comerciais entre os produtos vendidos, com base no conjunto de dados `ecommerce_preparados.csv`.

---

## Fonte de Dados

Arquivo CSV: `ecommerce_preparados.csv`

Contém informações como:

- Marca  
- Temporada  
- Gênero  
- Preço  
- Desconto  
- Número de Avaliações  
- Nota  

---

## Visualizações Geradas

1. **Histogramas**
   - Distribuição de avaliações por marca (top 5)
   - Distribuição de avaliações por temporada

2. **Gráfico de Dispersão**
   - Relação entre preços e temporada dos produtos

3. **Mapa de Calor**
   - Correlações entre avaliações e notas dos produtos

4. **Gráfico de Barras**
   - Análise dos descontos por público-alvo: Feminino, Masculino e Infantil

5. **Gráfico de Pizza**
   - Distribuição de vendas por estação do ano

6. **Gráfico de Densidade**
   - Faixa de preços mais comuns entre os produtos disponíveis

7. **Gráfico de Regressão**
   - Relação estatística entre preço e desconto dos produtos

---

## ▶️ Como Executar

Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install pandas matplotlib seaborn
