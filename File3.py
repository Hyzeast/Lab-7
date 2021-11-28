import requests
from bs4 import BeautifulSoup
import pylab
from file6 import L

r = requests.get("https://www.reddit.com")
page = BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
ryadok1=page.head.title.text
ryadok2=page.body.text
names=["розповідні","питальні","окличні"]
frequency=[0,0,0]
print(frequency)
frequency[0]=ryadok2.count('. ')
frequency[1]=ryadok2.count('? ')
frequency[2]=ryadok2.count('! ')
xdata=names
ydata=frequency
pylab.bar (xdata, ydata)
pylab.savefig('sentences.png', dpi=200)
pylab.show()