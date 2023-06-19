import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish = Dish("pizza", 20.0)
    dish2 = Dish("carne", 10.0)

    assert dish.name == "pizza"
    assert dish.price == 20.0
    assert dish.recipe == {}

    assert repr(dish) == "Dish('pizza', R$20.00)"
    assert dish == dish
    assert dish != dish2

    assert hash(dish) == hash(dish)
    assert hash(dish) != hash(dish2)

    ingredient1 = Ingredient("massa de lasanha")
    ingredient2 = Ingredient("massa de ravioli")

    dish.add_ingredient_dependency(ingredient1, 5)
    dish.add_ingredient_dependency(ingredient2, 10)

    assert dish.recipe == {ingredient1: 5, ingredient2: 10}

    assert dish.get_restrictions() == {Restriction.LACTOSE, Restriction.GLUTEN}
    assert dish.get_ingredients() == {ingredient1, ingredient2}

    with pytest.raises(TypeError):
        Dish("pao", "one")

    with pytest.raises(ValueError):
        Dish("pao", -1.0)

    with pytest.raises(ValueError):
        Dish("pao", 0.0)
