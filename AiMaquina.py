import itertools as it
from pattern.es import spelling,lexicon,parse
import random

Tipo= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NCS","NCP", "NNS","NP", "NNP","W"],#Revisar volver a comprobar en facil , primero en spell y lexi luego en sus
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}
##Verificar si la palabra es verbo o adjetivo parse() -> VB - JJ Dificultad -> Medio,Dificil
#if i in spelling.keys() and i in lexicon.keys(): #Dificultad -> Facil (Existe en lexicon y spelling) Hacer parse , si no es sut hacerla valida , si es sustantivo verificar si esta en spellin o lexicon si esta en alguna de las 2 es valida sino , es invalida

def palabra_larga(lista_palabras):
    max=0
    palabra_max=""
    for x in lista_palabras:
        if(len(x)>=max):
            max=len(x)
            palabra_max=x
    return(palabra_max)
def Facil(i,palabras_existentes):
    if (i in spelling.keys() or i in lexicon.keys()):
        if(parse(i).split("/")[1] in Tipo['sus']):
            palabras_existentes.append(i)
        elif(parse(i).split("/")[1] in Tipo['adj']):
            palabras_existentes.append(i)
        elif(parse(i).split("/")[1] in Tipo['verb']):
            palabras_existentes.append(i)
def Medio(i,palabras_existentes):
    if i in spelling.keys() and i in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        if(parse(i).split("/")[1] in Tipo['verb']):
            palabras_existentes.append(i)
        elif(parse(i).split("/")[1] in Tipo['sus']):
            palabras_existentes.append(i)
def Dificil(i,palabras_existentes,Dificil_elegido):
    if i in spelling.keys() and i in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
            if(Dificil_elegido=="adj"):
                if(parse(i).split("/")[1] in Tipo['adj']):
                    palabras_existentes.append(i)
            elif(Dificil_elegido =="verb"):
                if(parse(i).split("/")[1] in Tipo['verb']):
                    palabras_existentes.append(i)
            elif(Dificil_elegido=="sus"):
                if(parse(i).split("/")[1] in Tipo['sus']):
                    palabras_existentes.append(i)
def formar_palabra(letras,dificultad,Dificil_elegido):
    letras=letras.lower()
    palabras = set()
    for i in range(2,len(letras)+1):
        palabras.update((map("".join, it.permutations(letras, i))))
    palabras_existentes=[]
    for i in palabras:
        if (dificultad=="Facil"):
            Facil(i,palabras_existentes)
        elif(dificultad=="Medio"):
            Medio(i,palabras_existentes)
        elif(dificultad=="Dificil"):
            Dificil(i,palabras_existentes,Dificil_elegido)
    return(palabra_larga(palabras_existentes))


  #---------Porgrama Principal---
if __name__ == '__main__':
    print(formar_palabra("oef","Dificil","adj"))
