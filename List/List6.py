def generate_n_chars(num, char):
    g_char=''
    for iter in range(num):
        g_char+=char
    return g_char
        

num=5
char='x'
print(generate_n_chars(num,char))