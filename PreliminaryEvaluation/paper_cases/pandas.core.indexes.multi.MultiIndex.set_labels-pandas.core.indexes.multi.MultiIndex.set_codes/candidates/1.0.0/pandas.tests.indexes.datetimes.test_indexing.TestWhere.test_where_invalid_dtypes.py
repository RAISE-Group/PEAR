def test_where_invalid_dtypes(self):
    dti = pd.date_range('20130101', periods=3, tz='US/Eastern')
    i2 = dti.copy()
    i2 = Index([pd.NaT, pd.NaT] + dti[2:].tolist())
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        dti.where(notna(i2), i2.values)
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        dti.tz_localize(None).where(notna(i2), i2)
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        dti.where(notna(i2), i2.tz_localize(None).to_period('D'))
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        dti.where(notna(i2), i2.asi8.view('timedelta64[ns]'))
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        dti.where(notna(i2), i2.asi8)