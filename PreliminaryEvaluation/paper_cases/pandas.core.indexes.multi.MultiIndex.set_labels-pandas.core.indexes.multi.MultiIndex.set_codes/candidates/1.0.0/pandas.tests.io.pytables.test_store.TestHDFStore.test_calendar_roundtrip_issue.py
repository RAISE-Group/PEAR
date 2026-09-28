@td.xfail_non_writeable
@pytest.mark.skipif(LooseVersion(np.__version__) == LooseVersion('1.15.0'), reason='Skipping  pytables test when numpy version is exactly equal to 1.15.0: gh-22098')
def test_calendar_roundtrip_issue(self, setup_path):
    weekmask_egypt = 'Sun Mon Tue Wed Thu'
    holidays = ['2012-05-01', datetime.datetime(2013, 5, 1), np.datetime64('2014-05-01')]
    bday_egypt = pd.offsets.CustomBusinessDay(holidays=holidays, weekmask=weekmask_egypt)
    dt = datetime.datetime(2013, 4, 30)
    dts = date_range(dt, periods=5, freq=bday_egypt)
    s = Series(dts.weekday, dts).map(Series('Mon Tue Wed Thu Fri Sat Sun'.split()))
    with ensure_clean_store(setup_path) as store:
        store.put('fixed', s)
        result = store.select('fixed')
        tm.assert_series_equal(result, s)
        store.append('table', s)
        result = store.select('table')
        tm.assert_series_equal(result, s)