@pytest.mark.parametrize('scalar', ['foo', pd.Timestamp.now(), pd.Timedelta(days=4)])
def test_compare_invalid_scalar(self, box_with_array, scalar):
    pi = pd.period_range('2000', periods=4)
    parr = tm.box_expected(pi, box_with_array)
    assert_invalid_comparison(parr, scalar, box_with_array)