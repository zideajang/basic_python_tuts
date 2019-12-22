# import item as Item

# print(Item)

class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name

    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ',' + str(self.value) + ', ' + str(self.weight) + '>'
        return result

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def greedy(items, maxWeight, keyFunction):
    print('greedy')
    itemsCopy = sorted(items,key=keyFunction,reverse=True)
    result = []
    totalValue, totalWeight = 0.0,0.0
    print(itemsCopy)
    for i in range(len(itemsCopy)):
        print(itemsCopy[i].getWeight())
        # if(totalWeight + itemsCopy[i]).getWeight())<= maxWeight:
        #     result.append(itemsCopy[i])
        #     totalWeight += itemsCopy[i].getWeight()
        #     totalValue += itemsCopy[i].getValue()
    return (result,totalValue)

def buildItems():
    names = ['item1','item2','item3','item4','item5','item6']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    print(len(values))
    for i in range(len(values)):
        item = Item(names[i],values[i],weights[i])
        Items.append(item)
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is',val)
    for item in taken:
        print(' ',item)

def testGreedys(maxWeight = 20):
    items = buildItems()
    print('Use greedy by value to fill knapsack of size',maxWeight)
    testGreedy(items,maxWeight,value)

if __name__ == '__main__':
    testGreedys()
    