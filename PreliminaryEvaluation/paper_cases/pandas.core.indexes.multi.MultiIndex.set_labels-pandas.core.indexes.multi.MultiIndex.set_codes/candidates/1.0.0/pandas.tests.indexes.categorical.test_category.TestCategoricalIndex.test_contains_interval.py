@pytest.mark.parametrize('item, expected', [(pd.Interval(0, 1), True), (1.5, True), (pd.Interval(0.5, 1.5), False), ('a', False), (pd.Timestamp(1), False), (pd.Timedelta(1), False)], ids=str)
def test_contains_interval(self, item, expected):
    ci = CategoricalIndex(IntervalIndex.from_breaks(range(3)))
    result = item in ci
    assert result is expected