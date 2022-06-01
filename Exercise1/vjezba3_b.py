# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:39:23 2021

@author: Tomica
"""
def zadatak3_b():
    
    x=5
    y=20
    flag=0;
    arrnumber=[];
    br=0;
    
    for i in range(x,y):
        flag=0
        for j in range(2,int(i/2)):
            
            if(i%j==0):
               
               flag=1;
               
               
        if flag==0:
            arrnumber.append(i)
            br=br+1;                                                              
            
    print(arrnumber)  
    z=len(arrnumber)    
    print("odaberi n-ti prosti broj u nizu od nula do",z,":")                                                      
    print(" ")
    n=int(input())
    if n<0 or n>z:
        print("kriv upis.")
    print("ispisan je broj",arrnumber[n])

def main():
    zadatak3_b()       
        
if __name__ == "__main__":
    main()    