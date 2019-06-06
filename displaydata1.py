import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.sparse import dok_matrix
import csv

df = pd.read_csv('sortedlist.csv')
#df['mean'] = df.mean(axis=1)
#m100 = (df['mean']>= 1000)
#df = df.groupby(['EnsemblIDs']).mean().sort_values('mean', ascending=True)
print(df)

#tm = df[df.Transcription_Mean == '']
plt.title("test plot")
plt.xlabel("Avg TPM")
plt.ylabel("Genes")


plt.plot(df.Transcription_Mean, df.EnsemblIDs) 
plt.show()






	

# Reads csv file 


#with open('patientlist.csv') as csvfile:
		#readCSV = csv.reader(csvfile, delimiter=',')
		#patientlist = [None]*22000 # need to learn how many lines in a csv in general
		#patientlist = []
		#ens_list = [] # this will store the ENS IDs 
		#avg_list = [] # will store averages among the 7 patients, both lists built simulataneously 
	
		#i = 0
		#firstrow = next(readCSV)
		#for row in readCSV:
			 # probably unnecessary at this point since using enslist
				#print(Dforward.get(row[0]))
				#row[0] = Dforward.get(row[0])
				#patientlist[Dforward.get(row[0])] = row;
			#ens_list.append(row[0])
			#patientlist.append(row[1:])
			#vals = [float(j) for j in row[1:]]
			#avg_i = np.mean(vals)
			#print(avg_i)
			#avg_list.append(avg_i)
			#i = i + 1;

		#print(avg_list);
		#print(ens_map)
		#print(patientlist[8068]);
		#S = sorted(range(len(avg_list)), key=lambda k: avg_list[k]) # this returns indices of avg_list such that
		# S[0] is the index of the smalles element of avg-list and so on, will also allow us to get the ens is correspo
		# to smallest avg 
		#print(S);
		#S_sorted = [(ens_list[i],avg_list[i]) for i in S]
		#print(S_sorted[-100:]);

		# the whole list goes from tiny numbers around 0 up to 72517, total elems around 20000
		#last 100 elems range from 1000 to 72000, roughly


#df['mean'] = df.mean(axis=1)
#df.groupby(['mean'].sort_values('mean', ascending=True))

#m100 = df.loc[df['mean'] >= 1000]








#plt.plot(df.Patient1_Gene_Score.head(), df.EnsemblIDs.head(), 'o')