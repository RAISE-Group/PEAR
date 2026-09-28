def test_groupby_args(self, mframe):
    frame = mframe
    msg = "You have to supply one of 'by' and 'level'"
    with pytest.raises(TypeError, match=msg):
        frame.groupby()
    msg = "You have to supply one of 'by' and 'level'"
    with pytest.raises(TypeError, match=msg):
        frame.groupby(by=None, level=None)