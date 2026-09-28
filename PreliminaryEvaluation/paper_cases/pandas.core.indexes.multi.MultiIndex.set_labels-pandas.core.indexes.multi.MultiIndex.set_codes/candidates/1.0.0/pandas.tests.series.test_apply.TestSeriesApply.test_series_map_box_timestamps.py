def test_series_map_box_timestamps(self):
    ser = Series(pd.date_range('1/1/2000', periods=10))

    def func(x):
        return (x.hour, x.day, x.month)
    ser.map(func)
    ser.apply(func)