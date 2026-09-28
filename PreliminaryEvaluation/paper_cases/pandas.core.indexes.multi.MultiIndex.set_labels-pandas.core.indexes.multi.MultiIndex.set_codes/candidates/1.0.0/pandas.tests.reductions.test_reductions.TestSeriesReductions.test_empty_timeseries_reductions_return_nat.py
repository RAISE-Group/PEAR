def test_empty_timeseries_reductions_return_nat(self):
    for dtype in ('m8[ns]', 'm8[ns]', 'M8[ns]', 'M8[ns, UTC]'):
        assert Series([], dtype=dtype).min() is pd.NaT
        assert Series([], dtype=dtype).max() is pd.NaT
        assert Series([], dtype=dtype).min(skipna=False) is pd.NaT
        assert Series([], dtype=dtype).max(skipna=False) is pd.NaT