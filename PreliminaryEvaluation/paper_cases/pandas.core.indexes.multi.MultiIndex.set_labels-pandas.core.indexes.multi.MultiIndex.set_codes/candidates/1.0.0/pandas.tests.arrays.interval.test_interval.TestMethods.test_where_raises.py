@pytest.mark.parametrize('other', [Interval(0, 1, closed='right'), IntervalArray.from_breaks([1, 2, 3, 4], closed='right')])
def test_where_raises(self, other):
    ser = pd.Series(IntervalArray.from_breaks([1, 2, 3, 4], closed='left'))
    match = "'value.closed' is 'right', expected 'left'."
    with pytest.raises(ValueError, match=match):
        ser.where([True, False, True], other=other)