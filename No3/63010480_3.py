print("*** Reading E-Book ***")
text, hl = input("Text , Highlight : ").split(",")
text2 = text
a = int(0)
for x in text:
    if x == hl:
        text2 = text2[:a+1] + "]" + text2[a+1:]
        text2 = text2[:a] + "[" + text2[a:]
        a += 2
    a += 1
print(text2)
