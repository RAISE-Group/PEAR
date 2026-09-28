@pytest.mark.parametrize('colors_kwd, expected', [(dict(boxes='r', whiskers='b', medians='g', caps='c'), dict(boxes='r', whiskers='b', medians='g', caps='c')), (dict(boxes='r'), dict(boxes='r')), ('r', dict(boxes='r', whiskers='r', medians='r', caps='r'))])
def test_color_kwd(self, colors_kwd, expected):
    df = DataFrame(random.rand(10, 2))
    result = df.boxplot(color=colors_kwd, return_type='dict')
    for k, v in expected.items():
        assert result[k][0].get_color() == v