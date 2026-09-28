def test_inf(self):
    formatter = fmt.EngFormatter(accuracy=1, use_eng_prefix=True)
    result = formatter(np.inf)
    assert result == 'inf'