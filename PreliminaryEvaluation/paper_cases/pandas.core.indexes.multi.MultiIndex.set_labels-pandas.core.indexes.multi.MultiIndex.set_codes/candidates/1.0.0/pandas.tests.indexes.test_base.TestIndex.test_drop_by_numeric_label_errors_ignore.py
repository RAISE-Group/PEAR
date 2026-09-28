@pytest.mark.parametrize('key,expected', [(4, Index([1, 2, 3])), ([3, 4, 5], Index([1, 2]))])
def test_drop_by_numeric_label_errors_ignore(self, key, expected):
    index = Index([1, 2, 3])
    dropped = index.drop(key, errors='ignore')
    tm.assert_index_equal(dropped, expected)