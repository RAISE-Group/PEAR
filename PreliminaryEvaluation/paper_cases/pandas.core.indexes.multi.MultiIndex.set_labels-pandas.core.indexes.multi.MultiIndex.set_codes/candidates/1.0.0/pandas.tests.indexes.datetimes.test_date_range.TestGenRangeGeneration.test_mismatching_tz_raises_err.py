@pytest.mark.parametrize('start,end', [(pd.Timestamp(dt1, tz=tz1), pd.Timestamp(dt2)), (pd.Timestamp(dt1), pd.Timestamp(dt2, tz=tz2)), (pd.Timestamp(dt1, tz=tz1), pd.Timestamp(dt2, tz=tz2)), (pd.Timestamp(dt1, tz=tz2), pd.Timestamp(dt2, tz=tz1))])
def test_mismatching_tz_raises_err(self, start, end):
    with pytest.raises(TypeError):
        pd.date_range(start, end)
    with pytest.raises(TypeError):
        pd.date_range(start, end, freq=BDay())