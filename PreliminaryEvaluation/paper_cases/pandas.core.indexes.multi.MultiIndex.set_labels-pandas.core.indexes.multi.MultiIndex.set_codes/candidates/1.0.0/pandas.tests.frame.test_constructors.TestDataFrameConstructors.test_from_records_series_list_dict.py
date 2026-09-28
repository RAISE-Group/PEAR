def test_from_records_series_list_dict(self):
    expected = DataFrame([[{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]]).T
    data = Series([[{'a': 1, 'b': 2}], [{'a': 3, 'b': 4}]])
    result = DataFrame.from_records(data)
    tm.assert_frame_equal(result, expected)