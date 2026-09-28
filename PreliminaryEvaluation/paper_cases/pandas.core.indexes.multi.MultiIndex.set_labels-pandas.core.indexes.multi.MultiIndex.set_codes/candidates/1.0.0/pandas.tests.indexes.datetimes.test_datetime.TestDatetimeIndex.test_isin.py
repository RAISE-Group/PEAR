def test_isin(self):
    index = tm.makeDateIndex(4)
    result = index.isin(index)
    assert result.all()
    result = index.isin(list(index))
    assert result.all()
    tm.assert_almost_equal(index.isin([index[2], 5]), np.array([False, False, True, False]))