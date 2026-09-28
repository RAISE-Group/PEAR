@pytest.mark.parametrize('index', [MultiIndex.from_tuples([(1, 2), (4, 5), (8, 9)]), Index(['foo', 'bar', 'baz'])])
def test_equals_op_mismatched_multiindex_raises(self, index):
    df = pd.read_csv(StringIO('a,b,c\n1,2,3\n4,5,6'), index_col=[0, 1])
    with pytest.raises(ValueError, match='Lengths must match'):
        df.index == index