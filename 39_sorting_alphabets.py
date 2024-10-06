# This is a simple program to display the sorted words from the sentence

a = "Harry Potter and the Goblet of Fire"

w= a.split()
print(w)

for i in range (len(w)):
    w[i]=w[i].lower()


print(w)

w.sort()
print(w)
for i in w:
    print(i)