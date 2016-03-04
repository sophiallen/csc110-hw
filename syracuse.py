

def syr(n):
    sequence = [n]
    while n != 1:
        if n%2 == 0:
            nxt = n/2
        else:
            nxt = 3*n + 1
        sequence.append(nxt)
        n = nxt
    return sequence
    

'''1. Longest sequence'''
def longest():
    long = 0
    num = 0
    for i in range(1, 1001):
        lng = len(syr(i))
        if lng > long:
            long = lng
            num = i
    print(num,"has the longest sequence, with length of", long)

##871, 'has the longest sequence, with length of', 179

'''2. most common sequence length, what ints have it?'''
def lengthFreq():
    freq = {}
    for i in range(1,1001):
        lng = len(syr(i))
        if lng not in freq:
            freq[lng] = [i]
        else:
            freq[lng] += [i]
    mostFreq = 0
    for item in freq:
        if len(freq[item]) > mostFreq:
            mostFreq = item
    print("most freqent length is {0}, these ints have it:{1}".format(mostFreq, freq[mostFreq]))
'''most freqent length is 29, these ints have it:[130, 131, 132, 133, 134, 784, 788, 789, 792, 794, 800, 808,
810, 816, 820, 821, 833, 857, 866, 867, 868, 869, 870, 875, 882, 883, 950, 951, 953, 955]'''


'''3. which ints' sequences have the largest sum?'''
'''largest sum is 4444724.0, n's = [937]'''
def largestSum():
    sums = {}
    for i in range(1,1001):
        seqsum = sum(syr(i))
        if seqsum not in sums:
            sums[seqsum] = [i]
        else:
            sums[seqsum] += [i]
    keys = sums.keys()
    largest = max(keys)
    ints = sums[largest]
    print("largest sum is {0}, n's = {1}".format(largest, ints))
            
        
'''4.whic in or ints have the largest average in their sequence? What is the largest average?'''
'''largest average sum is 25962.0, n's = [703]'''
def largestAvg():
    averages = {}
    for i in range(1,1001):
        seq = syr(i)
        avg = sum(seq)//len(seq)
        if avg in averages:
            averages[avg] += [i]
        else:
            averages[avg] = [i]
    largest = max(averages.keys())
    ints = averages[largest]
    print("largest average sum is {0}, n's = {1}".format(largest, ints))

'''what prime has the largest sequence, and what is its length?'''
def isFactor(f,n):
    remain = n%f
    result = remain ==0
    return result


def factorsOf(n):
    '''return a list of factors of n'''
    factors = []
    for i in range(1, n+1):
        if isFactor(i, n):
            factors.append(i)
    return factors

def isPrime(n):
    truth = len(factorsOf(n)) == 2
    return truth

def longestPrimeSeq():
    nums = range(1, 1001)
    primes = []
    for num in nums:
        if isPrime(num):
            primes.append(num)
    seqlens = {}
    for i in primes:
        lng = len(syr(i))
        if lng in seqlens:
            seqlens[lng] += [i]
        else:
            seqlens[lng] = [i]
    longest = max(seqlens.keys())
    ints = seqlens[longest]
    print("longest sequence of prime is {0}, primes = {1}".format(longest,ints))

    #longest sequence of prime is 174, primes = [937]

'''6.find all n1 and n2 where the length of their sequences added to gether is the same as the
length of the sequence of their sum'''

def simSumLen():
    lens = {}
    matches = []
    for i in range(1, 1001):
        lens[i] = len(syr(i))
    for n1 in lens:
        n2 = n1 + 1
        while (n2 <= 1000):       
            n3 = n1 + n2
            if  (n3 in lens) and (lens[n1] + lens[n2] == lens[n3]):
                matches.append((n1, n2))
            n2 += 1
    return matches
'''There are 1302 n1 and n2 sets where the above conditions are true.'''
    
    


