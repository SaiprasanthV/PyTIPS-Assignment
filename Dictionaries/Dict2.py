def char_freq(st1):
    d=dict()
    for ch1 in st1:
        d[ch1]=d.get(ch1,0)+1
    print (d)

st1="abbabcbdbabdbdbabababcbcbab"
char_freq(st1)