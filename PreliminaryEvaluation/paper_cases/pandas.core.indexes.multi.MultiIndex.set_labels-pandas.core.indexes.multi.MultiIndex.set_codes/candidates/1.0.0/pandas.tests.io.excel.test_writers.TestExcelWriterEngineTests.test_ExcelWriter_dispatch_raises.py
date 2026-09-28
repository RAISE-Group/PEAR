def test_ExcelWriter_dispatch_raises(self):
    with pytest.raises(ValueError, match='No engine'):
        ExcelWriter('nothing')