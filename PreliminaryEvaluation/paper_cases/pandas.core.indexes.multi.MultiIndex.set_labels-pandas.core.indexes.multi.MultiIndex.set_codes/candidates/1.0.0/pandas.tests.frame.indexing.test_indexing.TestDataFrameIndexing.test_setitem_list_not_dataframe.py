def test_setitem_list_not_dataframe(self, float_frame):
    data = np.random.randn(len(float_frame), 2)
    float_frame[['A', 'B']] = data
    tm.assert_almost_equal(float_frame[['A', 'B']].values, data)