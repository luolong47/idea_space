# --encoding='utf-8'--

import hashlib
import string

if __name__ == '__main__':

    h = hashlib.md5()

    a1 = string.ascii_letters
    a2 = string.ascii_letters
    a3 = string.ascii_letters
    for a11 in a1:
        for a22 in a2:
            for a33 in a3:
                str_ori = f'TASC{a11}O3RJMV{a22}WDJKX{a33}ZM'
                h.update(str_ori.encode())
                r = h.hexdigest()
                if 'e903' in r and '4dab' in r:
                    # E903???4DAB????0
                    # 8?????51?80??8
                    # A?
                    print(str_ori)
                    print(r)
                    exit(0)
