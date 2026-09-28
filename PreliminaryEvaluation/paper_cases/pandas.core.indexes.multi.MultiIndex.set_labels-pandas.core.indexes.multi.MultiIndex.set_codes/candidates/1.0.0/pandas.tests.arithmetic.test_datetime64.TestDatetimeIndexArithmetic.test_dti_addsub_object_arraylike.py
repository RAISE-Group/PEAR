@pytest.mark.parametrize('other_box', [pd.Index, np.array])
def test_dti_addsub_object_arraylike(self, tz_naive_fixture, box_with_array, other_box):
    tz = tz_naive_fixture
    dti = pd.date_range('2017-01-01', periods=2, tz=tz)
    dtarr = tm.box_expected(dti, box_with_array)
    other = other_box([pd.offsets.MonthEnd(), pd.Timedelta(days=4)])
    xbox = get_upcast_box(box_with_array, other)
    expected = pd.DatetimeIndex(['2017-01-31', '2017-01-06'], tz=tz_naive_fixture)
    expected = tm.box_expected(expected, xbox)
    warn = None if box_with_array is pd.DataFrame else PerformanceWarning
    with tm.assert_produces_warning(warn):
        result = dtarr + other
    tm.assert_equal(result, expected)
    expected = pd.DatetimeIndex(['2016-12-31', '2016-12-29'], tz=tz_naive_fixture)
    expected = tm.box_expected(expected, xbox)
    with tm.assert_produces_warning(warn):
        result = dtarr - other
    tm.assert_equal(result, expected)