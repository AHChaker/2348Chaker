import csv
from datetime import datetime

class Inventory:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, damaged=False):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = datetime.strptime(service_date, "%m/%d/%Y")
        self.damaged = damaged


def read_file(file):
    # create empty dict and store id as key, and rest as values
    inv = {}
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[0]
            values = row[1:]
            inv[item_id] = values
    return inv


def combine_files(manufacturers, prices, service_dates):
    inv = {}
    for item_id, values in manufacturers.items():
        if item_id in prices and item_id in service_dates:
            item_price = prices[item_id][0]
            item_service_date = service_dates[item_id][0]
            item = Inventory(item_id, values[0], values[1], item_price, item_service_date, values[2])
            inv[item_id] = item
    return inv


def output_full_inventory(inv):
    # sort by manufacturer
    def get_manufacturer(item):
        return item.manufacturer

    item_list_sorted = sorted(inv.values(), key=get_manufacturer)

    with open('FullInventory.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in item_list_sorted:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date.strftime('%m/%d/%Y'), item.damaged])


def output_type_inventories(inv):
    # create a dictionary to store items grouped by type
    types_of_items = {}
    for item_id, item in inv.items():
        item_type = item.item_type
        if item_type not in types_of_items:
            #  create empty list to store values in
            types_of_items[item_type] = []
        types_of_items[item_type].append((item.item_id, item.manufacturer, item.price, item.service_date.strftime('%m/%d/%Y'), item.damaged))

    # write each type's inventory to a CSV file
    for item_type, items_list in types_of_items.items():
        filename = f"{item_type.capitalize()}Inventory.csv"

        def get_item_id(item):
            return item[0]
        sorted_items = sorted(items_list, key=get_item_id)


        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            for item in sorted_items:
                writer.writerow(item)


def output_past_service_date(inv):
    current_date = datetime.today()
    items_past_due = []
    for item_id, item in inv.items():
        item_date = item.service_date
        if current_date > item_date:
            items_past_due.append(item)

    def get_service_date(item):
        return item.service_date
    sorted_items_date = sorted(items_past_due, key=get_service_date)

    with open('PastServiceDates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in sorted_items_date:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date.strftime('%m/%d/%Y'), item.damaged])

def output_damaged_inventory(inv):
    damaged_items = []
    for item_id,item in inv.items():
        item_damaged = item.damaged
        if item_damaged:
            damaged_items.append(item)

    def get_price(item):
        return item.price
    sorted_damaged_items = sorted(damaged_items, key=get_price)

    with open('DamagedInventory.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in sorted_damaged_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date.strftime('%m/%d/%Y')])




if __name__ == '__main__':
    manufacturers = read_file('ManufacturerList.csv')
    prices = read_file('PriceList.csv')
    service_dates = read_file('ServiceDatesList.csv')


    items = combine_files(manufacturers, prices, service_dates)


    output_full_inventory(items)
    output_type_inventories(items)
    output_past_service_date(items)
    output_damaged_inventory(items)
