# Clima_MMQ
Este trabalho ainda em desenvolvimento busca realizar a análise dados históricos da média de Concentração de CO2 na atmosfera em partes por milhão (ppm) e Anomalias de temperatura em três casos: Concentração de CO2 ao longo do tempo; Anomalias de Temperatura ao longo do tempo. Anomalias de temperatura em relação a concentração de CO2. Os dados para realizar a análise podem ser encontrados nas referências [8] e [9] respectivamente e foram coletados e preparados pela bilioteca pandas, de acordo com o Arquivo de formato jupyter notebook - Preparo dos dados.
O arquuivo MMQ_statsModel, realiza a aplicação do Métodos dos Mínimos Quadrados nos três casos a partir de diferentes funções de aproximação e debate os resultados. Para verificar a significância dos resultados, é levado em consideração a aplicação do teste t de student para os coeficientes, e o teste F para o modelo. Para a aplicação dos métodos foi utilizado a biblioteca statsmodels, enquanto que para tratar de algumas transformações necessárias aos dados foi utilizada a biblioteca numpy, com os gráficos sendo construídos a partir da biblioteca matplotlib.
As análises ainda estão a ser construídas.


Referência relevantes para o estudo:
[1] CORTESE, Tatiana Tucunduva P.; NATALINI, Gilberto. Mudanças Climáticas: Do Global ao Local. Barueri: Editora Manole, 2014. E-book. ISBN 9788520446607. Disponível em: https://app.minhabiblioteca.com.br/#/books/9788520446607/. Acesso em: 27 jul. 2024.

[2]SILVA, Cleyton Martins da; ARBILLA, Graciela. Emissões atmosféricas e mudanças climáticas. 1. ed. Rio de Janeiro: Freitas Bastos, 2022. E-book. Disponível em: https://plataforma.bvirtual.com.br. Acesso em: 24 jul. 2024.

[3] Neide B. Franco. Cálculo Numérico. Pearson Prentice Hall, São Paulo, 2006.

[4] Marcia A. G. Ruggiero e Vera L. R. Lopes. Cálculo numérico: aspectos teóricos e computacionais. Pearson Education do Brasil, São Paulo, 2a edição, 2013.

[5] S. Arenales e A. Darezzo. Cálculo Numérico: Aprendizado com apoio de software. ed. São Paulo: Cengage Learning, 2a edição 2015

[6] MORETTIN, Pedro A.; BUSSAB, Wilton de O. Estatística básica. São Paulo: SRV Editora LTDA, 2017. E-book. ISBN 9788547220228. Disponível em: https://app.minhabiblioteca.com.br/#/books/9788547220228/. Acesso em: 30 jul. 2024.

[7] MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, G. Geoffrey. Introduction to Linear Regression Analysis. 5. ed. Hoboken: Wiley, 2012.

[8] Climate at a Glance | Global Time Series | National Centers for Environmental Information (NCEI). Disponível em: < https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/0/1979-2024 >. Acesso em: 27 ago. 2024.

[9] Global Monitoring Laboratory – Carbon Cycle Greenhouse Gases. Disponível em: <gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.txt>. Acesso em: 27 ago. 2024.



