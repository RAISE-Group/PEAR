@property
def row_levels(self) -> int:
    if self.fmt.index:
        return self.frame.index.nlevels
    elif self.show_col_idx_names:
        return 1
    return 0