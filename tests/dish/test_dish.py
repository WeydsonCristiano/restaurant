from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    prato1 = Dish("Rabanada", 8.5)
    prato2 = Dish("Brioche", 6.0)

    prato1.add_ingredient_dependency(Ingredient("ovos"), 4)

    with pytest.raises(
        TypeError, match="O preço do prato deve ser um número real."
    ):
        Dish("Rabanada", "precoteste")

    with pytest.raises(
        ValueError, match="O preço do prato deve ser maior que zero."
    ):
        Dish("Rabanada", 0)

    assert prato1.nome == "Rabanada"

    assert hash(prato1) == hash(prato1)
    assert hash(prato1) != hash(prato2)

    assert prato1 == prato1

    assert repr(prato1) == "Dish('Rabanada', R$8.50)"

    assert prato1.receita.get(Ingredient("ovos")) == 4

    assert prato1.obter_restricoes() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.EGG,
    }

    assert prato1.obter_ingredientes() == {Ingredient("ovos")}
