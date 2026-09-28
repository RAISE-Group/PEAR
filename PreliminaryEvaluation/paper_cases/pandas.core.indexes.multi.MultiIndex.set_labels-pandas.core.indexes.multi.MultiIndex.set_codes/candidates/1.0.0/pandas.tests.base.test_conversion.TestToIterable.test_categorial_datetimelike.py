@pytest.mark.parametrize('method', [lambda x: x.tolist(), lambda x: x.to_list(), lambda x: list(x), lambda x: list(x.__iter__())], ids=['tolist', 'to_list', 'list', 'iter'])
def test_categorial_datetimelike(self, method):
    i = CategoricalIndex([Timestamp('1999-12-31'), Timestamp('2000-12-31')])
    result = method(i)[0]
    assert isinstance(result, Timestamp)