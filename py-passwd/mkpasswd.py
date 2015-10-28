#!/usr/bin/env python
#
# Usage:  mkpasswd.py <cleartext> <salt>
#
import crypt
import sys

cleartext = sys.argv[1]
salt = sys.argv[2]


crypttext = crypt.crypt(cleartext, salt)

print("Cleartext:  {}".format(cleartext))
print("Crypttext:  {}".format(crypttext))
