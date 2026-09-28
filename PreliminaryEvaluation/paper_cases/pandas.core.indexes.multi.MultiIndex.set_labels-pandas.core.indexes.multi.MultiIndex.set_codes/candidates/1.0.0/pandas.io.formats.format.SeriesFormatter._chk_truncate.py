def _chk_truncate(self) -> None:
    from pandas.core.reshape.concat import concat
    self.tr_row_num: Optional[int]
    min_rows = self.min_rows
    max_rows = self.max_rows
    truncate_v = max_rows and len(self.series) > max_rows
    series = self.series
    if truncate_v:
        max_rows = cast(int, max_rows)
        if min_rows:
            max_rows = min(min_rows, max_rows)
        if max_rows == 1:
            row_num = max_rows
            series = series.iloc[:max_rows]
        else:
            row_num = max_rows // 2
            series = series._ensure_type(concat((series.iloc[:row_num], series.iloc[-row_num:])))
        self.tr_row_num = row_num
    else:
        self.tr_row_num = None
    self.tr_series = series
    self.truncate_v = truncate_v