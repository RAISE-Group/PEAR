def test_agg_with_one_lambda(self):
    df = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'], 'height': [9.1, 6.0, 9.5, 34.0], 'weight': [7.9, 7.5, 9.9, 198.0]})
    columns = ['height_sqr_min', 'height_max', 'weight_max']
    expected = pd.DataFrame({'height_sqr_min': [82.81, 36.0], 'height_max': [9.5, 34.0], 'weight_max': [9.9, 198.0]}, index=pd.Index(['cat', 'dog'], name='kind'), columns=columns)
    result1 = df.groupby(by='kind').agg(height_sqr_min=pd.NamedAgg(column='height', aggfunc=lambda x: np.min(x ** 2)), height_max=pd.NamedAgg(column='height', aggfunc='max'), weight_max=pd.NamedAgg(column='weight', aggfunc='max'))
    tm.assert_frame_equal(result1, expected)
    result2 = df.groupby(by='kind').agg(height_sqr_min=('height', lambda x: np.min(x ** 2)), height_max=('height', 'max'), weight_max=('weight', 'max'))
    tm.assert_frame_equal(result2, expected)