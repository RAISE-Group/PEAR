@pytest.mark.parametrize('tz', ['US/Eastern', 'dateutil/US/Eastern'])
def test_frame_reset_index(self, tz):
    dr = date_range('2012-06-02', periods=10, tz=tz)
    df = DataFrame(np.random.randn(len(dr)), dr)
    roundtripped = df.reset_index().set_index('index')
    xp = df.index.tz
    rs = roundtripped.index.tz
    assert xp == rs