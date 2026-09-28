def get_sheet_by_index(self, index: int):
    return self.book.get_sheet(index + 1)