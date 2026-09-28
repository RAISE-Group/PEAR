@pytest.mark.slow
def test_hist_layout(self):
    df = DataFrame(randn(100, 3))
    layout_to_expected_size = ({'layout': None, 'expected_size': (2, 2)}, {'layout': (2, 2), 'expected_size': (2, 2)}, {'layout': (4, 1), 'expected_size': (4, 1)}, {'layout': (1, 4), 'expected_size': (1, 4)}, {'layout': (3, 3), 'expected_size': (3, 3)}, {'layout': (-1, 4), 'expected_size': (1, 4)}, {'layout': (4, -1), 'expected_size': (4, 1)}, {'layout': (-1, 2), 'expected_size': (2, 2)}, {'layout': (2, -1), 'expected_size': (2, 2)})
    for layout_test in layout_to_expected_size:
        axes = df.hist(layout=layout_test['layout'])
        expected = layout_test['expected_size']
        self._check_axes_shape(axes, axes_num=3, layout=expected)
    with pytest.raises(ValueError):
        df.hist(layout=(1, 1))
    with pytest.raises(ValueError):
        df.hist(layout=(1,))
    with pytest.raises(ValueError):
        df.hist(layout=(-1, -1))