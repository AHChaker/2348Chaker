import csv

class OutputItems:
    def __init__(self, item_id, item_man, item_type, item_price, item_date, item_damaged):
        self.item_id = item_id
        self.item_man = item_man
        self.item_type = item_type
        self.item_price = item_price
        self.item_date = item_date
        self.item_damaged = item_damaged

def read_csv_file(filename):
    items = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            #item_id as dictionary key
            item_id = line[0]
            #rest of the data as its values
            attributes = line[1:]
            #make dictionary
            items[item_id] = attributes
        return items


def sort_items(items):
    #sort by manufacturer x[1]
    return dict(sorted(items.items(), key=lambda x: x[1]))



