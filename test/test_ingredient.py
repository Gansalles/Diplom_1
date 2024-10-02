import data
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        assert ingredient.get_price() == data.INGREDIENT_PRICE

    def test_get_name(self):
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        assert ingredient.get_name() == data.INGREDIENT_NAME

    def test_get_type(self):
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        assert ingredient.get_type() == data.INGREDIENT_TYPE
