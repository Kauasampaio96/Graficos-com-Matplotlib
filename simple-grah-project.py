
import matplotlib.pyplot as plt

meses = ['mar', 'abr', 'mai', 'jun', 'jul','ago','set', 'out', 'nov', 'dez']

consultas = [825, 1100, 1250, 830, 950, 778, 850, 989, 535, 749]
exames = [110, 323, 578 , 545, 780, 125, 569, 789, 452, 214]



plt.rcParams["figure.autolayout"] = True
plt.figure(1, figsize=(15,5))
   
plt.subplot(1,2,1)        
plt.plot(meses, consultas, color= 'blue')
plt.plot(meses, exames, color = 'red')
plt.axis([0, len(meses), 0, max(consultas)+ 300])
plt.axis('auto')
plt.title('Número de Consultas Posto de Saúde - Distrito Faveira - Mar/2020 a Dez/2020')
plt.suptitle('Dados ficitcios, usados apenas para fins de estudo.', fontsize = 10, color = 'blue')
plt.legend(['Consultas', 'Exames'])
plt.xlabel('Meses')
plt.ylabel('Consultas/ exames')
plt.text (0.25, 0.145, 'Houve falta de Especialistas para exames', fontsize = 5, transform=plt.gcf().transFigure)
plt.text (0.145, 0.845, 'Super Lotação', fontsize = 5, transform=plt.gcf().transFigure)


plt.subplot(1,2,2)           
plt.bar(meses, consultas, color= 'blue')
plt.plot(meses, exames, color = 'red')
plt.axis([0, len(meses), 0, max(consultas)+ 300])
plt.axis('auto')
plt.title('Número de Consultas Posto de Saúde - Distrito Faveira')
plt.suptitle('Dados ficitcios, usados apenas para fins de estudo.', fontsize = 10, color = 'blue')
plt.legend(['Consultas', 'Exames'])
plt.xlabel('Meses')
plt.ylabel('Consultas/ exames')

plt.show()
