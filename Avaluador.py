# -*- coding: utf-8 -*-

#Metadata Social Event Classification: AVALUADOR
#Sergi Diaz, Iker Elorza, Ferran Monfort, Jordi Aguilar

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import time
import datetime

timer = time.time()

#Arxiu de resultats provinents del classificador
class_result = pd.read_csv('C:\Users\Acer\Desktop\Projecte\Metadades\Resultats_Definitius.txt', sep=' ') #delimitat per espais

#Ground truth
sol_train  = pd.read_csv('C:\Users\Acer\Desktop\Projecte\Metadades\sol_2.txt', sep=' ')

#[+certs, +fals, -fals, -cert]
concert =   np.zeros(4,float)
conference =np.zeros(4,float)
exhibition =np.zeros(4,float)
fashion =   np.zeros(4,float)
non_event = np.zeros(4,float)
other =     np.zeros(4,float)
protest =   np.zeros(4,float) 
sports =    np.zeros(4,float)
the_dance = np.zeros(4,float) 

i = 0
j = 0

len_class = len (class_result)
len_solut = len (sol_train)

#------------------------------MATRIU DE CONFUSIO PER A CADA EVENT

while (i < len_class):
    j = 0
    while (j < len_solut):
        if (class_result.document_id[i] == sol_train.document_id[j]): 
            if (class_result.event_type[i] == sol_train.event_type[j]): 
                #incrementar positius certs de l'event
                if (class_result.event_type[i] == "concert"):     concert[0] += 1.0
                elif (class_result.event_type[i] == "conference"):  conference[0] += 1.0
                elif (class_result.event_type[i] == "exhibition"):  exhibition[0] += 1.0
                elif (class_result.event_type[i] == "fashion"):     fashion[0] += 1.0
                elif (class_result.event_type[i] == "non_event"):   non_event[0] += 1.0
                elif (class_result.event_type[i] == "other"):       other[0] += 1.0
                elif (class_result.event_type[i] == "protest"):     protest[0] += 1.0
                elif (class_result.event_type[i] == "sports"):       sports[0] += 1.0
                elif (class_result.event_type[i] == "theater_dance"):   the_dance[0] += 1.0
    
                #incrementar el negatius certs de la resta d'events
                if (class_result.event_type[i] != "concert"):     concert[3] += 1.0
                if (class_result.event_type[i] != "conference"):  conference[3] += 1.0
                if (class_result.event_type[i] != "exhibition"):  exhibition[3] += 1.0
                if (class_result.event_type[i] != "fashion"):     fashion[3] += 1.0
                if (class_result.event_type[i] != "non_event"):   non_event[3] += 1.0
                if (class_result.event_type[i] != "other"):       other[3] += 1.0
                if (class_result.event_type[i] != "protest"):     protest[3] += 1.0
                if (class_result.event_type[i] != "sports"):       sports[3] += 1.0
                if (class_result.event_type[i] != "theater_dance"):   the_dance[3] += 1.0 
                
            else:
                #incrementar positiu fals de la primera classe
                if (class_result.event_type[i] == "concert"):     concert[1] += 1.0
                elif (class_result.event_type[i] == "conference"):  conference[1] += 1.0
                elif (class_result.event_type[i] == "exhibition"):  exhibition[1] += 1.0
                elif (class_result.event_type[i] == "fashion"):     fashion[1] += 1.0
                elif (class_result.event_type[i] == "non_event"):   non_event[1] += 1.0
                elif (class_result.event_type[i] == "other"):       other[1] += 1.0
                elif (class_result.event_type[i] == "protest"):     protest[1] += 1.0
                elif (class_result.event_type[i] == "sports"):       sports[1] += 1.0
                elif (class_result.event_type[i] == "theater_dance"):   the_dance[1] += 1.0 
                
                #incrementar el negatius fals de l'altre event
                if (sol_train.event_type[j] == "concert"):     concert[2] += 1.0
                elif (sol_train.event_type[j] == "conference"):  conference[2] += 1.0
                elif (sol_train.event_type[j] == "exhibition"):  exhibition[2] += 1.0
                elif (sol_train.event_type[j] == "fashion"):     fashion[2] += 1.0
                elif (sol_train.event_type[j] == "non_event"):   non_event[2] += 1.0
                elif (sol_train.event_type[j] == "other"):       other[2] += 1.0
                elif (sol_train.event_type[j] == "protest"):     protest[2] += 1.0
                elif (sol_train.event_type[j] == "sports"):       sports[2] += 1.0
                elif (sol_train.event_type[j] == "theater_dance"):   the_dance[2] += 1.0
                
                #incrementar el negatius certs de la resta d'events
                if (class_result.event_type[i] != "concert" or sol_train.event_type[j] != "concert" ):              concert[3] += 1.0
                if (class_result.event_type[i] != "conference"or sol_train.event_type[j] != "conference"):          conference[3] += 1.0
                if (class_result.event_type[i] != "exhibition"or sol_train.event_type[j] != "exhibition"):          exhibition[3] += 1.0
                if (class_result.event_type[i] != "fashion"or sol_train.event_type[j] != "fashion"):                fashion[3] += 1.0
                if (class_result.event_type[i] != "non_event"or sol_train.event_type[j] != "non_event"):            non_event[3] += 1.0
                if (class_result.event_type[i] != "other"or sol_train.event_type[j] != "other"):                    other[3] += 1.0
                if (class_result.event_type[i] != "protest"or sol_train.event_type[j] != "protest"):                protest[3] += 1.0
                if (class_result.event_type[i] != "sports"or sol_train.event_type[j] != "sports"):                  sports[3] += 1.0
                if (class_result.event_type[i] != "theater_dance" or sol_train.event_type[j] != "theater_dance"):   the_dance[3] += 1.0 
            break;
        j=j+1
    i=i+1          



#---------------------- PRECISIO, Record, F1score, AVG precision

precisio = np.zeros(9,float)
record = np.zeros(9,float)
f1score = np.zeros(9,float)
avg = np.zeros(3,float)

#PRECISIO
precisio[0] = concert[0]/(concert[0]+concert[1])
precisio[1] = conference[0] / (conference[0]+conference[1])
precisio[2] = exhibition[0] / (exhibition[0]+exhibition[1])
precisio[3] = fashion[0] / (fashion[0]+fashion[1])
precisio[4] = non_event[0] / (non_event[0]+non_event[1])
precisio[5] = other[0] / (other[0]+other[1])
precisio[6] = protest[0] / (protest[0]+protest[1])
precisio[7] = sports[0] / (sports[0]+sports[1])
precisio[8] = the_dance[0] / (the_dance[0]+the_dance[1])

#RECORD
record[0] = concert[0] / (concert[0]+concert[2]) 
record[1] = conference[0] / (conference[0]+conference[2])
record[2] = exhibition[0] / (exhibition[0]+exhibition[2])
record[3] = fashion[0] / (fashion[0]+fashion[2])
record[4] = non_event[0] / (non_event[0]+non_event[2])
record[5] = other[0] / (other[0]+other[2])
record[6] = protest[0] / (protest[0]+protest[2])
record[7] = sports[0] / (sports[0]+sports[2])
record[8] = the_dance[0] / (the_dance[0]+the_dance[2])

#F1-SCORE
f1score[0] = 2*((precisio[0]*record[0])/(precisio[0]+record[0]))
f1score[1] = 2*((precisio[1]*record[1])/(precisio[1]+record[1]))
f1score[2] = 2*((precisio[2]*record[2])/(precisio[2]+record[2]))
f1score[3] = 2*((precisio[3]*record[3])/(precisio[3]+record[3]))
f1score[4] = 2*((precisio[4]*record[4])/(precisio[4]+record[4]))
f1score[5] = 2*((precisio[5]*record[5])/(precisio[5]+record[5]))
f1score[6] = 2*((precisio[6]*record[6])/(precisio[6]+record[6]))
f1score[7] = 2*((precisio[7]*record[7])/(precisio[7]+record[7]))
f1score[8] = 2*((precisio[8]*record[8])/(precisio[8]+record[8]))

#AVERAGE 0=precisio, 1=record, 2=f1score
avg[0] = np.nan_to_num(np.nansum(precisio)/np.count_nonzero(precisio))
avg[1] = np.nan_to_num(np.nansum(record)/np.count_nonzero(record))
avg[2] = np.nan_to_num(np.nansum(f1score)/np.count_nonzero(f1score))

#Nan_to_num
precisio = np.nan_to_num(precisio)
record   = np.nan_to_num(record)
f1score  = np.nan_to_num(f1score)

#-----------------------------BAR PLOT

fig1 = plt.figure(1)
a = np.arange(9)
plt.bar(a, f1score, align='center')
plt.xticks(a,('concert', 'conference', 'exhibition', 'fashion', 'non_event', 'other', 'protest', 'sports', 'theater_dance'), rotation = 90)
plt.ylabel('F1-Score')
plt.xlabel('Event Type')
plt.title('Resultat F1-Score per cada event')
plt.savefig("f1score_result.png",bbox_inches='tight')
plt.close()

fig2 = plt.figure(2)
b = np.arange(9)
plt.bar(b, precisio, align='center')
plt.xticks(b,('concert', 'conference', 'exhibition', 'fashion', 'non_event', 'other', 'protest', 'sports', 'theater_dance'), rotation = 90)
plt.ylabel('Precisio')
plt.xlabel('Event Type')
plt.title('Resultat Precisio per cada event')
plt.savefig("precision_result.png",bbox_inches='tight')
plt.close()

fig3 = plt.figure(3)
c = np.arange(9)
plt.bar(c, record, align='center')
plt.xticks(c,('concert', 'conference', 'exhibition', 'fashion', 'non_event', 'other', 'protest', 'sports', 'theater_dance'), rotation = 90)
plt.ylabel('Record')
plt.xlabel('Event Type')
plt.title('Resultat Record per cada event')
plt.savefig("record_result.png",bbox_inches='tight')
plt.close()

#--------------------SAVE RESULTS TO FILE

events = [concert, conference, exhibition, fashion, non_event, other, protest, sports, the_dance]
ev_name = ['Concert        ', 'Conference     ', 'Exhibition     ', 'Fashion        ', 'Non_event      ', 'Other          ', 'Protest        ', 'Sports         ', 'Theater_dance  ']

f = open('resultat.txt', 'w')
f.write("Resultats d'avaluació:\n\n")
f.write("Matrius de confusió\n\n")
i = 0
while (i < 9):
    f.write(ev_name[i]+'\n') 
    f.write('                      Classificacio\n')
    f.write('                   Positiu      Negatiu\n')
    f.write('Ground  Positiu      ')
    f.write(str(events[i][0]))
    f.write('          ')
    f.write(str(events[i][2])+'\n')
    f.write('Truth   Negatiu      ')
    f.write(str(events[i][1]))
    f.write('         ')
    f.write(str(events[i][3])+'\n') 
    f.write('\n')
    f.write('-----------------------------------------\n')
    i = i + 1  

f.write('Resultats:\n\n')
f.write('            Precisió    Record   F1-Score\n')

x = 0
while (x < 9):
    f.write(ev_name[x])
    f.write(str("%.2f" % precisio[x]))
    f.write('      ')
    f.write(str("%.2f" % record[x]))
    f.write('      ')
    f.write(str("%.2f" % f1score[x])+'\n')
    x = x + 1

f.write('-----------------------------------------\n')
f.write('     Precisió   Record   F1-Score\n')
f.write('AVG    ')
f.write(str("%.2f" % avg[0]))
f.write('      ')
f.write(str("%.2f" % avg[1])) 
f.write('      ')
f.write(str("%.2f" % avg[2])) 
f.write('\n\n')

#---------------PERCENTATGE + PIE
correcte = 0
total = 0
y = 0

while (y < 9):
    correcte = correcte + events[y][0] + events[y][3]
    total = total + events[y][0] + events[y][1] + events [y][2] + events[y][3]
    y = y + 1

tpcent_correcte = 0
tpcent_correcte = correcte / total * 100
tpcent_erroni = 100 - tpcent_correcte

f.write('-----------------------------------------\n')
f.write('\n')
f.write('Correctament classificat: '+str("%.2f" % tpcent_correcte+'%\n'))
f.write('Erroniament classificat: '+str("%.2f" % tpcent_erroni+'%\n'))

fig4 = plt.figure(4)
labels = 'Correctament classificats', 'Erroniament classificats'
sizers = [tpcent_correcte, tpcent_erroni]
colors = ['green', 'red']
explode = (0.1, 0)
plt.pie(sizers, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')
plt.savefig("Percentatge.png",bbox_inches='tight')
plt.close()

f.close()
print(str(datetime.timedelta(seconds=(time.time()-timer))))
