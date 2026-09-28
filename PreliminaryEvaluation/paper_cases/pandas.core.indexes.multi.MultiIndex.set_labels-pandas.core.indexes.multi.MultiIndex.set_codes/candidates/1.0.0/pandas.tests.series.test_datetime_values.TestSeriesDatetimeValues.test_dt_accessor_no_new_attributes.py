def test_dt_accessor_no_new_attributes(self):
    s = Series(date_range('20130101', periods=5, freq='D'))
    with pytest.raises(AttributeError, match='You cannot add any new attribute'):
        s.dt.xlabel = 'a'