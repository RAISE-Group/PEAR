def test_setitem_empty_indxer(self, data, box_in_series):
    if box_in_series:
        data = pd.Series(data)
    original = data.copy()
    data[np.array([], dtype=int)] = []
    self.assert_equal(data, original)