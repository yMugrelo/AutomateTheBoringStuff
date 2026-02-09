def printingMarketList(itemsDict, leftWidth, rightWidth):
    print("Marketlist items: ".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))

picnicItems = {'Watermelon': 2, 'Rice': 12, 'Beef': 4, 'cookies': 8000}
printingMarketList(picnicItems, 12, 4)
printingMarketList(picnicItems, 20, 8)