def test_raise_error_on_datetime_time_data(self):
    df = pd.DataFrame(np.random.randn(10), columns=['a'])
    df['dtime'] = pd.date_range(start='2014-01-01', freq='h', periods=10).time
    msg = "must be a string or a number, not 'datetime.time'"
    with pytest.raises(TypeError, match=msg):
        df.plot(kind='scatter', x='dtime', y='a')