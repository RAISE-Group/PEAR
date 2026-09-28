def test_invalid_colormap(self):
    df = DataFrame(randn(3, 2), columns=['A', 'B'])
    with pytest.raises(ValueError):
        df.plot(colormap='invalid_colormap')