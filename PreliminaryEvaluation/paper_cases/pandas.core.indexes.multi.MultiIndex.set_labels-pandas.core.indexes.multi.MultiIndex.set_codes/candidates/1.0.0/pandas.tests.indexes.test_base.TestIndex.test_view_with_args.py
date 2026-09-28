@pytest.mark.parametrize('index', ['datetime', 'float', 'int', 'period', 'range', 'repeats', 'timedelta', 'tuples', 'uint'], indirect=True)
def test_view_with_args(self, index):
    index.view('i8')