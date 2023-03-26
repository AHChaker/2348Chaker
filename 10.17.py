class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')


if __name__ == "__main__":

    items1 = ItemToPurchase()
    items2 = ItemToPurchase()

    print("Item 1")
    print("Enter the item name:")
    item1 = input()
    print("Enter the item price:")
    item1_price = int(input())
    print("Enter the item quantity:")
    item1_quan = int(input())

    print()
    print("Item 2")
    print("Enter the item name:")
    item2 = input()
    print("Enter the item price:")
    item2_price = int(input())
    print("Enter the item quantity:")
    item2_quan = int(input())

    items1.item_name = item1
    items1.item_price = item1_price
    items1.item_quantity = item1_quan

    items2.item_name = item2
    items2.item_price = item2_price
    items2.item_quantity = item2_quan
    print()
    print("TOTAL COST")
    items1.print_item_cost()
    items2.print_item_cost()
    print()
    print(f'Total: ${(items1.item_price*items1.item_quantity)+(items2.item_price*items2.item_quantity)}')