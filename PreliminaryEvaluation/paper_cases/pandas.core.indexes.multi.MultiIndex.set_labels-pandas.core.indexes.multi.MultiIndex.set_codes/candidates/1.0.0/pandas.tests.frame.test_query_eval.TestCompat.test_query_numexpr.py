def test_query_numexpr(self):
    df = self.df
    if _NUMEXPR_INSTALLED:
        result = df.query('A>0', engine='numexpr')
        tm.assert_frame_equal(result, self.expected1)
        result = df.eval('A+1', engine='numexpr')
        tm.assert_series_equal(result, self.expected2, check_names=False)
    else:
        with pytest.raises(ImportError):
            df.query('A>0', engine='numexpr')
        with pytest.raises(ImportError):
            df.eval('A+1', engine='numexpr')