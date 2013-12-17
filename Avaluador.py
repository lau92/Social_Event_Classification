# -*- coding: utf-8 -*-

#Metadata Social Event Classification: AVALUADOR
#Sergi Diaz, Iker Elorza, Ferran Monfort, Jordi Aguilar

import pandas as pd
import csv
import numpy as np 
import matplotlib.pyplot as plt
import time
import datetime

timer = time.time()

#Arxiu de resultats provinents del classificador
class_result = pd.read_csv('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio 5\Res_34.txt', sep=' ') 

#Ground truth
sol_train  = pd.read_csv('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Projecte_GDSA_1.3-master\Projecte_GDSA_1.3-master\Metadades\PER.txt', sep=' ')

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

predict = []
ground = []
y = 0

while ( y < len_class):
    predict.append(class_result.event_type[y])
    ground.append(sol_train.event_type[y])
    y+=1

#------------------- MATRIU DE CONFUSIO PER A CADA EVENT

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
    
                #incrementar el negatius certs
                if (class_result.event_type[i] != "concert" and sol_train.event_type[j] != "concert" ):              concert[3] += 1.0
                if (class_result.event_type[i] != "conference"and sol_train.event_type[j] != "conference"):          conference[3] += 1.0
                if (class_result.event_type[i] != "exhibition"and sol_train.event_type[j] != "exhibition"):          exhibition[3] += 1.0
                if (class_result.event_type[i] != "fashion"and sol_train.event_type[j] != "fashion"):                fashion[3] += 1.0
                if (class_result.event_type[i] != "non_event"and sol_train.event_type[j] != "non_event"):            non_event[3] += 1.0
                if (class_result.event_type[i] != "other"and sol_train.event_type[j] != "other"):                    other[3] += 1.0
                if (class_result.event_type[i] != "protest"and sol_train.event_type[j] != "protest"):                protest[3] += 1.0
                if (class_result.event_type[i] != "sports"and sol_train.event_type[j] != "sports"):                  sports[3] += 1.0
                if (class_result.event_type[i] != "theater_dance" and sol_train.event_type[j] != "theater_dance"):   the_dance[3] += 1.0 
                
            else:
                #incrementar positiu fals de la primera classe
                if (class_result.event_type[i] == "concert" and sol_train.event_type[j] != "concert"):     concert[1] += 1.0
                elif (class_result.event_type[i] == "conference" and sol_train.event_type[j] != "conference"):  conference[1] += 1.0
                elif (class_result.event_type[i] == "exhibition" and sol_train.event_type[j] != "exhibition"):  exhibition[1] += 1.0
                elif (class_result.event_type[i] == "fashion" and sol_train.event_type[j] != "fashion"):     fashion[1] += 1.0
                elif (class_result.event_type[i] == "non_event" and sol_train.event_type[j] != "non_event"):   non_event[1] += 1.0
                elif (class_result.event_type[i] == "other" and sol_train.event_type[j] != "other"):       other[1] += 1.0
                elif (class_result.event_type[i] == "protest" and sol_train.event_type[j] != "protest"):     protest[1] += 1.0
                elif (class_result.event_type[i] == "sports" and sol_train.event_type[j] != "sports"):       sports[1] += 1.0
                elif (class_result.event_type[i] == "theater_dance" and sol_train.event_type[j] != "theater_dance"):   the_dance[1] += 1.0 
                
                #incrementar els positius fals 
                if (class_result.event_type[i] != "concert" and sol_train.event_type[j] == "concert"):     concert[2] += 1.0
                elif (class_result.event_type[i] != "conference" and sol_train.event_type[j] == "conference"):  conference[2] += 1.0
                elif (class_result.event_type[i] != "exhibition" and sol_train.event_type[j] == "exhibition"):  exhibition[2] += 1.0
                elif (class_result.event_type[i] != "fashion" and sol_train.event_type[j] == "fashion"):     fashion[2] += 1.0
                elif (class_result.event_type[i] != "non_event" and sol_train.event_type[j] == "non_event"):   non_event[2] += 1.0
                elif (class_result.event_type[i] != "other" and sol_train.event_type[j] == "other"):       other[2] += 1.0
                elif (class_result.event_type[i] != "protest" and sol_train.event_type[j] == "protest"):     protest[2] += 1.0
                elif (class_result.event_type[i] != "sports" and sol_train.event_type[j] == "sports"):       sports[2] += 1.0
                elif (class_result.event_type[i] != "theater_dance" and sol_train.event_type[j] == "theater_dance"):   the_dance[2] += 1.0 
                
                #incrementar els negatius fals
                if (class_result.event_type[i] != "concert" and sol_train.event_type[j] != "concert" ):              concert[3] += 1.0
                if (class_result.event_type[i] != "conference"and sol_train.event_type[j] != "conference"):          conference[3] += 1.0
                if (class_result.event_type[i] != "exhibition"and sol_train.event_type[j] != "exhibition"):          exhibition[3] += 1.0
                if (class_result.event_type[i] != "fashion"and sol_train.event_type[j] != "fashion"):                fashion[3] += 1.0
                if (class_result.event_type[i] != "non_event"and sol_train.event_type[j] != "non_event"):            non_event[3] += 1.0
                if (class_result.event_type[i] != "other"and sol_train.event_type[j] != "other"):                    other[3] += 1.0
                if (class_result.event_type[i] != "protest"and sol_train.event_type[j] != "protest"):                protest[3] += 1.0
                if (class_result.event_type[i] != "sports"and sol_train.event_type[j] != "sports"):                  sports[3] += 1.0
                if (class_result.event_type[i] != "theater_dance" and sol_train.event_type[j] != "theater_dance"):   the_dance[3] += 1.0               
               
            break;
        j=j+1
    i=i+1          



#--------- Precisio, Record, F1score, Accuracy

precisio = np.zeros(9,float)
record = np.zeros(9,float)
f1score = np.zeros(9,float)
avg = np.zeros(3,float)

#--------- PRECISIO

precisio[0] = concert[0]/(concert[0]+concert[1])
precisio[1] = conference[0] / (conference[0]+conference[1])
precisio[2] = exhibition[0] / (exhibition[0]+exhibition[1])
precisio[3] = fashion[0] / (fashion[0]+fashion[1])
precisio[4] = non_event[0] / (non_event[0]+non_event[1])
precisio[5] = other[0] / (other[0]+other[1])
precisio[6] = protest[0] / (protest[0]+protest[1])
precisio[7] = sports[0] / (sports[0]+sports[1])
precisio[8] = the_dance[0] / (the_dance[0]+the_dance[1])

#-------- RECORD

record[0] = concert[0] / (concert[0]+concert[2]) 
record[1] = conference[0] / (conference[0]+conference[2])
record[2] = exhibition[0] / (exhibition[0]+exhibition[2])
record[3] = fashion[0] / (fashion[0]+fashion[2])
record[4] = non_event[0] / (non_event[0]+non_event[2])
record[5] = other[0] / (other[0]+other[2])
record[6] = protest[0] / (protest[0]+protest[2])
record[7] = sports[0] / (sports[0]+sports[2])
record[8] = the_dance[0] / (the_dance[0]+the_dance[2])

#------- F1-SCORE

f1score[0] = 2*((precisio[0]*record[0])/(precisio[0]+record[0]))
f1score[1] = 2*((precisio[1]*record[1])/(precisio[1]+record[1]))
f1score[2] = 2*((precisio[2]*record[2])/(precisio[2]+record[2]))
f1score[3] = 2*((precisio[3]*record[3])/(precisio[3]+record[3]))
f1score[4] = 2*((precisio[4]*record[4])/(precisio[4]+record[4]))
f1score[5] = 2*((precisio[5]*record[5])/(precisio[5]+record[5]))
f1score[6] = 2*((precisio[6]*record[6])/(precisio[6]+record[6]))
f1score[7] = 2*((precisio[7]*record[7])/(precisio[7]+record[7]))
f1score[8] = 2*((precisio[8]*record[8])/(precisio[8]+record[8]))

#-------- TOTAL 

precisio = np.nan_to_num(precisio)
record   = np.nan_to_num(record)
f1score  = np.nan_to_num(f1score)

total_precisio = sum(precisio) / np.count_nonzero(precisio)
total_record = sum(record) / np.count_nonzero(record)
total_f1score = sum(f1score) / np.count_nonzero(f1score)

#--------- ACCURACY

class_result = list(csv.reader(open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Solucions_Grups\Res_11.txt','rb'),delimiter=' '))
sol_train =    list(csv.reader(open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\sol_1.txt','rb'),delimiter=' '));

doc_id=[];
tags=[];
lon_fi=(len(class_result));
m=0;
llista=[];

while(m<lon_fi):  
    if(m>0):
      if(class_result[m][0]!=class_result[m-1][0]):
           doc_id.append(tags);
           tags=[];
           tags.append(class_result[m][1]+'\n');
           llista.append(doc_id);
           doc_id=[];
           doc_id.append(class_result[m][0]);     
      else:
           tags.append(class_result[m][1]+'\n');
    else:
        doc_id.append(class_result[m][0]);
        tags.append((class_result[m][1]+'\n'));
    m+=1

doc_id.append(tags);    
llista.append(doc_id);

doc_id = [];
tags = [];
lon_fi = (len(sol_train));
m = 0;
llista1 = [];

while(m<lon_fi): 
    if(m>0):
      if(sol_train[m][0]!=sol_train[m-1][0]):
           doc_id.append(tags);
           tags=[];
           tags.append(sol_train[m][1]+'\n')
           llista1.append(doc_id);
           doc_id=[];
           doc_id.append(sol_train[m][0]);   
      else:
           tags.append(sol_train[m][1]+'\n')
    else:
        doc_id.append(sol_train[m][0]);
        tags.append((sol_train[m][1]+'\n'))
    m+=1

doc_id.append(tags);    
llista1.append(doc_id)

i = 0
a = []
b = []

while (i<(len(llista1))):
    j=0
    while (j<(len(llista))):
      if(llista1[i][0]==llista[j][0]):
          a.append(llista1[i][1])
          b.append(llista[j][1])
          break
      j=j+1
    i=i+1
    
i=0
cont=0.0

while(i<len(a)):
    if(a[i]==b[i]):
        cont=cont+1;
    i=i+1;

accuracy = cont/len(a)*100
tpcent_erroni = 100 - accuracy

#--------- RESULTAT.TXT

events = [concert, conference, exhibition, fashion, non_event, other, protest, sports, the_dance]
ev_name = ['Concert        ', 'Conference     ', 'Exhibition     ', 'Fashion        ', 'Non_event      ', 'Other          ', 'Protest        ', 'Sports         ', 'Theater_dance  ']

f = open('resultat.txt', 'w')
f.write("Resultats d'avaluaciÃ³:\n\n")
f.write("Matrius de confusiÃ³\n\n")
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
f.write('            Precisio    Record   F1-Score\n')

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
f.write('\n')
f.write('Precisio: '+str("%.5f" % total_precisio+'\n'))
f.write('Record  : '+str("%.5f" % total_record+'\n'))
f.write('F1-Score: '+str("%.5f" % total_f1score+'\n\n'))
f.write('Accuracy: '+str("%.2f" % accuracy+'%\n'))

#---------------- FIGURES

fig1 = plt.figure(1)
a = np.arange(9)
plt.bar(a, f1score, align='center')
plt.xticks(a,('concert', 'conference', 'exhibition', 'fashion', 'non_event', 'other', 'protest', 'sports', 'theater_dance'), rotation = 90)
plt.ylabel('F1-Score')
plt.xlabel('Event Type')
plt.title('Resultat F1-Score per cada event')
fig1.savefig("f1score_result.png",bbox_inches='tight')

fig2 = plt.figure(2)
a = np.arange(9)
plt.bar(a, precisio, align='center')
plt.xticks(a,('concert', 'conference', 'exhibition', 'fashion', 'non_event', 'other', 'protest', 'sports', 'theater_dance'), rotation = 90)
plt.ylabel('Precisio')
plt.xlabel('Event Type')
plt.title('Resultat Precisio per cada event')
fig2.savefig("precision_result.png",bbox_inches='tight')

fig3 = plt.figure(3)
a = np.arange(9)
plt.bar(a, record, align='center')
plt.xticks(a,('concert', 'conference', 'exhibition', 'fashion', 'non_event', 'other', 'protest', 'sports', 'theater_dance'), rotation = 90)
plt.ylabel('Record')
plt.xlabel('Event Type')
plt.title('Resultat Record per cada event')
fig3.savefig("record_result.png",bbox_inches='tight')

events = [concert, conference, exhibition, fashion, non_event, other, protest, sports, the_dance]
ev_name = ['Concert        ', 'Conference     ', 'Exhibition     ', 'Fashion        ', 'Non_event      ', 'Other          ', 'Protest        ', 'Sports         ', 'Theater_dance  ']

fig4 = plt.figure(4)
labels = 'Accuracy', 'Erroni'
sizers = [accuracy, tpcent_erroni]
colors = ['green', 'red']
explode = (0.1, 0)
plt.pie(sizers, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')
plt.savefig("accuracy.png",bbox_inches='tight')

plt.show()

#--------------------------- 

f.close()
print '\n'
print("Temps total: "+str(datetime.timedelta(seconds=(time.time()-timer)))), "\n"
print 'Accuracy: ', str("%.2f" % accuracy+'%')
print 'F1-Score:  '+str("%.5f" % total_f1score)
