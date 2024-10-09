# This is a simple program to display the sorted words from the sentence

a = "Harry Potter and the Goblet of Fire"

# We have to sort the string in list to move forward

w= a.split()
print(w)

for i in range (len(w)):
    w[i]=w[i].lower()


print(w)

w.sort()
print(w)
for i in w:
    print(i)