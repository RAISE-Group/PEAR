@pytest.mark.parametrize('inplace', [True, False])
@pytest.mark.parametrize('upper', [[1, 2, 3], np.asarray([1, 2, 3])])
def test_clip_against_list_like(self, inplace, upper):
    original = pd.Series([5, 6, 7])
    result = original.clip(upper=upper, inplace=inplace)
    expected = pd.Series([1, 2, 3])
    if inplace:
        result = original
    tm.assert_series_equal(result, expected, check_exact=True)