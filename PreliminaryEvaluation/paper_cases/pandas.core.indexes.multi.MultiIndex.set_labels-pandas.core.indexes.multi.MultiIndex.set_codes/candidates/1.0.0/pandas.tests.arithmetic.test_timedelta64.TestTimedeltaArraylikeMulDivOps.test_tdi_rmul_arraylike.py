@pytest.mark.parametrize('other', [np.arange(1, 11), pd.Int64Index(range(1, 11)), pd.UInt64Index(range(1, 11)), pd.Float64Index(range(1, 11)), pd.RangeIndex(1, 11)], ids=lambda x: type(x).__name__)
def test_tdi_rmul_arraylike(self, other, box_with_array):
    box = box_with_array
    xbox = get_upcast_box(box, other)
    tdi = TimedeltaIndex(['1 Day'] * 10)
    expected = timedelta_range('1 days', '10 days')
    expected._data.freq = None
    tdi = tm.box_expected(tdi, box)
    expected = tm.box_expected(expected, xbox)
    result = other * tdi
    tm.assert_equal(result, expected)
    commute = tdi * other
    tm.assert_equal(commute, expected)