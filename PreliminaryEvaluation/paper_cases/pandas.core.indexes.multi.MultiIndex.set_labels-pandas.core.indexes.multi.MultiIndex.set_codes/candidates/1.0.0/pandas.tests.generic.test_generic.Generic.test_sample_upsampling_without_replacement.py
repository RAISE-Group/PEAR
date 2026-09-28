def test_sample_upsampling_without_replacement(self):
    df = pd.DataFrame({'A': list('abc')})
    msg = 'Replace has to be set to `True` when upsampling the population `frac` > 1.'
    with pytest.raises(ValueError, match=msg):
        df.sample(frac=2, replace=False)