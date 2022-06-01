# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:02:33 2021

@author: Tomica
"""
def zadatak2():
    import random
    niz=[0,1,2];
    brojac1=0;
    brojac2=0;
    x=0;
    y=0;
    
    while(brojac1<3 and brojac2<3):
        print("odaberi broj od 0 do 2:")
        x=input()  
        print("računalo bira broj od 0 do 2.")
        y=random.choice(niz)
        print(y)
        if(x==y):
            print("isti broj.bacaj ponovo")
        elif(x==0 and y==1):
            print("igrac dobio")
            brojac1=brojac1+1;
            
        elif(x==1 and y==2):
            print("igrac dobio")
            brojac1=brojac1+1;   
            
        elif(x==2 and y==0):
            print("igrac dobio")
            brojac1=brojac1+1;  
        
        else:
            print("racunalo dobilo")
            brojac2=brojac2+1;  
    
    print("")
    if(brojac1==3):
        print("igrac pobijedio")
    else:
        print("racunalo pobijedilo")
       
def main():
    zadatak2()       
        
if __name__ == "__main__":
    main()        
        
        