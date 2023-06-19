import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data = []
        self.read_data(source_path)

    def read_data(self, source_path: str) -> None:
        with open(source_path, newline="") as csv_file:
            data = csv.reader(csv_file)
            _, *data = data

            dish_dict = dict()

            for row in data:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                recipe_amount = int(row[3])

                if dish_name in dish_dict:
                    dish_dict[dish_name].add_ingredient_dependency(
                        Ingredient(ingredient_name), recipe_amount
                    )
                else:
                    dish = Dish(dish_name, price)
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name), recipe_amount
                    )
                    dish_dict[dish_name] = dish

            self.dishes = set(dish_dict.values())
