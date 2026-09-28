def test_series_given_mismatched_index_raises(self, data):
    msg = 'Length of passed values is 3, index implies 5'
    with pytest.raises(ValueError, match=msg):
        pd.Series(data[:3], index=[0, 1, 2, 3, 4])