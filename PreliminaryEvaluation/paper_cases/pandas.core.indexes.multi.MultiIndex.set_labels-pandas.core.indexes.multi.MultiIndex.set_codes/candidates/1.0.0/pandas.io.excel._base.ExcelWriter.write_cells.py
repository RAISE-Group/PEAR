@abc.abstractmethod
def write_cells(self, cells, sheet_name=None, startrow=0, startcol=0, freeze_panes=None):
    """
        Write given formatted cells into Excel an excel sheet

        Parameters
        ----------
        cells : generator
            cell of formatted data to save to Excel sheet
        sheet_name : str, default None
            Name of Excel sheet, if None, then use self.cur_sheet
        startrow : upper left cell row to dump data frame
        startcol : upper left cell column to dump data frame
        freeze_panes: int tuple of length 2
            contains the bottom-most row and right-most column to freeze
        """
    pass