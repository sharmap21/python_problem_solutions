#!/bin/python3

import os
import sys

class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []  # List to store all added items

    def add(self, item: Item):
        self.items.append(item)  # Add item to the cart

    def total(self) -> int:
        return sum(item.price for item in self.items)  # Sum of all item prices

    def __len__(self):
        return len(self.items)  # Number of items in cart

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())  # Number of items
    items = []  # List to store item objects
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())  # Number of operations
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")  # Number of items in cart
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")  # Total price of items
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)  # Find item by name
            cart.add(item)  # Add item to cart
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
