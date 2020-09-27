def donvi(n9,m9):
    if n9 == 0:
        n11 = ""
    elif n9 == 1:
        if m9 > 1:
            n11 = "mốt"
        else:
            n11 = "một"
    elif n9 == 2:
        n11 = "hai"
    elif n9 == 3:
        n11 = "ba"
    elif n9 == 4:
        n11 = "bốn"
    elif n9 == 5:
        if m9 == 0:
            n11 = "năm"
        else:
            n11 = "lăm"
    elif n9 == 6:
        n11 = "sáu"
    elif n9 == 7:
        n11 = "bảy"
    elif n9 == 8:
        n11 = "tám"
    elif n9 == 9:
        n11 = "chín"
    return n11

def chuc(m9,n9,k9,l9):
    if m9 == 0:
        if m9 == 0 and n9 == 0:
            m11 = ""
        elif k9 == 0 and l9 == 0 and n9 != 0:
            m11 = ""
        else:
            m11 = "lẻ"
    elif m9 == 1:
        m11 = "mười"
    elif m9 == 2:
        m11 = "hai"
    elif m9 == 3:
        m11 = "ba"
    elif m9 == 4:
        m11 = "bốn"
    elif m9 == 5:
        m11 = "năm"
    elif m9 == 6:
        m11 = "sáu"
    elif m9 == 7:
        m11 = "bảy"
    elif m9 == 8:
        m11 = "tám"
    elif m9 == 9:
        m11 = "chín"
    return m11
def tram(l9,j9,k9):
    if l9 == 0:
        if  l9 == 0 and l9 == 0:
            l11 = ""
        elif j9 == 0 and k9 == 0 and l9 != 0:
            l11 = "không trăm"
    elif l9 == 1:
        l11 = "một"
    elif l9 == 2:
        l11 = "hai"
    elif l9 == 3:
        l11 = "ba"
    elif l9 == 4:
        l11 = "bốn"
    elif l9 == 5:
        l11 = "năm"
    elif l9 == 6:
        l11 = "sáu"
    elif l9 == 7:
        l11 = "bảy"
    elif l9 == 8:
        l11 = "tám"
    elif l9 == 9:
        l11 = "chín"
    return l11
def muoii(m9):
    if m9 == 0:
        m12 =  ""
    elif m9 == 1:
        m12 = ""
    else:
        m12 = "mươi"
    return m12
def tramm(l9):
    if l9 == 0:
        l12 = ""
    else:
        l12 = "trăm"
    return l12

def chucPlus(g9,f9,h9):
    if g9 == 0:
        if f9 != 0 and h9 != 0:
            g11 = "lẻ"
        else:
            g11 = ""
    elif g9 == 1:
        g11 = "mười"
    elif g9 == 2:
        g11 = "hai"
    elif g9 == 3:
        g11 = "ba"
    elif g9 == 4:
        g11 = "bốn"
    elif g9 == 5:
        g11 = "năm"
    elif g9 == 6:
        g11 = "sáu"
    elif g9 == 7:
        g11 = "bảy"
    elif g9 == 8:
        g11 = "tám"
    elif g9 == 9:
        g11 = "chín"
    return g11

def tramPlus(f9):
    if f9 == 0:
        f11 = ""
    elif f9 == 1:
        f11 = "một"
    elif f9 == 2:
        f11 = "hai"
    elif f9 == 3:
        f11 = "ba"
    elif f9 == 4:
        f11 = "bốn"
    elif f9 == 5:
        f11 = "năm"
    elif f9 == 6:
        f11 = "sáu"
    elif f9 == 7:
        f11 = "bảy"
    elif f9 == 8:
        f11 = "tám"
    elif f9 == 9:
        f11 = "chín"
    return f11

def sum(a,b,c):
    return a + b + c

def main():
    num = 100000000000
    numList = [int(x) for x in str(num)]
    while(len(numList) < 12):
        numList.insert(0,0)
    print(numList)

    c9 = numList[0]
    d9 = numList[1]
    e9 = numList[2]
    f9 = numList[3]
    g9 = numList[4]
    h9 = numList[5]
    i9 = numList[6]
    j9 = numList[7]
    k9 = numList[8]
    l9 = numList[9]
    m9 = numList[10]
    n9 = numList[11]

    c10 = c9
    d10 = sum(c9, d9, 0)
    e10 = sum(c9, d9, e9)
    f10 = f9
    g10 = sum(f9, g9, 0)
    h10 = sum(f9, g9, h9)
    i10 = i9
    j10 = sum(i9, j9, 0)
    k10 = sum(i9, j9, k9)
    l10 = l9
    m10 = sum(l9, m9, 0)
    n10 = sum(l9, m9, n9)

    print(c10,d10,e10,f10,g10,h10,i10,j10,k10,l10,m10,n10)

    n11 = donvi(n9,m9)
    m11 = chuc(m9,n9,k9,l9)
    l11 = tram(l9,j9,k9)
    m12 = muoii(m9)
    l12 = tramm(l9)

    k11 = donvi(k9,j9)
    j11 = chuc(j9,k9,h9,i9)
    i11 = tram(i9,g9,h9)
    j12 = muoii(j9)
    i12 = tramm(i9)

    h11 = donvi(h9,g9)
    g11 = chucPlus(g9,f9,h9)
    f11 = tramPlus(f9)
    g12 = muoii(g9)
    f12 = tramm(f9)

    e11 = donvi(e9,d9)
    d11 = chucPlus(d9,c9,e9)
    c11 = tramPlus(c9)
    d12 = muoii(d9)
    c12 = tramm(c9)



    if k9 == 0 and k10 == 0:
        k12 = ""
    else:
        k12 = "ngàn"

    if h9 == 0 and h10 == 0:
        h12 = ""
    else:
        h12 = "triệu"

    if e9 == 0 and e10 == 0:
        e12 = ""
    else:
        e12 = "tỷ"










    print(c11,c12,d11,d12,e11,e12,f11,f12,g11,g12,h11,h12,i11,i12,j11,j12,k11,k12,l11,l12, m11,m12, n11)





main()