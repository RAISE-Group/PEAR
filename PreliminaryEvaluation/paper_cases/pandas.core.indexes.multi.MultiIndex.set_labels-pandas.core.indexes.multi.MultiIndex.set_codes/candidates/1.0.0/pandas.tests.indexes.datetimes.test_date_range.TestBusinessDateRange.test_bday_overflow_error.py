def test_bday_overflow_error(self):
    start = pd.Timestamp.max.floor('D').to_pydatetime()
    with pytest.raises(OutOfBoundsDatetime):
        pd.date_range(start, periods=2, freq='B')