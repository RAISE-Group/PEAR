def test_to_datetime_barely_out_of_bounds(self):
    arr = np.array(['2262-04-11 23:47:16.854775808'], dtype=object)
    with pytest.raises(OutOfBoundsDatetime):
        to_datetime(arr)