@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_unprocessable_input(self, cache):
    result = to_datetime([1, '1'], errors='ignore', cache=cache)
    expected = Index(np.array([1, '1'], dtype='O'))
    tm.assert_equal(result, expected)
    msg = 'invalid string coercion to datetime'
    with pytest.raises(TypeError, match=msg):
        to_datetime([1, '1'], errors='raise', cache=cache)