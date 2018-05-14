import os 
import csv

os.chdir('/mnt/digital-staging/Mexican-Broadsides/batch2/Working_Files')
folders = [name for name in os.listdir(".") if os.path.isdir(name)]
csvfile = '/home/zelgius/Documents/biblist.csv'
txtfile = '/home/zelgius/Documents/biblist.txt'
textfile = open(txtfile,'w')

print("A preview of the bib list:", '\n', folders[0:30])
print('\n',len(folders), "total folders")

# Assuming a flat list! Write the csv
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for f in folders:
        writer.writerow([f]) 

# Write the txt file        
textfile.write(",".join(folders))
        
    
print('\n', "bib list csv and .txt completed!")