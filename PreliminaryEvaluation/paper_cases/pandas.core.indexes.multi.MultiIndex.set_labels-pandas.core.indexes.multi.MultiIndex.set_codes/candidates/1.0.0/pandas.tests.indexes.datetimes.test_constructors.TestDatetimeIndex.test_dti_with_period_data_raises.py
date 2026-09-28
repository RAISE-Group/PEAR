def test_dti_with_period_data_raises(self):
    data = pd.PeriodIndex(['2016Q1', '2016Q2'], freq='Q')
    with pytest.raises(TypeError, match='PeriodDtype data is invalid'):
        DatetimeIndex(data)
    with pytest.raises(TypeError, match='PeriodDtype data is invalid'):
        to_datetime(data)
    with pytest.raises(TypeError, match='PeriodDtype data is invalid'):
        DatetimeIndex(period_array(data))
    with pytest.raises(TypeError, match='PeriodDtype data is invalid'):
        to_datetime(period_array(data))