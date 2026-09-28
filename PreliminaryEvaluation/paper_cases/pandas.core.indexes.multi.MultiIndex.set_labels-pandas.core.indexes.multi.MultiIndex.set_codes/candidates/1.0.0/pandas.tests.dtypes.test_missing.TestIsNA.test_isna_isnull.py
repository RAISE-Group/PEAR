@pytest.mark.parametrize('isna_f', [isna, isnull])
def test_isna_isnull(self, isna_f):
    assert not isna_f(1.0)
    assert isna_f(None)
    assert isna_f(np.NaN)
    assert float('nan')
    assert not isna_f(np.inf)
    assert not isna_f(-np.inf)
    assert not isna_f(type(pd.Series(dtype=object)))
    assert not isna_f(type(pd.Series(dtype=np.float64)))
    assert not isna_f(type(pd.DataFrame()))
    for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries(), tm.makeTimeSeries(), tm.makePeriodSeries()]:
        assert isinstance(isna_f(s), Series)
    for df in [tm.makeTimeDataFrame(), tm.makePeriodFrame(), tm.makeMixedDataFrame()]:
        result = isna_f(df)
        expected = df.apply(isna_f)
        tm.assert_frame_equal(result, expected)