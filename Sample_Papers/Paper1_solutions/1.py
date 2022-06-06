'''
Given a string of words delimited by spaces, your task is to write a Python script to reverse the characters of words in the string. For example, given "hello world here", display "olleh dlrow ereh". Sample input
"the light heart lives long"
Sample output
"eht thgil traeh sevil gnol"
'''
a=input()
l=a.split()
for i in range(len(l)):
    l[i]=l[i][-1::-1]
out=" ".join(l)
print(out)
