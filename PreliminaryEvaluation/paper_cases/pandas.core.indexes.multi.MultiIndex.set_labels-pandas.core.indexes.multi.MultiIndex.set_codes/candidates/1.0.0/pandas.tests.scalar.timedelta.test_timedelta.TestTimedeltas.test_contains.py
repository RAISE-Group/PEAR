def test_contains(self):
    td = to_timedelta(range(5), unit='d') + pd.offsets.Hour(1)
    for v in [NaT, None, float('nan'), np.nan]:
        assert not v in td
    td = to_timedelta([NaT])
    for v in [NaT, None, float('nan'), np.nan]:
        assert v in td