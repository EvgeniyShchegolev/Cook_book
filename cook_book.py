class Dish:
    def __init__(self, name_dish):
        self.name_dish = name_dish
        self.ingredient = []

    def show_ingredients_for_person(self, number_person):
        print(f'\n{self.name_dish.capitalize()}:')
        for ingredient in self.ingredient:
            print(f'{ingredient.name_ingredient}, {ingredient.count * number_person} {ingredient.measure}')


class Ingredient:
    def __init__(self, name_ingredient, count, measure):
        self.name_ingredient = name_ingredient
        self.count = count
        self.measure = measure


def count_ingerdients_dishes(number_person):
    for dish in cook_book:
        dish.show_ingredients_for_person(number_person)


potato = Ingredient('картофель', 100, 'гр.')
carrot = Ingredient('морковь', 50, 'гр.')
cucumbers = Ingredient('огурцы', 50, 'гр.')
polka_dots = Ingredient('горошек', 30, 'гр.')
mayonnaise = Ingredient('майонез', 70, 'мл.')

cheese = Ingredient('сыр', 50, 'гр.')
tomato = Ingredient('томаты', 50, 'гр.')
dough = Ingredient('тесто', 100, 'гр.')
bacon = Ingredient('бекон', 30, 'гр.')
sausage = Ingredient('колбаса', 30, 'гр.')
mushroom = Ingredient('грибы', 20, 'гр.')

persimmon = Ingredient('хурма', 60, 'гр.')
kiwi = Ingredient('киви', 60, 'гр.')
curd = Ingredient('творог', 60, 'гр.')
sugar = Ingredient('сахар', 10, 'гр.')
honey = Ingredient('мед', 50, 'мл.')

salad = Dish('салат')
salad.ingredient = [potato, carrot, cucumbers, polka_dots, mayonnaise]

pizza = Dish('пицца')
pizza.ingredient = [cheese, tomato, dough, bacon, sausage, mushroom]

fruit_dessert = Dish('фруктовый десерт')
fruit_dessert.ingredient = [persimmon, kiwi, curd, sugar, honey]

cook_book = [salad, pizza, fruit_dessert]

count_ingerdients_dishes(int(input('Введите количество персон: ')))
