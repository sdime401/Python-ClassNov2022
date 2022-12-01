def sales(cart):
    with open("receipt.txt", "w") as grocery_cart:
        order={'tomato':30, 'Thyme':4.50, 'garlic':7.75, 'onions':4, 'fish':9.99, 'pepper':5}
        price_list=[]
        for price in order:
            price_list.append(order[price])
        
        total = sum(price_list)
        total= str(total)
        grocery_cart.write("The total of your grocery is:$ ")  
        grocery_cart.write(total)
        
sales("total")           
