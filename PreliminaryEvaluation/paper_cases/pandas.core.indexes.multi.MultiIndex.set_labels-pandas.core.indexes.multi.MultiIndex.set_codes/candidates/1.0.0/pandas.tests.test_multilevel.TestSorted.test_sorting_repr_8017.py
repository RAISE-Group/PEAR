def test_sorting_repr_8017(self):
    np.random.seed(0)
    data = np.random.randn(3, 4)
    for gen, extra in [([1.0, 3.0, 2.0, 5.0], 4.0), ([1, 3, 2, 5], 4), ([Timestamp('20130101'), Timestamp('20130103'), Timestamp('20130102'), Timestamp('20130105')], Timestamp('20130104')), (['1one', '3one', '2one', '5one'], '4one')]:
        columns = MultiIndex.from_tuples([('red', i) for i in gen])
        df = DataFrame(data, index=list('def'), columns=columns)
        df2 = pd.concat([df, DataFrame('world', index=list('def'), columns=MultiIndex.from_tuples([('red', extra)]))], axis=1)
        assert str(df2).splitlines()[0].split() == ['red']
        result = df.copy().sort_index(axis=1)
        expected = df.iloc[:, [0, 2, 1, 3]]
        tm.assert_frame_equal(result, expected)
        result = df2.sort_index(axis=1)
        expected = df2.iloc[:, [0, 2, 1, 4, 3]]
        tm.assert_frame_equal(result, expected)
        result = df.copy()
        result['red', extra] = 'world'
        result = result.sort_index(axis=1)
        tm.assert_frame_equal(result, expected)