i=1

print('{0}.TITLE() FUNCTION'.format(i))
word='i am Martian'
print(word.title())
i=2

print('{0}.TITLE() WITH APOSTROPHES'.format(i))
word="they don't know"
print(word.title())
i=3

print('{0}.STARTSWITH() WITHOUT START AND END PARAMETERS'.format(i))
result=word.startswith('they')
print(result)
i=4

print('{0}.STARTsWITH() WITH START AND END PARAMETERS'.format(i))
result=word.startswith('know',11)
print(result)

