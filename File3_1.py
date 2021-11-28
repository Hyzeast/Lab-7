import pylab

with open("yourtext", "r") as file:
    data = file.read().replace('\n', '')
    rozp = 0
    pyt = 0
    okl = 0
    trikrapki = 0
    for char in data:
        if char == "!":
            okl = okl + 1
        elif char == "…":
            trikrapki = trikrapki + 1
        elif char == ".":
            rozp = rozp + 1
        elif char == "?":
            pyt = pyt + 1
sentences = [rozp, pyt, okl, trikrapki]
ydata = sentences
xdata = ("Розповідні", "Питальні", "Окличні", "Три крапки")

pylab.bar (xdata, ydata)
pylab.savefig('sentences.png', dpi=200)
pylab.show()