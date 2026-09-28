def parse(self, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, dtype=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=True, mangle_dupe_cols=True, **kwds):
    validate_header_arg(header)
    ret_dict = False
    if isinstance(sheet_name, list):
        sheets = sheet_name
        ret_dict = True
    elif sheet_name is None:
        sheets = self.sheet_names
        ret_dict = True
    else:
        sheets = [sheet_name]
    sheets = list(dict.fromkeys(sheets).keys())
    output = {}
    for asheetname in sheets:
        if verbose:
            print(f'Reading sheet {asheetname}')
        if isinstance(asheetname, str):
            sheet = self.get_sheet_by_name(asheetname)
        else:
            sheet = self.get_sheet_by_index(asheetname)
        data = self.get_sheet_data(sheet, convert_float)
        usecols = _maybe_convert_usecols(usecols)
        if not data:
            output[asheetname] = DataFrame()
            continue
        if is_list_like(header) and len(header) == 1:
            header = header[0]
        header_names = None
        if header is not None and is_list_like(header):
            header_names = []
            control_row = [True] * len(data[0])
            for row in header:
                if is_integer(skiprows):
                    row += skiprows
                data[row], control_row = _fill_mi_header(data[row], control_row)
                if index_col is not None:
                    header_name, _ = _pop_header_name(data[row], index_col)
                    header_names.append(header_name)
        if is_list_like(index_col):
            if not is_list_like(header):
                offset = 1 + header
            else:
                offset = 1 + max(header)
            if offset < len(data):
                for col in index_col:
                    last = data[offset][col]
                    for row in range(offset + 1, len(data)):
                        if data[row][col] == '' or data[row][col] is None:
                            data[row][col] = last
                        else:
                            last = data[row][col]
        has_index_names = is_list_like(header) and len(header) > 1
        try:
            parser = TextParser(data, names=names, header=header, index_col=index_col, has_index_names=has_index_names, squeeze=squeeze, dtype=dtype, true_values=true_values, false_values=false_values, skiprows=skiprows, nrows=nrows, na_values=na_values, parse_dates=parse_dates, date_parser=date_parser, thousands=thousands, comment=comment, skipfooter=skipfooter, usecols=usecols, mangle_dupe_cols=mangle_dupe_cols, **kwds)
            output[asheetname] = parser.read(nrows=nrows)
            if not squeeze or isinstance(output[asheetname], DataFrame):
                if header_names:
                    output[asheetname].columns = output[asheetname].columns.set_names(header_names)
        except EmptyDataError:
            output[asheetname] = DataFrame()
    if ret_dict:
        return output
    else:
        return output[asheetname]