@pytest.mark.slow
def test_subplots_warnings(self):
    with tm.assert_produces_warning(None):
        df = DataFrame(np.random.randn(100, 4))
        df.plot(subplots=True, layout=(3, 2))
        df = DataFrame(np.random.randn(100, 4), index=date_range('1/1/2000', periods=100))
        df.plot(subplots=True, layout=(3, 2))