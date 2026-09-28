@td.skip_if_no_scipy
@pytest.mark.parametrize('meth', ['pearson', 'spearman'])
def test_corr_constant(self, meth):
    df = DataFrame({'A': [1, 1, 1, np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, np.nan, 1, 1, 1]})
    rs = df.corr(meth)
    assert isna(rs.values).all()