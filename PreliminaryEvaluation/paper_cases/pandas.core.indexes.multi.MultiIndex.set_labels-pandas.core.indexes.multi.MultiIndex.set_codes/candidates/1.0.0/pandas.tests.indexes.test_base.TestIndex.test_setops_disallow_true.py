@pytest.mark.parametrize('method', ['union', 'intersection', 'difference', 'symmetric_difference'])
def test_setops_disallow_true(self, method):
    idx1 = pd.Index(['a', 'b'])
    idx2 = pd.Index(['b', 'c'])
    with pytest.raises(ValueError, match="The 'sort' keyword only takes"):
        getattr(idx1, method)(idx2, sort=True)