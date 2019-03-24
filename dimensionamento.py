#Importação dos outros arquivos
import dados
import tabelas_norma

#Cálculo dos critérios
#Critério da Capacidade de Condução de Corrente

    #Preciso acessar esses dados na tabela!!!
if dados.environmental_temperature == 40:
    temperature_factor = 0.91
        
soil_resistivity_factor=1
sizing_current=(dados.rated_current*dados.overload_factor)/(temperature_factor*dados.grouping_factor*soil_resistivity_factor)

#Critério da Queda de Tensão

#Critério da Capacidade de Corrente de Curto-Circuito

print (sizing_current)
#wb.save('dimensionamento.xlsx')