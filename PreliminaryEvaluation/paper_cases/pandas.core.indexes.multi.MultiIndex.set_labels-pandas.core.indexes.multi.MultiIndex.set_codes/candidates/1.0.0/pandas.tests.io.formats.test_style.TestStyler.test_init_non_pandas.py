def test_init_non_pandas(self):
    with pytest.raises(TypeError):
        Styler([1, 2, 3])