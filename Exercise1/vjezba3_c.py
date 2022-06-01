# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:44:01 2021

@author: Tomica
"""

def zadatak3_c():

    x=5
    y=100
    flag=0;
    arrnumber=[];
    br=0;
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
    flag=0;
    
    
    for i in range(0,z-1):
            
        if(arrnumber[i+1]-arrnumber[i]==2):
            print("brojevi",arrnumber[i],"i",arrnumber[i+1],"su susjedni")

def main():
    zadatak3_c()       
        
if __name__ == "__main__":
    main()