@pytest.mark.parametrize('dict_colors, msg', [(dict(boxes='r', invalid_key='r'), "invalid key 'invalid_key'")])
def test_color_kwd_errors(self, dict_colors, msg):
    df = DataFrame(random.rand(10, 2))
    with pytest.raises(ValueError, match=msg):
        df.boxplot(color=dict_colors, return_type='dict')