def test_display_format_raises(self):
    df = pd.DataFrame(np.random.randn(2, 2))
    with pytest.raises(TypeError):
        df.style.format(5)
    with pytest.raises(TypeError):
        df.style.format(True)