def translate(Eng_L):
    Swe_L=[]
    d={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt","year":"år"}
    for Eng_W in Eng_L:
        Swe_L.append(d[Eng_W])
    return Swe_L

Eng_L=['merry','christmas','and','happy','new','year']
Swe_L=translate(Eng_L)
print(Swe_L)