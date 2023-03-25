#Hamid Chaker 2060843
class FoodItem():

    def __init__(self, name="None", fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food1 = FoodItem()

    item1 = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    amount_serv = float(input())

    food2 = FoodItem(item1, amount_fat, amount_carbs, amount_protein)

    food1.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(amount_serv, food1.get_calories(amount_serv)))
    print()
    food2.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(amount_serv, food2.get_calories(amount_serv)))