'''
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数：它所有的真因子（即除了自身以外的约数）的和，恰好等于它本身，完全数不可能是楔形数、平方数、佩尔数或费波那契数。
例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加， 1 + 2 + 3 = 6 {\displaystyle {{{1}+{2}}+{3}}=6}，恰好等于本身。第二个完全数是28，
它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加， 1 + 2 + 4 + 7 + 14 = 28 {\displaystyle {{{{{1}+{2}}+{4}}+{7}}+{14}}=28}，也恰好等于本身。后面的数是496、8128。 
'''
# This example is find all perfect number below 10000
for n in range(2, 10001,1):
    fact_sum = 0
    for i in range(1,n):
        if (n % i == 0):
            fact_sum = fact_sum + i
    if n == fact_sum:
        print('n = %d' % n)    
