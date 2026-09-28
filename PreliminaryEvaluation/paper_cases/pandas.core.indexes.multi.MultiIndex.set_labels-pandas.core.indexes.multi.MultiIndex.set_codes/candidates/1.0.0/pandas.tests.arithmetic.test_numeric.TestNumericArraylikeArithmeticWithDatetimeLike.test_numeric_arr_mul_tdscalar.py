@pytest.mark.parametrize('scalar_td', [Timedelta(days=1), Timedelta(days=1).to_timedelta64(), Timedelta(days=1).to_pytimedelta()], ids=lambda x: type(x).__name__)
def test_numeric_arr_mul_tdscalar(self, scalar_td, numeric_idx, box):
    index = numeric_idx
    expected = pd.timedelta_range('0 days', '4 days')
    index = tm.box_expected(index, box)
    expected = tm.box_expected(expected, box)
    result = index * scalar_td
    tm.assert_equal(result, expected)
    commute = scalar_td * index
    tm.assert_equal(commute, expected)