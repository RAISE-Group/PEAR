@pytest.mark.parametrize('index', ['string', 'int', 'float'], indirect=True)
def test_drop_by_str_label(self, index):
    n = len(index)
    drop = index[list(range(5, 10))]
    dropped = index.drop(drop)
    expected = index[list(range(5)) + list(range(10, n))]
    tm.assert_index_equal(dropped, expected)
    dropped = index.drop(index[0])
    expected = index[1:]
    tm.assert_index_equal(dropped, expected)