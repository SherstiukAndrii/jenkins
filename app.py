VERY_LONG_CONSTANT_NAME_TO_DEMONSTRATE_LINE_LENGTH_VIOLATION = (
    "This is a very long string that Pylint will flag as C0301 "
    "(Line too long)"
)


def calculate_something(a, b):
    c = a + b
    return c


class MyDataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        processed_data = [x * 2 for x in self.data]
        return processed_data

    def count(self):
        return len(self.data)


def main():
    result = calculate_something(5, 7)
    processor = MyDataProcessor([1, 2, 3])
    final_result = processor.process()
    print(f"Result: {result}, Final: {final_result}")


if __name__ == "__main__":
    main()
