import sys

def power(x,n):
	if n == 1:
		return x
	elif n % 2 == 0:
		return power(x * x, n/2)
	elif n > 2 and n % 2 != 0:
		return x * power(x * x, (n-1)/2)

def mod(p,n,m):
	if p == 0:
		return 1
	q = mod(p // 2,n,m)
	if p % 2 == 0:
		return (q*q) % m
	else:
		return (((q*n) % m) *q) % m

#DH
#public keys
p = 23612983189237981723
g = 19121236178236781263

#private naturals
a = 25123761235671253512352153615273571253615235123571253721537612546542153519284798
b = 39987615312546192470912756127460192843192751829631902830912784916234891289371263
secretKey = ''

aa = a;
bb = b;

#AA = power(g,aa) % p
#BB = power(g,bb) % p

#Kaa = power(BB,aa) % p
#Kbb = power(AA,bb) % p

A = mod(aa,g,p)
B = mod(bb,g,p)

Ka = mod(aa,B,p)
Kb = mod(bb,A,p)

secretKey = Ka

print("Public keys(a,b) =", p,"|",g,sep=" ")
print("Private keys(Ka,Kb)=", Ka,"|",Kb,sep=" ")
#print("Private keys(Kaa,Kbb)=", Kaa,"|",Kbb,sep=" ")