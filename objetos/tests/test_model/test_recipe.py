from django.test import TestCase

from objetos.models import Recipe, User


class RecipeTestCase(TestCase):
    def test_str(self):
        user = User.objects.create()
        recipe = Recipe.objects.create(description='Some description', creator=user)

        self.assertIsInstance(recipe, Recipe)
        self.assertEqual(recipe.description, str(recipe))
