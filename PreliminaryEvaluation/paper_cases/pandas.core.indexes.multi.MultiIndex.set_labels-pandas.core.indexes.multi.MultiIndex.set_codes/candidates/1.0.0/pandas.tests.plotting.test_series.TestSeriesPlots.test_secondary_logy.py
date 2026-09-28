@pytest.mark.slow
@pytest.mark.parametrize('input_logy, expected_scale', [(True, 'log'), ('sym', 'symlog')])
def test_secondary_logy(self, input_logy, expected_scale):
    s1 = Series(np.random.randn(30))
    s2 = Series(np.random.randn(30))
    ax1 = s1.plot(logy=input_logy)
    ax2 = s2.plot(secondary_y=True, logy=input_logy)
    assert ax1.get_yscale() == expected_scale
    assert ax2.get_yscale() == expected_scale