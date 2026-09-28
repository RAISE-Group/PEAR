def test_constructor_subclassed_datetime(self):

    class SubDatetime(datetime):
        pass
    data = SubDatetime(2000, 1, 1)
    result = Timestamp(data)
    expected = Timestamp(2000, 1, 1)
    assert result == expected