@pytest.mark.parametrize('index', ['string', 'int', 'float'], indirect=True)
def test_drop_by_str_label_errors_ignore(self, index):
    n = len(index)
    drop = index[list(range(5, 10))]
    mixed = drop.tolist() + ['foo']
    dropped = index.drop(mixed, errors='ignore')
    expected = index[list(range(5)) + list(range(10, n))]
    tm.assert_index_equal(dropped, expected)
    dropped = index.drop(['foo', 'bar'], errors='ignore')
    expected = index[list(range(n))]
    tm.assert_index_equal(dropped, expected)