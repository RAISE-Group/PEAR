@pytest.mark.parametrize('freq', ['H', '12H', '2D', 'W'])
@pytest.mark.parametrize('kind', [None, 'period', 'timestamp'])
@pytest.mark.parametrize('kwargs', [dict(on='date'), dict(level='d')])
def test_selection(self, index, freq, kind, kwargs):
    rng = np.arange(len(index), dtype=np.int64)
    df = DataFrame({'date': index, 'a': rng}, index=pd.MultiIndex.from_arrays([rng, index], names=['v', 'd']))
    msg = 'Resampling from level= or on= selection with a PeriodIndex is not currently supported, use \\.set_index\\(\\.\\.\\.\\) to explicitly set index'
    with pytest.raises(NotImplementedError, match=msg):
        df.resample(freq, kind=kind, **kwargs)