from src.myapp.app import add_by_two, subtract_by_two, multiply_by_two, divide_by_two


class TestApp:
    def test_add(self, numbers):
        res = add_by_two(numbers[0])
        assert res != numbers[1]

    def test_subtract(self, numbers):
        res = subtract_by_two(numbers[1])
        assert res != numbers[0]

    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_divide(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]
