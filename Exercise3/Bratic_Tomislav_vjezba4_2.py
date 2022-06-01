def zadatak2():
    import csv
    
    def sumkol(x,k1,k2):
        summ=0;
        summ = 0.2 *x + 0.4 *k1  + 0.4 * k2
        return summ
    
    def sumispit(x,ispit):
        summ=0;
        summ=0.2 *x + 0.8*ispit
        return summ
    
    def red ():
       csv_writer.writerow(line);
    
    broj_bodova=0;
    with open('evidencija.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        with open('evidencija2.csv', 'w') as new_file:
            fieldnames = ['mat.','status','V', '1.rok','K1', 'K2', 'status2'];
    
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
    
            csv_writer.writeheader()
    
            for line in csv_reader:
                
                 if line["V"]=='' or int(line["V"])<50:
                   line['status2']="nopp";
                   csv_writer.writerow(line);
                 
                 elif line["K1"]=='' or line["K2"]=='' or (int(line["K1"])+int(line["K2"]))<40:
                     if line["1.rok"]=='' or (int(line["1.rok"]))<50:
                         line['status2']="1";
                         red()
                     
                     else:
                         broj_bodova = sumispit(int(line["V"]),int(line["1.rok"]))
                         line['status2']=broj_bodova
                         
                         red()
                 
                 else:
                     broj_bodova = sumkol(int(line["V"]),int(line["K1"]),int(line["K2"])) 
                     line['status2']=broj_bodova
                     red()
                     

def main():
    zadatak2()       
         
if __name__ == "__main__":
     main()   