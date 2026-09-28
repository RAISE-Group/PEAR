@td.skip_if_windows
def test_to_datetime_today(self):
    with tm.set_timezone('Pacific/Auckland'):
        nptoday = np.datetime64('today').astype('datetime64[ns]').astype(np.int64)
        pdtoday = pd.to_datetime('today')
        pdtoday2 = pd.to_datetime(['today'])[0]
        tstoday = pd.Timestamp('today')
        tstoday2 = pd.Timestamp.today()
        assert abs(pdtoday.normalize().value - nptoday) < 10000000000.0
        assert abs(pdtoday2.normalize().value - nptoday) < 10000000000.0
        assert abs(pdtoday.value - tstoday.value) < 10000000000.0
        assert abs(pdtoday.value - tstoday2.value) < 10000000000.0
        assert pdtoday.tzinfo is None
        assert pdtoday2.tzinfo is None
    with tm.set_timezone('US/Samoa'):
        nptoday = np.datetime64('today').astype('datetime64[ns]').astype(np.int64)
        pdtoday = pd.to_datetime('today')
        pdtoday2 = pd.to_datetime(['today'])[0]
        assert abs(pdtoday.normalize().value - nptoday) < 10000000000.0
        assert abs(pdtoday2.normalize().value - nptoday) < 10000000000.0
        assert pdtoday.tzinfo is None
        assert pdtoday2.tzinfo is None