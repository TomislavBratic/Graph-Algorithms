# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:04:37 2021

@author: Tomica
"""
def zadatak1():
    niz1=[1,2,3,4,5]
    niz2=[2,3,7,6,8,9]
    niz3=[0]
    brojac1=0;
    brojac2=0;
    
    while(len(niz1) and len(niz2)):
        if(niz1[0]>niz2[0]):
            niz3.append(niz2.pop(0))
            brojac1=brojac1+1;
        elif(niz1[0]<niz2[0]):        
            niz3.append(niz1.pop(0))
            brojac2=brojac2+1;
        else:
            niz3.append(niz1.pop(0))
            niz2.pop(0)
            brojac1=brojac1+1;
            brojac2=brojac2+1;
            
    
    if(len(niz1)==0):  
        niz3.extend(niz2)
    else:    
        niz3.extend(niz1)
    
    
    print(niz3) 
    
def main():
        zadatak1()       
    
if __name__ == "__main__":
    main()
    