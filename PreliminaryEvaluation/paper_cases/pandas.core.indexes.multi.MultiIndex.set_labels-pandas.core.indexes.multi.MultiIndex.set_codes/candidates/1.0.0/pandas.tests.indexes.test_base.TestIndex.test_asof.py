@pytest.mark.parametrize('index', ['datetime'], indirect=True)
def test_asof(self, index):
    d = index[0]
    assert index.asof(d) == d
    assert isna(index.asof(d - timedelta(1)))
    d = index[-1]
    assert index.asof(d + timedelta(1)) == d
    d = index[0].to_pydatetime()
    assert isinstance(index.asof(d), Timestamp)