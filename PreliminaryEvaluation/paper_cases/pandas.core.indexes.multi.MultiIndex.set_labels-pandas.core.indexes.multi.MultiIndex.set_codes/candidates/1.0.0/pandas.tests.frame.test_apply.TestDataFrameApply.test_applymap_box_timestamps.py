def test_applymap_box_timestamps(self):
    ser = pd.Series(date_range('1/1/2000', periods=10))

    def func(x):
        return (x.hour, x.day, x.month)
    pd.DataFrame(ser).applymap(func)