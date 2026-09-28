def compare(self, formatter, input, output):
    formatted_input = formatter(input)
    assert formatted_input == output