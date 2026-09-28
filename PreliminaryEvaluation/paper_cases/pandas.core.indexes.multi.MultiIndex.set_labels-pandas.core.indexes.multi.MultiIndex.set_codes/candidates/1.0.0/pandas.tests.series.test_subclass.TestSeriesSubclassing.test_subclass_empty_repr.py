def test_subclass_empty_repr(self):
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        sub_series = tm.SubclassedSeries()
    assert 'SubclassedSeries' in repr(sub_series)