# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:31:16 2021

@author: Tomica
"""
def zadatak4():

    brojevi = {
      "x": [2,3],
      "y": [2,5],
      "z": [1],
      "a": [2]
    }
    slova= {}
    brojac=1;
    for k, v in brojevi.items():
        if brojac not in slova:
            slova[brojac]= [k]
            brojac=brojac+1;
        else:
            slova[brojac].extend(k)
            
    print(slova)
    
def main():
        zadatak4()       
        
if __name__ == "__main__":
    main()