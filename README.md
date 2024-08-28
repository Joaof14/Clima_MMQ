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

As análises dos resultados ainda estão em desenvolvimento.

## Referência relevantes para o estudo:
[1] CORTESE, Tatiana Tucunduva P.; NATALINI, Gilberto. Mudanças Climáticas: Do Global ao Local. Barueri: Editora Manole, 2014. E-book. ISBN 9788520446607. Disponível em: https://app.minhabiblioteca.com.br/#/books/9788520446607/. Acesso em: 27 jul. 2024.

[2]SILVA, Cleyton Martins da; ARBILLA, Graciela. Emissões atmosféricas e mudanças climáticas. 1. ed. Rio de Janeiro: Freitas Bastos, 2022. E-book. Disponível em: https://plataforma.bvirtual.com.br. Acesso em: 24 jul. 2024.

[3] Neide B. Franco. Cálculo Numérico. Pearson Prentice Hall, São Paulo, 2006.

[4] Marcia A. G. Ruggiero e Vera L. R. Lopes. Cálculo numérico: aspectos teóricos e computacionais. Pearson Education do Brasil, São Paulo, 2a edição, 2013.

[5] S. Arenales e A. Darezzo. Cálculo Numérico: Aprendizado com apoio de software. ed. São Paulo: Cengage Learning, 2a edição 2015

[6] MORETTIN, Pedro A.; BUSSAB, Wilton de O. Estatística básica. São Paulo: SRV Editora LTDA, 2017. E-book. ISBN 9788547220228. Disponível em: https://app.minhabiblioteca.com.br/#/books/9788547220228/. Acesso em: 30 jul. 2024.

[7] MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, G. Geoffrey. Introduction to Linear Regression Analysis. 5. ed. Hoboken: Wiley, 2012.

[8] Climate at a Glance | Global Time Series | National Centers for Environmental Information (NCEI). Disponível em: < https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/0/1979-2024 >. Acesso em: 27 ago. 2024.

[9] Global Monitoring Laboratory – Carbon Cycle Greenhouse Gases. Disponível em: <gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.txt>. Acesso em: 27 ago. 2024.



