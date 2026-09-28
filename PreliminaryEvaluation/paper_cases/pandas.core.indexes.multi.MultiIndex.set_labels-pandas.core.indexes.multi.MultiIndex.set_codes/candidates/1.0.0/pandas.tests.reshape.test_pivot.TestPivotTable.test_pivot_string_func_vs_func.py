@pytest.mark.parametrize('f, f_numpy', [('sum', np.sum), ('mean', np.mean), ('std', np.std), (['sum', 'mean'], [np.sum, np.mean]), (['sum', 'std'], [np.sum, np.std]), (['std', 'mean'], [np.std, np.mean])])
def test_pivot_string_func_vs_func(self, f, f_numpy):
    result = pivot_table(self.data, index='A', columns='B', aggfunc=f)
    expected = pivot_table(self.data, index='A', columns='B', aggfunc=f_numpy)
    tm.assert_frame_equal(result, expected)