def test_append_tuples(self):
    s = pd.Series([1, 2, 3])
    list_input = [s, s]
    tuple_input = (s, s)
    expected = s.append(list_input)
    result = s.append(tuple_input)
    tm.assert_series_equal(expected, result)