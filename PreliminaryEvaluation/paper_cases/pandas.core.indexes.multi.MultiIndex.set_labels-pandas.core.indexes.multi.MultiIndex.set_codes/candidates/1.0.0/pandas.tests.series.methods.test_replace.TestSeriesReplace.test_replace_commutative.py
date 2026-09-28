@pytest.mark.parametrize('ser, to_replace, exp', [([1, 2, 3], {1: 2, 2: 3, 3: 4}, [2, 3, 4]), (['1', '2', '3'], {'1': '2', '2': '3', '3': '4'}, ['2', '3', '4'])])
def test_replace_commutative(self, ser, to_replace, exp):
    series = pd.Series(ser)
    expected = pd.Series(exp)
    result = series.replace(to_replace)
    tm.assert_series_equal(result, expected)