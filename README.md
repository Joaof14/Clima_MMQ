# Clima_MMQ

Este projeto em desenvolvimento busca analisar dados históricos da média de Concentração de CO2 na atmosfera (em partes por milhão - ppm) e Anomalias de Temperatura em três cenários:
1. Concentração de CO2 ao longo do tempo.
2. Anomalias de Temperatura ao longo do tempo.
3. Anomalias de Temperatura em relação à Concentração de CO2.

## Dados

Os dados utilizados para a análise podem ser encontrados nas referências [8] e [9]. Eles foram coletados e preparados utilizando a biblioteca `pandas`, conforme descrito no arquivo Jupyter Notebook - Preparo dos Dados.

## Metodologia

O arquivo `MMQ_statsModel` aplica o Método dos Mínimos Quadrados (MMQ) nos três cenários mencionados, utilizando diferentes funções de aproximação e discutindo os resultados. Para verificar a significância dos resultados, são aplicados:
- Teste t de Student para os coeficientes.
- Teste F para o modelo.

## Ferramentas Utilizadas

- **Bibliotecas**: `statsmodels` para os modelos estatísticos, `numpy` para transformações de dados e `matplotlib` para visualizações gráficas.

## Status

As análises dos resultados ainda estão em desenvolvimento, sendo desenvolvidas nessa branch.



