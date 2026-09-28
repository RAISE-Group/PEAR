def test_register_writer(self):
    called_save = []
    called_write_cells = []

    class DummyClass(ExcelWriter):
        called_save = False
        called_write_cells = False
        supported_extensions = ['xlsx', 'xls']
        engine = 'dummy'

        def save(self):
            called_save.append(True)

        def write_cells(self, *args, **kwargs):
            called_write_cells.append(True)

    def check_called(func):
        func()
        assert len(called_save) >= 1
        assert len(called_write_cells) >= 1
        del called_save[:]
        del called_write_cells[:]
    with pd.option_context('io.excel.xlsx.writer', 'dummy'):
        register_writer(DummyClass)
        writer = ExcelWriter('something.xlsx')
        assert isinstance(writer, DummyClass)
        df = tm.makeCustomDataframe(1, 1)
        check_called(lambda: df.to_excel('something.xlsx'))
        check_called(lambda: df.to_excel('something.xls', engine='dummy'))