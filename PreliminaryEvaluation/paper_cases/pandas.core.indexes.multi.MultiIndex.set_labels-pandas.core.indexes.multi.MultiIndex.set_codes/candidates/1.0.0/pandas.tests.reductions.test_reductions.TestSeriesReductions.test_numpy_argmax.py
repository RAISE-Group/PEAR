def test_numpy_argmax(self):
    data = np.arange(1, 11)
    s = Series(data, index=data)
    result = np.argmax(s)
    expected = np.argmax(data)
    assert result == expected
    result = s.argmax()
    assert result == expected
    msg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.argmax(s, out=data)