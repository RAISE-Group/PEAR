@pytest.mark.parametrize('use_bottleneck', [True, False])
@pytest.mark.parametrize('method, unit', [('sum', 0.0), ('prod', 1.0)])
def test_empty(self, method, unit, use_bottleneck):
    with pd.option_context('use_bottleneck', use_bottleneck):
        s = Series([], dtype=object)
        result = getattr(s, method)()
        assert result == unit
        result = getattr(s, method)(min_count=0)
        assert result == unit
        result = getattr(s, method)(min_count=1)
        assert pd.isna(result)
        result = getattr(s, method)(skipna=True)
        result == unit
        result = getattr(s, method)(skipna=True, min_count=0)
        assert result == unit
        result = getattr(s, method)(skipna=True, min_count=1)
        assert pd.isna(result)
        s = Series([np.nan])
        result = getattr(s, method)()
        assert result == unit
        result = getattr(s, method)(min_count=0)
        assert result == unit
        result = getattr(s, method)(min_count=1)
        assert pd.isna(result)
        result = getattr(s, method)(skipna=True)
        result == unit
        result = getattr(s, method)(skipna=True, min_count=0)
        assert result == unit
        result = getattr(s, method)(skipna=True, min_count=1)
        assert pd.isna(result)
        s = Series([np.nan, 1])
        result = getattr(s, method)()
        assert result == 1.0
        result = getattr(s, method)(min_count=0)
        assert result == 1.0
        result = getattr(s, method)(min_count=1)
        assert result == 1.0
        result = getattr(s, method)(skipna=True)
        assert result == 1.0
        result = getattr(s, method)(skipna=True, min_count=0)
        assert result == 1.0
        result = getattr(s, method)(skipna=True, min_count=1)
        assert result == 1.0
        df = DataFrame(np.empty((10, 0)))
        assert (getattr(df, method)(1) == unit).all()
        s = pd.Series([1])
        result = getattr(s, method)(min_count=2)
        assert pd.isna(result)
        s = pd.Series([np.nan])
        result = getattr(s, method)(min_count=2)
        assert pd.isna(result)
        s = pd.Series([np.nan, 1])
        result = getattr(s, method)(min_count=2)
        assert pd.isna(result)