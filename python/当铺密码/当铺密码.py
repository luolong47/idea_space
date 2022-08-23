

if __name__ == '__main__':
    dh = '田口由中人工大土士王夫井羊壮'
    ds = '00123455567899'

    cip = '王夫 井工 夫口 由中人 井中 夫夫 由中大'
    s = ''
    for i in cip:
        if i in dh:
            s += ds[dh.index(i)]
        else:
            s += ' '
    # print(s)

    ll = s.split(" ")
    t = ''
    for i in range(0, len(ll)):
        t += chr(int(ll[i]) + i + 1)
    print('t=', t, '\t\tt.lower()=', t.lower())