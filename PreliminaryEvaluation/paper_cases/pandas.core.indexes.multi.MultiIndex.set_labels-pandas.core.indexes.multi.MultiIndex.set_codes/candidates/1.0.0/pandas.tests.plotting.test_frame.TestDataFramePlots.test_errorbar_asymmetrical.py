def test_errorbar_asymmetrical(self):
    np.random.seed(0)
    err = np.random.rand(3, 2, 5)
    df = DataFrame(np.arange(15).reshape(3, 5)).T
    ax = df.plot(yerr=err, xerr=err / 2)
    yerr_0_0 = ax.collections[1].get_paths()[0].vertices[:, 1]
    expected_0_0 = err[0, :, 0] * np.array([-1, 1])
    tm.assert_almost_equal(yerr_0_0, expected_0_0)
    with pytest.raises(ValueError):
        df.plot(yerr=err.T)
    tm.close()