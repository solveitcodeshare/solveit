# problem 2

from timeit import timeit

start = '''
import math
#how to generate primes up to N
N = 100

n = 2

def get_primes(n):
    sieve = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        #print(i)
        if sieve[i]:
            #print(sieve[i*i::2*i])
            #print(int((n-i*i-1)/(2*i)+1))
            #print("sieve[",i,"*",i,"::2*",i,"]=[False]*int((",n,"-",i,"*",i,"-1)/(2*",i,")+1+))")
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    #print(sieve)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
    '''
itr = '''

primes = get_primes(N)


#print(len(primes))
#print(N/math.log(n))

'''

time = timeit(stmt=itr,setup=start,number=100)

print(time)



#input file shuld be given via stdinput e.g. python p2_2017_goldbachs.py < input/testp1_2017_1.in
