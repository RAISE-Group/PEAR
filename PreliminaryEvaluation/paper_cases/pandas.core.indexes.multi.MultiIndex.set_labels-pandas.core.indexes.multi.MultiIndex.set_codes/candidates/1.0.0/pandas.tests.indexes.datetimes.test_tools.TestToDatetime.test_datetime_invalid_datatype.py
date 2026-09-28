def test_datetime_invalid_datatype(self):
    with pytest.raises(TypeError):
        pd.to_datetime(bool)
    with pytest.raises(TypeError):
        pd.to_datetime(pd.to_datetime)