def test_to_records_with_unicode_column_names(self):
    result = DataFrame(data={'accented_name_é': [1.0]}).to_records()
    expected = np.rec.array([(0, 1.0)], dtype={'names': ['index', 'accented_name_é'], 'formats': ['=i8', '=f8']})
    tm.assert_almost_equal(result, expected)