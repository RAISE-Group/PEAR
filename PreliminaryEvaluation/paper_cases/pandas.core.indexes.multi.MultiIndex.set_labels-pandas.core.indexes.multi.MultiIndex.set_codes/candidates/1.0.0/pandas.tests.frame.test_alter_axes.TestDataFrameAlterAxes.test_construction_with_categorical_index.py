def test_construction_with_categorical_index(self):
    ci = tm.makeCategoricalIndex(10)
    ci.name = 'B'
    df = DataFrame({'A': np.random.randn(10), 'B': ci.values})
    idf = df.set_index('B')
    tm.assert_index_equal(idf.index, ci)
    df = DataFrame({'A': np.random.randn(10), 'B': ci})
    idf = df.set_index('B')
    tm.assert_index_equal(idf.index, ci)
    idf = idf.reset_index().set_index('B')
    tm.assert_index_equal(idf.index, ci)