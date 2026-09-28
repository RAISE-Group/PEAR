def test_repr_utcoffset(self):
    date_with_utc_offset = Timestamp('2014-03-13 00:00:00-0400', tz=None)
    assert '2014-03-13 00:00:00-0400' in repr(date_with_utc_offset)
    assert 'tzoffset' not in repr(date_with_utc_offset)
    assert 'pytz.FixedOffset(-240)' in repr(date_with_utc_offset)
    expr = repr(date_with_utc_offset).replace("'pytz.FixedOffset(-240)'", 'pytz.FixedOffset(-240)')
    assert date_with_utc_offset == eval(expr)