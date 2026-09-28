@td.skip_if_windows
def test_to_datetime_now(self):
    with tm.set_timezone('US/Eastern'):
        npnow = np.datetime64('now').astype('datetime64[ns]')
        pdnow = pd.to_datetime('now')
        pdnow2 = pd.to_datetime(['now'])[0]
        assert abs(pdnow.value - npnow.astype(np.int64)) < 10000000000.0
        assert abs(pdnow2.value - npnow.astype(np.int64)) < 10000000000.0
        assert pdnow.tzinfo is None
        assert pdnow2.tzinfo is None