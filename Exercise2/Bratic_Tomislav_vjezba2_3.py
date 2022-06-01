# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:03:36 2021

@author: Tomica
"""
def zadatak3():

    def rekurzija(arr):
        n=len(niz)
        if n==1:
            return  niz
        elif( niz[n-1]> niz[n-2]):
            del  niz[n-2]
        elif( niz[n-2]> niz[n-1]):
                del  niz[n-1] 
                
        return rekurzija(arr)
    
    
    def notint(arr):
        for i in range(0,len(niz)-1):
            if type(niz[i])is str or type(niz[i])is tuple:
                niz.pop(i)
    
    
    niz=[2,3,7,"true",8,9,(2,3)];
    
    
    
    print("nakon pop-a vrijednost:niza:")
    notint(niz)
    
    print(niz)
    y=rekurzija(niz)
    print(y)

def main():
    zadatak3()       
        
if __name__ == "__main__":
    main()