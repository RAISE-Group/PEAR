def test_numpy_argmin(self):
    data = np.arange(1, 11)
    s = Series(data, index=data)
    result = np.argmin(s)
    expected = np.argmin(data)
    assert result == expected
    result = s.argmin()
    assert result == expected
    msg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.argmin(s, out=data)