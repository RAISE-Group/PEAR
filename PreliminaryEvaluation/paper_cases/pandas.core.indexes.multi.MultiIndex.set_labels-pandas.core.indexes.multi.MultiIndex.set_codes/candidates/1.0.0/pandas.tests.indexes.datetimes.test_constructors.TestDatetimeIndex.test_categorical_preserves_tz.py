def test_categorical_preserves_tz(self):
    dti = pd.DatetimeIndex([pd.NaT, '2015-01-01', '1999-04-06 15:14:13', '2015-01-01'], tz='US/Eastern')
    ci = pd.CategoricalIndex(dti)
    carr = pd.Categorical(dti)
    cser = pd.Series(ci)
    for obj in [ci, carr, cser]:
        result = pd.DatetimeIndex(obj)
        tm.assert_index_equal(result, dti)