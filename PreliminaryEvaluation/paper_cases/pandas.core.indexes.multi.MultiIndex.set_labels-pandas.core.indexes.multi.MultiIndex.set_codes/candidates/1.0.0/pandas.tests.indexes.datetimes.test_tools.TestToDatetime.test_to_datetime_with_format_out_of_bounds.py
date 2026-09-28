@pytest.mark.parametrize('dt_str', ['00010101', '13000101', '30000101', '99990101'])
def test_to_datetime_with_format_out_of_bounds(self, dt_str):
    with pytest.raises(OutOfBoundsDatetime):
        pd.to_datetime(dt_str, format='%Y%m%d')