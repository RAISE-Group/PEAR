def test_frame_dict_constructor_empty_series(self):
    s1 = Series([1, 2, 3, 4], index=MultiIndex.from_tuples([(1, 2), (1, 3), (2, 2), (2, 4)]))
    s2 = Series([1, 2, 3, 4], index=MultiIndex.from_tuples([(1, 2), (1, 3), (3, 2), (3, 4)]))
    s3 = Series(dtype=object)
    DataFrame({'foo': s1, 'bar': s2, 'baz': s3})
    DataFrame.from_dict({'foo': s1, 'baz': s3, 'bar': s2})