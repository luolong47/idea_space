#!/usr/bin/env python
# -*- coding: utf-8 -*-

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


e1 = 773
e2 = 839
n = 6266565720726907265997241358331585417095726146341989755538017122981360742813498401533594757088796536341941659691259323065631249
c1 = 3453520592723443935451151545245025864232388871721682326408915024349804062041976702364728660682912396903968193981131553111537349
c2 = 5672818026816293344070119332536629619457163570036305296869053532293105379690793386019065754465292867769521736414170803238309535

a, r, s = egcd(e1, e2)
# print a,r,s

if r < 0:
    r = -r
    c1 = modinv(c1, n)

if s < 0:
    s = -s
    c2 = modinv(c2, n)

flag = pow(c1, r) * pow(c2, s) % n

print(flag)

ff = [102, 108, 97, 103, 123, 119, 104, 101, 110, 119, 101, 116, 104, 105, 110, 107, 105, 116, 105, 115, 112, 111, 115,
      115, 105, 98, 108, 101, 125]
s = ''
for f in ff:
    s += chr(f)
print(s)
