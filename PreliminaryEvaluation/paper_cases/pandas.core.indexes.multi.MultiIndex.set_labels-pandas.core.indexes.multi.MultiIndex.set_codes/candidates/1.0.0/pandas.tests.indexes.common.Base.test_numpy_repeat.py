def test_numpy_repeat(self):
    rep = 2
    i = self.create_index()
    expected = i.repeat(rep)
    tm.assert_index_equal(np.repeat(i, rep), expected)
    msg = "the 'axis' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.repeat(i, rep, axis=0)