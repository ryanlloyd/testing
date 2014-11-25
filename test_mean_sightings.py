from mean_sightings import get_sightings

filename = 'sightings_animal.csv'

def test_pig_is_correct():
	pigrec, pigmean = get_sightings(filename, 'Pig')   #See mean_sightings for explaination of how this works
	assert pigrec == 1, 'Number of records for Pig is wrong'
	assert pigmean == 4, 'Mean sightings for pig is wrong'

def test_Mouse_is_correct():
	mouserec, mousemean = get_sightings(filename, 'Mouse')
	assert mouserec == 12, 'Mouse number wrong'
	assert mousemean == 1, 'Mouse mean wrong'

def test_anonymouse_is_correct():
	anirec, animean = get_sightings(filename, 'NotPresent')
	assert anirec == 0, 'Number of anonymous records is wrong'
	assert animean == 0 , 'Mean for anonymous animal rec is wrong'


