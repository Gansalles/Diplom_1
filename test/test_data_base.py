from praktikum.database import Database


class TestDataBase:

    def test_available_buns(self):
        db = Database()
        available_buns = db.available_buns()
        expected_result = ['black bun', 'white bun', 'red bun']
        bun_names_list = [bun.get_name() for bun in available_buns]
        assert expected_result == bun_names_list

    def test_available_ingredients(self):
        db = Database()
        expected_buns_length = 6
        available_ingredients = db.available_ingredients()
        expected_result = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage']
        ingredient_name_list = [ingredient.get_name() for ingredient in available_ingredients]
        assert expected_result == ingredient_name_list
