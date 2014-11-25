import matplotlib.mlab as ml
import numpy as np

def get_sightings(filename, ani):
	#Loading table
	tab=ml.csv2rec(filename) #Load a given table and call it tab. This function takes first line as headings (conveted to lower case), and latter as data
	ani=ani.capitalize()
	#Find total number of records for animal and calculate mean sightings
	isfocus=(tab['animal'] == ani) #Checks for whether ip ani exists within file- eg animal called cow
	total_rec=np.sum(isfocus) #Tells how many of the above there are in the file

	if total_rec == 0:
		meancount=0
	else:
		meancount=np.mean(tab['count'][isfocus])  #Find the mean (a function in numpy) of counts from file

	#Return number of records and animals seen
	return total_rec, meancount

