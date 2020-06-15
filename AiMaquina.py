
TIPO= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}



import itertools as it
from pattern.es import spelling,lexicon,parse
import json

def Ai()
  letras = "l"  
  palabras = set()
  for i in range(2,len(letras)+1):
      palabras.update((map("".join, it.permutations(letras, i))))

  palabras_existentes=[]
  for i in palabras:
    if i in spelling.keys() and i in lexicon.keys(): #Dificultad -> Facil
    ##Verificar si la palabra es verbo o adjetivo parse() -> VB - JJ Dificultad -> Medio,Dificil
      palabras_existentes.append(i)

  with open("palabras.json","w") as file:
    #json.dump(res,file,indent=4)
    json.dump(palabras_existentes,file,indent=4)

#ProgramaPrincipal
if __name__ == "__main__":
    Ai()