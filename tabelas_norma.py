#Dados dos cabos: Primeira Coluna -> Seção transversal do cabo
#                 Segunda Coluna -> Resistência Sequência Positiva
#                 Terceira Coluna -> Reatância Sequência Positiva
#                 Quarta Coluna -> Resistência Sequência Zero
#                 Quinta Coluna -> Reatância Sequência Zero       
dados_cabo = [[1.5,	14.8137, 0.1378, 16.6137, 2.9262],
              [2.5,	8.8882,	0.1345,	10.6882, 2.8755],
              [4,	5.5518,	0.1279,	7.3552,	2.8349],
              [6,	3.7035,	0.1225,	5.5035,	2.8000],
              [10,	2.2221,	0.1207,	4.0222,	2.7639],
              [16,	1.3899,	0.1173,	3.1890,	2.7173],
              [25,	0.8891,	0.1164,	2.6891,	2.6692],
              [35,	0.6353,	0.1128,	2.4355,	2.6382],
              [50,	0.4450,	0.1127,	2.2450,	2.5991],
              [70,	0.3184,	0.1096,	2.1184,	2.5681],
              [95,	0.2352,	0.1090,	2.0352,	2.5325],
              [120,	0.1868,	0.1076,	1.9868,	2.5104],
              [150,	0.1502,	0.1074,	1.9502,	2.4843],
              [185,	0.1226,	0.1073,	1.9226,	2.4594],
              [240,	0.0958,	0.1070,	1.8958,	2.4312],
              [300,	0.0781,	0.1068,	1.8781,	2.4067],
              [400,	0.0608,	0.1058,	1.8608,	2.3757],
              [500,	0.0507,	0.1051,	1.8550,	2.3491],
              [630,	0.0292,	0.1042,	1.8376,	2.3001]]

#Dados de correção da temp. ambiente: Primeira Coluna -> Temperatura ambiente °C
#                                     Segunda Coluna -> Fator de correção para cabo com isolação PVC
#                                     Terceira Coluna -> Fator de correção para cabo com isolação EPR ou XLPE
correcao_temperatura_ambiente = [[10, 1.22, 1.15],
                                 [15, 1.17, 1.12],
                                 [20, 1.12, 1.08],
                                 [25, 1.06, 1.04],
                                 [35, 0.94, 0.96],
                                 [40, 0.87, 0.91],
                                 [45, 0.79, 0.87],
                                 [50, 0.71, 0.82],
                                 [55, 0.61, 0.76],
                                 [60, 0.50, 0.71],
                                 [65, 0, 0.65],
                                 [70, 0, 0.58],
                                 [75, 0, 0.50],
                                 [80, 0, 0.41]]

#Dados de correção da temp. do solo: Primeira Coluna -> Temperatura ambiente °C
#                                    Segunda Coluna -> Fator de correção para cabo com isolação PVC
#                                    Terceira Coluna -> Fator de correção para cabo com isolação EPR ou XLPE
correcao_temperatura_solo = [[10, 1.10, 1.07],
                             [15, 1.05, 1.04],
                             [25, 0.95, 0.96],
                             [30, 0.89, 0.93],
                             [35, 0.84, 0.89],
                             [40, 0.77, 0.85],
                             [45, 0.71, 0.80],
                             [50, 0.63, 0.76],
                             [55, 0.55, 0.71],
                             [60, 0.45, 0.65],
                             [65, 0, 0.60],
                             [70, 0, 0.53],
                             [75, 0, 0.46],
                             [80, 0, 0.38]]
