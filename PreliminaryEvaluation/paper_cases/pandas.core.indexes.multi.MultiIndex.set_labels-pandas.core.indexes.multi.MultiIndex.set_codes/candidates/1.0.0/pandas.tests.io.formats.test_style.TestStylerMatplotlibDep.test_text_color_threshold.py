@pytest.mark.parametrize('c_map,expected', [(None, {(0, 0): ['background-color: #440154', 'color: #f1f1f1'], (1, 0): ['background-color: #fde725', 'color: #000000']}), ('YlOrRd', {(0, 0): ['background-color: #ffffcc', 'color: #000000'], (1, 0): ['background-color: #800026', 'color: #f1f1f1']})])
def test_text_color_threshold(self, c_map, expected):
    df = pd.DataFrame([1, 2], columns=['A'])
    result = df.style.background_gradient(cmap=c_map)._compute().ctx
    assert result == expected