def test_divmod_invalid(self):
    td = Timedelta(days=2, hours=6)
    with pytest.raises(TypeError):
        divmod(td, Timestamp('2018-01-22'))