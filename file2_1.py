from array import *
import pylab

text = input("yourtext")

letters_str='abcdefghijklmnopqrstuvwxyz'
letters=list(letters_str)
frequency=[]

L=len(letters)

for i in range(L):
    elem=letters[i]
    fr=text.count(elem)
    frequency.append(fr)
xdata=letters
ydata=frequency
pylab.bar (xdata, ydata)
pylab.savefig('2.png', dpi=200)

pylab.show()
