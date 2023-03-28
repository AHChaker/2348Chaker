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
            if i == ItemToPurchase:
                new_quan = int(input())
                self.item_quantity = new_quan
            else:
                print('Item not found in cart. Nothing removed.')


    def get_num_items_in_cart(self):


    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

    def print_description(self):
        pass