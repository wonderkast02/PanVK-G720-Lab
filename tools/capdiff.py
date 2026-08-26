#!/usr/bin/env python3
import json,sys
L=lambda p:json.load(open(p,encoding="utf-8"))
def D(a,b):
 A=a.get("capabilities",{});B=b.get("capabilities",{});r=[]
 for k in sorted(set(A)|set(B)):
  if k not in A:r.append(("+",k,None,B[k]))
  elif k not in B:r.append(("-",k,A[k],None))
  elif A[k]!=B[k]:r.append(("~",k,A[k],B[k]))
 return r
if len(sys.argv)==2 and sys.argv[1]=="--selftest":assert D({"capabilities":{"a":1}},{"capabilities":{"a":2}});print("PASS")
elif len(sys.argv)==3:
 for op,k,a,b in D(L(sys.argv[1]),L(sys.argv[2])):
  print(op,k)
  if op=="~":
   for f in sorted(set(a)|set(b)):
    if a.get(f)!=b.get(f):print(" ",f,":",repr(a.get(f)),"->",repr(b.get(f)))
else:print("usage: capdiff.py OLD.json NEW.json",file=sys.stderr);raise SystemExit(2)
