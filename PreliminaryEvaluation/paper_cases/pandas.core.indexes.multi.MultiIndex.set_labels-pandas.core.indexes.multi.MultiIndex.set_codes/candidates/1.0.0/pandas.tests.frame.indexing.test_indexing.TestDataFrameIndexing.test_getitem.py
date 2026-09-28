def test_getitem(self, float_frame):
    sl = float_frame[:20]
    assert len(sl.index) == 20
    for _, series in sl.items():
        assert len(series.index) == 20
        assert tm.equalContents(series.index, sl.index)
    for key, _ in float_frame._series.items():
        assert float_frame[key] is not None
    assert 'random' not in float_frame
    with pytest.raises(KeyError, match='random'):
        float_frame['random']
    df = float_frame.copy()
    df['$10'] = np.random.randn(len(df))
    ad = np.random.randn(len(df))
    df['@awesome_domain'] = ad
    with pytest.raises(KeyError, match=re.escape('\'df["$10"]\'')):
        df.__getitem__('df["$10"]')
    res = df['@awesome_domain']
    tm.assert_numpy_array_equal(ad, res.values)