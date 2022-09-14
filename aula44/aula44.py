s1 = {1, 2, 3, 4, 5}
print(type(s1))
print(s1)
for x in s1:
    print(x)


s2 = set()
s2.add(1)
s2.add(2)
s2.add('casa')
s2.add((44, 22, 66))
print(s2)
s2.discard('casa')
print(s2)

s3 = set()
s3.update('python')
print(s3)

l1 = [1, 2, 1, 1, 1, 3, 4, 5, 5, 6, 6, 6, 6, 6, 7, 8, 9, 9, 9, 'L', 'U', 'L', 'A']
print(set(l1))


ex1 = {1, 2, 3, 4, 5, 7}
ex2 = {1, 2, 3, 4, 5, 6}
ex3 = ex1 | ex2
print(ex3)
ex4 = ex1 & ex2
print(ex4)
ex5 = ex1 - ex2
print(ex5)
ex6 = ex2 - ex1
print(ex6)
ex7 = ex2 ^ ex1
print(ex7)
ex8 = ex1 ^ ex2
print(ex8)


