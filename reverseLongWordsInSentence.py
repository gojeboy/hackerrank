sentence = "SID Instant EFT is a secure   method that allows you to make quick online payments without a credit card"


sent_arrary = sentence.split(" ")

print(sent_arrary)

temp= []
for word in sent_arrary:
    if len(word) > 4:
        a = word.split('')
        a.reverse()
        b = ''.join(a)
        temp.append(b)

    else:
        temp.append(word)




returned_string =' '.join(temp)

print(returned_string)







