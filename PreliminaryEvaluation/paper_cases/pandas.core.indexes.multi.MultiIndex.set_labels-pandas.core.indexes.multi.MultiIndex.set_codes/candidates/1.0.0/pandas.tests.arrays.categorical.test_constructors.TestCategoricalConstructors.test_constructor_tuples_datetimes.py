def test_constructor_tuples_datetimes(self):
    values = np.array([(Timestamp('2010-01-01'),), (Timestamp('2010-01-02'),), (Timestamp('2010-01-01'),), (Timestamp('2010-01-02'),), ('a', 'b')], dtype=object)[:-1]
    result = Categorical(values)
    expected = Index([(Timestamp('2010-01-01'),), (Timestamp('2010-01-02'),)], tupleize_cols=False)
    tm.assert_index_equal(result.categories, expected)