import collections

def counter(x):
    finish = collections.Counter(x)
    return finish

def order(List_1,List_2,dictionary):
    dictionary
    sia, Price = [], []
    while True:
        Dict = {"coffee" : 3, "tea" : 4, "beer" : 5}
        shekveta = input("ras inebebt? ")
        if shekveta == "done":
            print("shekveta dasrulebulia")
            print("sul gadasaxdelia ", sum(Price), " lari")
            print("Tqven sheukvetet: ",counter(sia))
            break
        raodenoba = input("ramdeni? ")
        price = List_2[int(shekveta)] * int(raodenoba)
        Price.append(price)
        for a in range(int(raodenoba)):
            sia.append(List_1[int(shekveta)])

def dividing(List_1,List_2,dictionary):
    for i,l in dictionary.items():
        List_1.append(i)
        List_2.append(l)
    
