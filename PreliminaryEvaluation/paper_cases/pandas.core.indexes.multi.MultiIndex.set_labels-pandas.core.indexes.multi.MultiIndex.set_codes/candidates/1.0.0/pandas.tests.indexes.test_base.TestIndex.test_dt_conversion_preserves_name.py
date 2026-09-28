@pytest.mark.parametrize('dt_conv', [pd.to_datetime, pd.to_timedelta])
def test_dt_conversion_preserves_name(self, dt_conv):
    index = pd.Index(['01:02:03', '01:02:04'], name='label')
    assert index.name == dt_conv(index).name