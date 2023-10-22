import unittest
from main import Cat  # Import your Cat class from your actual module

class TestCat(unittest.TestCase):
    def test_initial_age(self):
        cat = Cat()
        age = cat.getAge()
        self.assertTrue(5 <= age <= 10, "Initial age is not between 5 and 10")
    
    def test_set_name(self):
        cat = Cat()
        cat.setName("Whiskers")
        self.assertEqual(cat.getName(), "Whiskers", "Name setting failed")
        self.assertEqual(cat.getNames(), [], "Empty name added to old names")
    
    def test_get_average_name_length(self):
        cat = Cat()
        cat.setName("Whiskers")
        cat.setName("Fluffy")
        cat.setName("Mirai")
        self.assertEqual(cat.getNames(), ["Whiskers", "Fluffy"], "Old names are not matching")
        self.assertEqual(cat.getAverageNameLength(), 7.0, "Average name length calculation is incorrect")
    
    def test_speak_method_age_increase(self):
        cat = Cat()
        cat.setAge(8)

        for _ in range(4):
            cat.speak()
        age = cat.getAge()
        self.assertEqual(age, 8, "Age should not increase to 9 after speaking four times")
        cat.speak()
        age = cat.getAge()
        self.assertEqual(age, 9, "Age should increase to 9 after speaking five times")
        cat.speak()
        age = cat.getAge()
        self.assertEqual(age, 9, "Age should remain to 9 after speaking six times")

if __name__ == '__main__':
    unittest.main()
