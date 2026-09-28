@pytest.fixture
def df(self):
    return DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'b', 'c'], 'C': [1, 2, 3]})