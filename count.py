def count_products(data):
    products = {} # 建立空字典
    for d in data: 
        name, count = d.split() # 把data清單中每筆字串d用空格拆開, 並建立新清單包含name與count兩字串
        count = int(count) # 字串轉整數, 才能表示為products此字典的value(值)
        if name in products:
            products[name] += count
        else:
            products[name] = count
    return products

print(count_products(['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']))