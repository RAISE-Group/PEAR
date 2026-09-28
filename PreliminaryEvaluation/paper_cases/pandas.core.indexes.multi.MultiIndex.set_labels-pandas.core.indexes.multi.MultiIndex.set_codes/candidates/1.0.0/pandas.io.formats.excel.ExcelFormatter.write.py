def write(self, writer, sheet_name='Sheet1', startrow=0, startcol=0, freeze_panes=None, engine=None):
    """
        writer : string or ExcelWriter object
            File path or existing ExcelWriter
        sheet_name : string, default 'Sheet1'
            Name of sheet which will contain DataFrame
        startrow :
            upper left cell row to dump data frame
        startcol :
            upper left cell column to dump data frame
        freeze_panes : tuple of integer (length 2), default None
            Specifies the one-based bottommost row and rightmost column that
            is to be frozen
        engine : string, default None
            write engine to use if writer is a path - you can also set this
            via the options ``io.excel.xlsx.writer``, ``io.excel.xls.writer``,
            and ``io.excel.xlsm.writer``.
        """
    from pandas.io.excel import ExcelWriter
    num_rows, num_cols = self.df.shape
    if num_rows > self.max_rows or num_cols > self.max_cols:
        raise ValueError(f'This sheet is too large! Your sheet size is: {num_rows}, {num_cols} Max sheet size is: {self.max_rows}, {self.max_cols}')
    if isinstance(writer, ExcelWriter):
        need_save = False
    else:
        writer = ExcelWriter(stringify_path(writer), engine=engine)
        need_save = True
    formatted_cells = self.get_formatted_cells()
    writer.write_cells(formatted_cells, sheet_name, startrow=startrow, startcol=startcol, freeze_panes=freeze_panes)
    if need_save:
        writer.save()