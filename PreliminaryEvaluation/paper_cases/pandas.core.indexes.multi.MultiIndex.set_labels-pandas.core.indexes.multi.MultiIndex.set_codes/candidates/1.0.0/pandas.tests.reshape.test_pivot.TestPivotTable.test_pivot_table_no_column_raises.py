def test_pivot_table_no_column_raises(self):

    def agg(l):
        return np.mean(l)
    foo = pd.DataFrame({'X': [0, 0, 1, 1], 'Y': [0, 1, 0, 1], 'Z': [10, 20, 30, 40]})
    with pytest.raises(KeyError, match='notpresent'):
        foo.pivot_table('notpresent', 'X', 'Y', aggfunc=agg)