def test_df_numeric_cmp_dt64_raises(self):
    ts = pd.Timestamp.now()
    df = pd.DataFrame({'x': range(5)})
    msg = 'Invalid comparison between dtype=int64 and Timestamp'
    with pytest.raises(TypeError, match=msg):
        df > ts
    with pytest.raises(TypeError, match=msg):
        df < ts
    with pytest.raises(TypeError, match=msg):
        ts < df
    with pytest.raises(TypeError, match=msg):
        ts > df
    assert not (df == ts).any().any()
    assert (df != ts).all().all()