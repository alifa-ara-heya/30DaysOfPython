'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''


filename = open('./day_28/mbox-short.txt')
counts = dict()
lst = list()
for line in filename:
    if line.startswith('From '):
        words = line.split()
        for word in words:
            persons = words[1]
        lst.append(persons)
#print(lst)

            
for person in lst:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] = counts[person] + 1

# print(counts)
'''output:  {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1} '''

largest_value = -1
for key in counts:
    if counts[key] > largest_value:
        largest_key = key
        largest_value = counts[key]
print(largest_key, largest_value)