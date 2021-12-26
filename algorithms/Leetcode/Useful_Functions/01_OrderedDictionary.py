from collections import OrderedDict

strng = 'GeeksForGeeks'
ord_dict = OrderedDict()
for each in strng:
    if each in ord_dict:
        # ord_dict.move_to_end(each, last=True)
        ord_dict[each]+=1
    else:
        # ord_dict.move_to_end(each, last=True)
        ord_dict[each]=1

ord_dict.move_to_end('G')

print("Original Dictionary")
print(ord_dict)

# Pop the key from last
ord_dict.popitem()
print("\nAfter Deleting Last item :")
print(ord_dict)

# Pop the key from beginning
ord_dict.popitem(last = False)
print("\nAfter Deleting Key from Beginning :")
print(ord_dict)
