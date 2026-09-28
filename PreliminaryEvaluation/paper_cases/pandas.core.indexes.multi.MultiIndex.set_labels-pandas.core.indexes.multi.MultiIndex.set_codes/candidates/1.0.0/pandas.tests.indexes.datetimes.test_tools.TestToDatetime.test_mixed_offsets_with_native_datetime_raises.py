def test_mixed_offsets_with_native_datetime_raises(self):
    s = pd.Series(['nan', pd.Timestamp('1990-01-01'), '2015-03-14T16:15:14.123-08:00', '2019-03-04T21:56:32.620-07:00', None])
    with pytest.raises(ValueError, match='Tz-aware datetime.datetime'):
        pd.to_datetime(s)