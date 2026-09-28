def test_mod_invalid(self):
    td = Timedelta(hours=37)
    with pytest.raises(TypeError):
        td % Timestamp('2018-01-22')
    with pytest.raises(TypeError):
        td % []