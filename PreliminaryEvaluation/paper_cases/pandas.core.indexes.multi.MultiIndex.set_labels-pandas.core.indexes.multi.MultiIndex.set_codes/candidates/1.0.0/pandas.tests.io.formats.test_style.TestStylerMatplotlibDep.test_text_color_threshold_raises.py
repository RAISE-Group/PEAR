@pytest.mark.parametrize('text_color_threshold', [1.1, '1', -1, [2, 2]])
def test_text_color_threshold_raises(self, text_color_threshold):
    df = pd.DataFrame([[1, 2], [2, 4]], columns=['A', 'B'])
    msg = '`text_color_threshold` must be a value from 0 to 1.'
    with pytest.raises(ValueError, match=msg):
        df.style.background_gradient(text_color_threshold=text_color_threshold)._compute()