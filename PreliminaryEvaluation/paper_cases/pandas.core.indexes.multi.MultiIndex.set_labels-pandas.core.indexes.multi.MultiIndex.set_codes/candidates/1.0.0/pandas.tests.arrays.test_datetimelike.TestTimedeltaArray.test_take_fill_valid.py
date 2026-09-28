def test_take_fill_valid(self, timedelta_index):
    tdi = timedelta_index
    arr = TimedeltaArray(tdi)
    td1 = pd.Timedelta(days=1)
    result = arr.take([-1, 1], allow_fill=True, fill_value=td1)
    assert result[0] == td1
    now = pd.Timestamp.now()
    with pytest.raises(ValueError):
        arr.take([0, 1], allow_fill=True, fill_value=now)
    with pytest.raises(ValueError):
        arr.take([0, 1], allow_fill=True, fill_value=now.to_period('D'))