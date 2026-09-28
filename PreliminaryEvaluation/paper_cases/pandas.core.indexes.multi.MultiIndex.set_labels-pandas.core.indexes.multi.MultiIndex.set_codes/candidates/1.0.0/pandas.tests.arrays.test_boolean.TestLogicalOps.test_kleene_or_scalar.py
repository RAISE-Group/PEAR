@pytest.mark.parametrize('other, expected', [(pd.NA, [True, None, None]), (True, [True, True, True]), (np.bool_(True), [True, True, True]), (False, [True, False, None]), (np.bool_(False), [True, False, None])])
def test_kleene_or_scalar(self, other, expected):
    a = pd.array([True, False, None], dtype='boolean')
    result = a | other
    expected = pd.array(expected, dtype='boolean')
    tm.assert_extension_array_equal(result, expected)
    result = other | a
    tm.assert_extension_array_equal(result, expected)
    tm.assert_extension_array_equal(a, pd.array([True, False, None], dtype='boolean'))