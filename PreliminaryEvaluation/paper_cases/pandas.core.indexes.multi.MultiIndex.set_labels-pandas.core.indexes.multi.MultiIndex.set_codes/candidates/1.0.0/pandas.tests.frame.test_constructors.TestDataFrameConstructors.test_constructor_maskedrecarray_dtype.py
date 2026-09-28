def test_constructor_maskedrecarray_dtype(self):
    data = np.ma.array(np.ma.zeros(5, dtype=[('date', '<f8'), ('price', '<f8')]), mask=[False] * 5)
    data = data.view(mrecords.mrecarray)
    result = pd.DataFrame(data, dtype=int)
    expected = pd.DataFrame(np.zeros((5, 2), dtype=int), columns=['date', 'price'])
    tm.assert_frame_equal(result, expected)