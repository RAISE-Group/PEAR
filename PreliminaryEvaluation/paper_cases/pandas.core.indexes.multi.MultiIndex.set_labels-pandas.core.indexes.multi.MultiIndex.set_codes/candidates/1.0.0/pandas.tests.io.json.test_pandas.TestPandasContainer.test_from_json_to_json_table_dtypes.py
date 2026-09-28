def test_from_json_to_json_table_dtypes(self):
    expected = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0], 'c': ['5', '6']})
    dfjson = expected.to_json(orient='table')
    result = pd.read_json(dfjson, orient='table')
    tm.assert_frame_equal(result, expected)