from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("farinha")

    assert ingredient1.__hash__() == ingredient3.__hash__()
    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert ingredient1.__eq__(ingredient3)
    assert ingredient1.__repr__() == "Ingredient('farinha')"
    assert ingredient1.name == "farinha"
    assert ingredient2.name != "veganbacon"
    assert ingredient1.restrictions == {Restriction.GLUTEN}
