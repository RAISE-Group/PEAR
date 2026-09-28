def test_td64_series_astype_object(self):
    tdser = Series(['59 Days', '59 Days', 'NaT'], dtype='timedelta64[ns]')
    result = tdser.astype(object)
    assert isinstance(result.iloc[0], timedelta)
    assert result.dtype == np.object_