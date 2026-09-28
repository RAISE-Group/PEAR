@pytest.mark.parametrize('vals', [[1, 2.0 + 3j, 4.0], ['a', 'b', 'c']])
def test_format_missing(self, vals, nulls_fixture):
    vals = list(vals)
    vals.append(nulls_fixture)
    index = Index(vals)
    formatted = index.format()
    expected = [str(index[0]), str(index[1]), str(index[2]), 'NaN']
    assert formatted == expected
    assert index[3] is nulls_fixture