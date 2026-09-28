def test_pandas_plots_register(self):
    pytest.importorskip('matplotlib.pyplot')
    s = Series(range(12), index=date_range('2017', periods=12))
    with tm.assert_produces_warning(None) as w:
        s.plot()
    assert len(w) == 0