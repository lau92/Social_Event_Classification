# -*- coding: utf-8 -*-

#Metadata Social Event Classification: CLASSIFICADOR
#Sergi Diaz, Iker Elorza, Ferran Monfort, Jordi Aguilar

import pandas as pd
import csv
import numpy as np

dades_clas = list(csv.reader(open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_clas\doc_classificador.csv','rb'),delimiter=' '));

doc_id=[];
tags=[];
lon_fi=(len(dades_clas));
m=0;
llista=[];

while(m<lon_fi):
        
    if(m>0):
    
      if(dades_clas[m][0]!=dades_clas[m-1][0]):
           doc_id.append(tags);
           tags=[];
           tags.append(dades_clas[m][1]+'\n');
           llista.append(doc_id);
           doc_id=[];
           doc_id.append(dades_clas[m][0]);
           
      else:
           tags.append(dades_clas[m][1]+'\n');
    
    else:
        doc_id.append(dades_clas[m][0]);
        tags.append((dades_clas[m][1]+'\n'));
        
    m+=1
doc_id.append(tags);    
llista.append(doc_id);

concert = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\concert_ent.txt")
llista_con=concert.readlines()
concert.close()

conference = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\conference_ent.txt")
llista_conf=conference.readlines()
conference.close()

exhibition = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\exhibition_ent.txt")
llista_ex=exhibition.readlines()
exhibition.close()


fashion = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\efashion_ent.txt")
llista_fas=fashion.readlines()
fashion.close()

non_event = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\enon_event_ent.txt")
llista_ne=non_event.readlines()
non_event.close()

other = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\other_ent.txt")
llista_ot=other.readlines()
other.close()

sports = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\sport_ent.txt")
llista_sp=sports.readlines()
sports.close()

theater_dance = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\etheater_dance_ent.txt")
llista_td=theater_dance.readlines()
theater_dance.close()

protest = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\protest_ent.txt")
llista_pr=protest.readlines()
protest.close()

tam=len(llista);
itera=0;
cont_id=[];

while(itera<tam):
    cont_concert = 0
    cont_conference = 0
    cont_exhibition = 0
    cont_fashion = 0
    cont_non_event = 0
    cont_other = 0
    cont_sports = 0
    cont_theater_dance = 0
    cont_protest = 0
    maxims=0;
    concert = ['concert']
    conference = ['conference']
    exhibition = ['exhibition']
    fashion = ['fashion']
    other = ['other']
    sports = ['sports']
    theater_dance = ['theater_dance']
    protest = ['protest']
    non_event=['non_event']
    
     
         
    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_con.count((llista[itera][1])[i])
      cont_concert=cont_concert+aux
      i+=1
    concert.append(cont_concert)

    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_conf.count(llista[itera][1][i])
      cont_conference=cont_conference+aux
      i+=1
    conference.append(cont_conference)
    
    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_ex.count(llista[itera][1][i])
      cont_exhibition=cont_exhibition+aux
      i+=1
    exhibition.append(cont_exhibition)
    
    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_fas.count(llista[itera][1][i])
      cont_fashion=cont_fashion+aux
      i+=1
    fashion.append(cont_fashion)
   
    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_ot.count(llista[itera][1][i])
      cont_other=cont_other+aux
      i+=1
    other.append(cont_other)

    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_sp.count(llista[itera][1][i])
      cont_sports=cont_sports+aux
      i+=1
    sports.append(cont_sports)
    
    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_td.count(llista[itera][1][i])
      cont_theater_dance=cont_theater_dance+aux
      i+=1
    theater_dance.append(cont_theater_dance)

    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_pr.count(llista[itera][1][i])
      cont_protest=cont_protest+aux
      i+=1
    protest.append(cont_protest)

    i=0;
    while(i<len(llista[itera][1])):
      aux=llista_ne.count(llista[itera][1][i])
      cont_non_event=cont_non_event+aux
      i+=1
    non_event.append(cont_non_event)
    
    maxims=(max(concert[1],conference[1],exhibition[1],fashion[1],other[1],sports[1],theater_dance[1],protest[1],non_event[1]))


    if(maxims<3):
        cont_id.append([llista[itera][0],non_event[0]])
    else:
        if(concert[1]==maxims):
                cont_id.append([llista[itera][0],concert[0]]);
        elif(conference[1]==maxims):
                cont_id.append([llista[itera][0],conference[0]]);
        elif(exhibition[1]==maxims):
                cont_id.append([llista[itera][0],exhibition[0]]);
        elif(fashion[1]==maxims):
                cont_id.append([llista[itera][0],fashion[0]]);
        elif(other[1]==maxims):
                cont_id.append([llista[itera][0],other[0]]);
        elif(sports[1]==maxims):
                cont_id.append([llista[itera][0],sports[0]]);
        elif(theater_dance[1]==maxims):
                cont_id.append([llista[itera][0],theater_dance[0]]);
        elif(protest[1]==maxims):
                cont_id.append([llista[itera][0],protest[0]]);
        elif(non_event[1]==maxims):
                cont_id.append([llista[itera][0],non_event[0]]);
        
                
    itera+=1
    
i=0;
x=len(cont_id)

fitxer = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Resultats_Definitius.txt","a")
fitxer.write('document_id event_type' '\n')
fitxer.close()
        
while(i<x):
        fitxer = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Resultats_Definitius.txt","a")
        fitxer.write(str(cont_id[i][0])+' '+str(cont_id[i][1]))
        fitxer.write("\n")
        fitxer.close()
        
        i+=1
   
fitxer.close()
       
