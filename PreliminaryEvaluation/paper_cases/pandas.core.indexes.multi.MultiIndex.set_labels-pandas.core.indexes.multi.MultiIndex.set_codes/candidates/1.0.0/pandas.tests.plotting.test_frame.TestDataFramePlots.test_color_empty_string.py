def test_color_empty_string(self):
    df = DataFrame(randn(10, 2))
    with pytest.raises(ValueError):
        df.plot(color='')