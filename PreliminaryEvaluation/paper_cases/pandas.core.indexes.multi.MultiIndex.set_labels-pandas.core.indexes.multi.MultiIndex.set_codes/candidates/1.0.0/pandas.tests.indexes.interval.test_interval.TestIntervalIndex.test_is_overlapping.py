@pytest.mark.parametrize('start, shift, na_value', [(0, 1, np.nan), (Timestamp('2018-01-01'), Timedelta('1 day'), pd.NaT), (Timedelta('0 days'), Timedelta('1 day'), pd.NaT)])
def test_is_overlapping(self, start, shift, na_value, closed):
    tuples = [(start + n * shift, start + (n + 1) * shift) for n in (0, 2, 4)]
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    assert index.is_overlapping is False
    tuples = [(na_value, na_value)] + tuples + [(na_value, na_value)]
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    assert index.is_overlapping is False
    tuples = [(start + n * shift, start + (n + 2) * shift) for n in range(3)]
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    assert index.is_overlapping is True
    tuples = [(na_value, na_value)] + tuples + [(na_value, na_value)]
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    assert index.is_overlapping is True
    tuples = [(start + n * shift, start + (n + 1) * shift) for n in range(3)]
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    result = index.is_overlapping
    expected = closed == 'both'
    assert result is expected
    tuples = [(na_value, na_value)] + tuples + [(na_value, na_value)]
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    result = index.is_overlapping
    assert result is expected