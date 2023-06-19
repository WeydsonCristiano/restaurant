import pandas as pd
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        curr_dish = next(
            (dish for dish in self.menu_data.dishes if dish.name == dish_name),
            None,
        )
        if curr_dish is None:
            raise ValueError("Dish does not exist")
        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        filtered_dishes = [
            dish
            for dish in self.menu_data.dishes
            if not restriction or restriction not in dish.get_restrictions()
        ]

        dish_data = {
            "dish_name": [dish.name for dish in filtered_dishes],
            "ingredients": [
                ", ".join(
                    str(ingredient) for ingredient in dish.get_ingredients()
                )
                for dish in filtered_dishes
            ],
            "price": [dish.price for dish in filtered_dishes],
            "restrictions": [
                ", ".join(str(r) for r in dish.get_restrictions())
                for dish in filtered_dishes
            ],
        }

        return pd.DataFrame(dish_data)
