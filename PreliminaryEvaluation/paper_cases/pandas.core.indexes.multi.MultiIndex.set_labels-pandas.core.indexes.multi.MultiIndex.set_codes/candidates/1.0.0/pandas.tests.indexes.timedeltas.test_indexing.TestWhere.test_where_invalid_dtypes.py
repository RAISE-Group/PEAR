def test_where_invalid_dtypes(self):
    tdi = timedelta_range('1 day', periods=3, freq='D', name='idx')
    i2 = tdi.copy()
    i2 = Index([pd.NaT, pd.NaT] + tdi[2:].tolist())
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        tdi.where(notna(i2), i2.asi8)
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        tdi.where(notna(i2), i2 + pd.Timestamp.now())
    with pytest.raises(TypeError, match='Where requires matching dtype'):
        tdi.where(notna(i2), (i2 + pd.Timestamp.now()).to_period('D'))