def dec_to_bin(x):
    return int(bin(x)[2:])

def main(a,b,c):

    x = str(dec_to_bin(b))
    print(x)
    ###############################################
    x_reverse = x[::-1]
    x_list = list(x_reverse)
    print(x_list)
    ###############################################
    two = []
    for i in x_list:
        if i == "1":
            two.append(x_list.index(i))
            x_list[x_list.index(i)] = "0"
    print(two)
    ###############################################
    multiplication = 1
    for i in two:
        temp = a ** (2 ** i) % c
        multiplication = multiplication*temp
    ###############################################
    m = multiplication % c
    print(m)



main(667,937,2537)