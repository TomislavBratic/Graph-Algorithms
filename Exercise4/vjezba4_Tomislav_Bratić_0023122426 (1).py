# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:06:26 2021

@author: Tomislav Bratić
"""

from sortedcontainers import SortedList
import time

def Obris(buildings):
        niz = []
        for l, r, h in buildings:
           niz.append((l, h, 0))
           niz.append((r, h, 1))
           

        ans = []
        aktivne_visine = SortedList([0])
        
        niz.sort()     #nlogn
        print("Lijeva i desna tocka:\n",niz,"\n")
        n = len(niz)
        i = 0
        
        while i < n:       #n
            x, h, t = niz[i]
            if t == 0:
                aktivne_visine.add(h)
                print("Dodaje se visina ", h,"\n" ,aktivne_visine,"\n")
            else:
                aktivne_visine.remove(h)
                print("Brise se visina ", h ,"\n",aktivne_visine,"\n")
            i += 1
            
            if not ans or ans[-1][1] != aktivne_visine[-1]:
                ans.append((x, aktivne_visine[-1]))
                
        
        return ans
    
start = time.perf_counter()
print("krece program\n")

buildings = [[1,5,11],[3,9,13],[12,16,7],[14,25,3],[19,22,18],[23,29,13],[24,28,4]]
y=Obris(buildings)

end = time.perf_counter()
print(end - start," je vrijeme izvršavanja\n")
print("kompleksnost je:T(n)=nlogn+n reda Θ(nlogn)")

