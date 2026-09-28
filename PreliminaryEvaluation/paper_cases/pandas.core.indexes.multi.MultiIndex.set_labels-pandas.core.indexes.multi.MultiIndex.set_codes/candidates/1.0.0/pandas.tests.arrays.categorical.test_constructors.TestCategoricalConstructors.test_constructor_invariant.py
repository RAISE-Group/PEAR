def test_constructor_invariant(self):
    vals = [np.array([1.0, 1.2, 1.8, np.nan]), np.array([1, 2, 3], dtype='int64'), ['a', 'b', 'c', np.nan], [pd.Period('2014-01'), pd.Period('2014-02'), NaT], [Timestamp('2014-01-01'), Timestamp('2014-01-02'), NaT], [Timestamp('2014-01-01', tz='US/Eastern'), Timestamp('2014-01-02', tz='US/Eastern'), NaT]]
    for val in vals:
        c = Categorical(val)
        c2 = Categorical(c)
        tm.assert_categorical_equal(c, c2)