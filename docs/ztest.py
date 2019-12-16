MyList = ['GR9608100010000001234567890','DE89370400440532013000']

# print(MyList[0][-4:])
# print(MyList[0][:-4])
# print(MyList[1][-4:])
# print(MyList[1][:-4])

list2= MyList[0][:-4]
list2 = '---'
print(list2)

list1=MyList[0][-4:]
print(list1)

list3 = list2+list1
print(list3)

for ele in MyList:
    list2=ele[:-4]
    list2='---'
    list1=ele[-4:]
    print(list1)
    list3=list2+list1
    print(list3)
