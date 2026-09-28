@pytest.mark.parametrize('field', ['dayofweek', 'dayofyear', 'week', 'weekofyear', 'quarter', 'days_in_month', 'is_month_start', 'is_month_end', 'is_quarter_start', 'is_quarter_end', 'is_year_start', 'is_year_end'])
def test_dti_timestamp_fields(self, field):
    idx = tm.makeDateIndex(100)
    expected = getattr(idx, field)[-1]
    result = getattr(Timestamp(idx[-1]), field)
    assert result == expected