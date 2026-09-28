def test_boolean(self):
    s = Series([False, False, True])
    _check_plot_works(s.plot, include_bool=True)
    msg = 'no numeric data to plot'
    with pytest.raises(TypeError, match=msg):
        _check_plot_works(s.plot)