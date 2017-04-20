#!/usr/bin/env python3 

import sys
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

# length of message (from hints)
# prime factorisation: 7 x 359 x 757
num_bits = 1902341

# physical scales

'''
 The frequency of the radio signal defines the physical scales of the problem
 we can use the relations:
 	lambda = c / frequency
	period t = 1 / frequency
 to derive the length and time scales to use
'''

wl = 452.12919E+6 # wavelength of signal in hertz
l = 0.6630681 # length in metres
t = 2.2117572E-9 # time in seconds

# relevant constants
c = 299792458 # speed of light in metres per second
yr = 31557600 # number of seconds in a year
au = 149597870700 # au in metres

# 

try:
	with open("SETI_message.txt") as inputdata:
		for line in inputdata:
			# read as ASCII representation, need to subtract 48 for correct value
			data = np.fromstring(line, dtype=np.int8, sep='') - 48
except EnvironmentError:
	sys.exit("Couldn't find SETI_message.txt, is it in the same directory as the script?")


# check array is the right size
try:
	data[num_bits - 1]
except:
	sys.exit("SETI_message.txt isn't complete...")

data = data.reshape(7, 1, 757, 359)


# plot the data

'''
 picture #0: axes on the bottom and right side of the box 
 picture #1: counting from 0 to 
 picture #2: counting prime numbers
 picture #3: sine wave
 picture #4: alien picture
 picture #5: picture of their telescopes, modelled on the Square Kilometre array (SKA),
              a picture can be found here https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/SKA_overview.jpg/1024px-SKA_overview.jpg
 picture #6: picture of the alien homeworld, it is a moon orbiting a gas giant
'''

nrow = data.shape[1]
ncol = data.shape[0]

fig = plt.figure(1)
gs = gridspec.GridSpec(nrow, ncol)
plt.title('test')
plt.axis('off')

for (j, k) in np.ndindex(data.shape[:2]):
	ax = fig.add_subplot(gs[nrow - k - 1, j])
	ax.axis('off')
	ax.matshow(data[j, k, :, :], cmap=plt.cm.gray)

plt.show()



# extract data from images pictures

# data in the first two lines of pictures 3,4,5,6

# extracts relevant line of image, converts it to a string and then from
# binary into a decimal number. as the binary numbers in the image 1 and 2
# have the least significant digit to the left rather than to the right,
# as is usual we have to reverse the order of the string before we convert 
# it to its decimal representation

s1 = int(''.join(np.flip(data[3, 0, 0, :], axis=0).astype(str)), 2)
s2 = int(''.join(np.flip(data[3, 0, 1, :], axis=0).astype(str)), 2)

a1 = int(''.join(np.flip(data[4, 0, 0, :], axis=0).astype(str)), 2)
a2 = int(''.join(np.flip(data[4, 0, 1, :], axis=0).astype(str)), 2)

t1 = int(''.join(np.flip(data[5, 0, 0, :], axis=0).astype(str)), 2)
t2 = int(''.join(np.flip(data[5, 0, 1, :], axis=0).astype(str)), 2)

p1 = int(''.join(np.flip(data[6, 0, 0, :], axis=0).astype(str)), 2)
p2 = int(''.join(np.flip(data[6, 0, 1, :], axis=0).astype(str)), 2)


#results

'''
 the scale in the problems is set by s1
 
 the two different numbers in each picture contain 
 information relating to:
 	#1: length information
 	#2: temporal information
'''

# recover time for signal to reach earth given in hint (50 years)
dist = s2/s1 * t / yr 
dist = "{0:.5g}".format(dist) 

print("time for signal to reach earth:", dist, "yrs")

# alien height
alien_h = a1/s1 * l
alien_h = "{0:.5g}".format(alien_h)

print("alien height:", alien_h, "m")

# alien lifetime
alien_l = a2/s1 * t /yr
alien_l = "{0:.5g}".format(alien_l)

print("alien lifetime:", alien_l, "yrs")

# telescope size
tele_s = t1/s1 * l
tele_s = "{0:.5g}".format(tele_s)

print("telescope size:", tele_s, "m")

# communication time
com_t = t2/s1 * t / yr
com_t = "{0:.5g}".format(com_t)

print("time they've been communicating:", com_t, "yrs")

# solar system size
sol_s = p1/s1 * l / au # we expect their solar system to be a comparable size to ours, so use appropriate units
sol_s = "{0:.5g}".format(sol_s)

print("planet distance from star:", sol_s, "AU")

# age of solar system  
age_s = p2/s1 * t / yr
age_s = "{0:.5g}".format(age_s)

print("age of their stellar system:", age_s, "yrs")

