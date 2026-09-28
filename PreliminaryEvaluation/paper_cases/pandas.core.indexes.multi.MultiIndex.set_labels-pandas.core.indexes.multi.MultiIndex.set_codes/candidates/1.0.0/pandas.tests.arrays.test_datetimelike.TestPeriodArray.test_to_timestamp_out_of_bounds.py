def test_to_timestamp_out_of_bounds(self):
    pi = pd.period_range('1500', freq='Y', periods=3)
    with pytest.raises(OutOfBoundsDatetime):
        pi.to_timestamp()
    with pytest.raises(OutOfBoundsDatetime):
        pi._data.to_timestamp()