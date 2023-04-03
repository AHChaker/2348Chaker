class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')

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
                print("Item not found in cart. Nothing Removed.")

    def modify_item(self, ItemToPurchase):
        for i in self.cart_items:
            if i.item_name == ItemToPurchase.item_name:
                new_quan = int(input())
                i = ItemToPurchase
                i.item_quantity = new_quan
            else:
                print('Item not found in cart. Nothing removed.')


    def get_num_items_in_cart(self):
        total_quan = 0
        for i in self.cart_items:
            total_quan += i.item_quantity
        return total_quan


    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += i.item_price
        return total_cost

    def print_total(self):
        if len(self.cart_items) != 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}:/n'
                  f'Number of Items: {self.get_num_items_in_cart()}/n'
                  f'/n')
            for item in self.cart_items:
                item.print_item_cost()
            print(f'/n'
                  f'Total {self.get_cost_of_cart()}')
        else:
            print('SHOPPING CART IS EMPTY')


    def print_description(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}:/n'
              f'Item Descriptions')

        for i in self.cart_items:
            return i.print_item_description()

    def menuOfChoices(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")

    def print_menu(self):
        choice = ''
        choice = str(input())
        while choice != "q":
            if choice == 'o':
                print("OUTPUT SHOPPING CART")
                self.print_total()
            if choice == 'i':
                print('OUTPUT ITEMS\' DESCRIPTIONS')
                self.print_total()
            if choice == 'a':
                print('Enter the item name:')
                i_name = input()
                print('Enter the item description:')
                i_descrip = input()
                print('Enter the item price:')
                i_price = input()
                print('Enter the item quantity:')
                i_quantity = input()

                item = ItemToPurchase(i_name,i_descrip, i_price, i_quantity)

                self.add_item(item)
            if choice == 'r':
                print("REMOVE ITEM FROM CART")
                print('Enter name of item to remove:')
                i_remove = input()
                self.remove_item(i_remove)



if __name__ == "__main__":
    print("Enter customer's name:")
    cust_name = str(input())
    print("Enter today's date:")
    todays_date = input()

    print(f'Customer Name: {cust_name}')
    print(f'Today\'s date: {todays_date}')
