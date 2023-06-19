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
        dishes = [
            {
                "dish_name": dish.name,
                "ingredients": dish.get_ingredients(),
                "price": dish.price,
                "restrictions": dish.get_restrictions(),
            }
            for dish in menu.menu_data.dishes
        ]
        df = pd.DataFrame(dishes)
        if restriction is not None:
            print(restriction)
            return df.loc[
                df["restrictions"].apply(
                    lambda restrictions: restriction not in restrictions
                )
            ]
        else:
            return df


menu = MenuBuilder()
