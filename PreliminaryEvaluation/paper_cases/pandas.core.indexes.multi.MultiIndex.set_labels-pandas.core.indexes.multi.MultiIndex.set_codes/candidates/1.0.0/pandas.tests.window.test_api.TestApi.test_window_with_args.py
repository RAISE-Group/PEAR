@td.skip_if_no_scipy
@pytest.mark.filterwarnings("ignore:can't resolve:ImportWarning")
def test_window_with_args(self):
    r = Series(np.random.randn(100)).rolling(window=10, min_periods=1, win_type='gaussian')
    expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
    expected.columns = ['<lambda>', '<lambda>']
    result = r.aggregate([lambda x: x.mean(std=10), lambda x: x.mean(std=0.01)])
    tm.assert_frame_equal(result, expected)

    def a(x):
        return x.mean(std=10)

    def b(x):
        return x.mean(std=0.01)
    expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
    expected.columns = ['a', 'b']
    result = r.aggregate([a, b])
    tm.assert_frame_equal(result, expected)