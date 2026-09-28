def test_display_set_precision(self):
    df = pd.DataFrame(data=[[1.0, 2.009], [3.2121, 4.566]], columns=['a', 'b'])
    s = Styler(df)
    ctx = s.set_precision(1)._translate()
    assert s.precision == 1
    assert ctx['body'][0][1]['display_value'] == '1.0'
    assert ctx['body'][0][2]['display_value'] == '2.0'
    assert ctx['body'][1][1]['display_value'] == '3.2'
    assert ctx['body'][1][2]['display_value'] == '4.6'
    ctx = s.set_precision(2)._translate()
    assert s.precision == 2
    assert ctx['body'][0][1]['display_value'] == '1.00'
    assert ctx['body'][0][2]['display_value'] == '2.01'
    assert ctx['body'][1][1]['display_value'] == '3.21'
    assert ctx['body'][1][2]['display_value'] == '4.57'
    ctx = s.set_precision(3)._translate()
    assert s.precision == 3
    assert ctx['body'][0][1]['display_value'] == '1.000'
    assert ctx['body'][0][2]['display_value'] == '2.009'
    assert ctx['body'][1][1]['display_value'] == '3.212'
    assert ctx['body'][1][2]['display_value'] == '4.566'