@pytest.mark.parametrize('other', [pd.date_range('2000', periods=4).array, pd.timedelta_range('1D', periods=4).array, np.arange(4), np.arange(4).astype(np.float64), list(range(4))])
def test_compare_invalid_listlike(self, box_with_array, other):
    pi = pd.period_range('2000', periods=4)
    parr = tm.box_expected(pi, box_with_array)
    assert_invalid_comparison(parr, other, box_with_array)