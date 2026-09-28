@pytest.mark.slow
def test_overlapping_datetime(self):
    s1 = Series([1, 2, 3], index=[datetime(1995, 12, 31), datetime(2000, 12, 31), datetime(2005, 12, 31)])
    s2 = Series([1, 2, 3], index=[datetime(1997, 12, 31), datetime(2003, 12, 31), datetime(2008, 12, 31)])
    _, ax = self.plt.subplots()
    s1.plot(ax=ax)
    s2.plot(ax=ax)
    s1.plot(ax=ax)