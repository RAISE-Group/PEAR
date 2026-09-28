@pytest.mark.parametrize('addend', [datetime(2011, 1, 1), DatetimeIndex(['2011-01-01', '2011-01-02']), DatetimeIndex(['2011-01-01', '2011-01-02']).tz_localize('US/Eastern'), np.datetime64('2011-01-01'), Timestamp('2011-01-01')], ids=lambda x: type(x).__name__)
@pytest.mark.parametrize('tz', [None, 'US/Eastern'])
def test_add_datetimelike_and_dtarr(self, box_with_array, addend, tz):
    dti = DatetimeIndex(['2011-01-01', '2011-01-02']).tz_localize(tz)
    dtarr = tm.box_expected(dti, box_with_array)
    msg = 'cannot add DatetimeArray and'
    with pytest.raises(TypeError, match=msg):
        dtarr + addend
    with pytest.raises(TypeError, match=msg):
        addend + dtarr