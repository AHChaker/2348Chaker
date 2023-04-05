#Hamid Chaker 2060843
class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${float(self.item_price)} = ${int(self.item_quantity) * float(self.item_price)}')

    def print_item_description(self):
        print(f'{self.item_description}')


class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item):
        for i in self.cart_items:
            if i.item_name == item:
                return self.cart_items.remove(i)
            else:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToPurchase.item_name:
                self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quan = 0
        for i in self.cart_items:
            total_quan += int(i.item_quantity)
        return total_quan

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += i.item_price * i.item_quantity
        return total_cost

    def print_total(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}\n'
              f'Number of Items: {self.get_num_items_in_cart()}\n')
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        for item in self.cart_items:
            item.print_item_cost(item)
        print(f'\nTotal: ${self.get_cost_of_cart()}')

    def print_description(self):
        if len(self.cart_items) != 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}:/n'
                  f'Item Descriptions')

        for i in self.cart_items:
            return i.print_item_description()

    def print_menu(self):
        menu = "\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit"
        choice = ''
        choice_list = ['a', 'r', 'c', 'i', 'o', 'q']
        while choice != "q":
                print(menu)
                print('')
                print('Choose an option:')
                choice = input()
                if choice == 'o':
                    print("OUTPUT SHOPPING CART")
                    self.print_total()

                elif choice == 'i':
                    print('OUTPUT ITEMS\' DESCRIPTIONS')
                    self.print_description()

                elif choice == 'a':
                    print('\nADD ITEM TO CART')
                    print('Enter the item name:')
                    i_name = input()
                    print('Enter the item description:')
                    i_descrip = input()
                    print('Enter the item price:')
                    i_price = input()
                    print('Enter the item quantity:')
                    i_quantity = input()

                    item = ItemToPurchase
                    item.item_name = i_name
                    item.item_price = i_price
                    item.item_quantity = i_quantity
                    item.item_description = i_descrip
                    self.add_item(item)

                elif choice == 'r':
                    print("REMOVE ITEM FROM CART")
                    print('Enter name of item to remove:')
                    i_remove = input()
                    self.remove_item(i_remove)

                elif choice == 'c':
                    print("CHANGE ITEM QUANTITY")
                    print("Enter the item name:")
                    item_name = input()
                    print("Enter the new quantity:")
                    new_quantity = input()

                    item = ItemToPurchase()
                    item.item_name = item_name
                    item.item_quantity = new_quantity

                    self.modify_item(item)


if __name__ == "__main__":
    print("Enter customer's name:")
    cust_name = str(input())
    print("Enter today's date:")
    todays_date = input()

    print('')
    print(f'Customer name: {cust_name}')
    print(f'Today\'s date: {todays_date}')
    print('')

    new_cust = ShoppingCart(cust_name, todays_date)
    new_cust.print_menu()