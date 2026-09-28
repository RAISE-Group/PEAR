@classmethod
def _convert_to_style(cls, style_dict, num_format_str=None):
    """
        converts a style_dict to an xlwt style object

        Parameters
        ----------
        style_dict : style dictionary to convert
        num_format_str : optional number format string
        """
    import xlwt
    if style_dict:
        xlwt_stylestr = cls._style_to_xlwt(style_dict)
        style = xlwt.easyxf(xlwt_stylestr, field_sep=',', line_sep=';')
    else:
        style = xlwt.XFStyle()
    if num_format_str is not None:
        style.num_format_str = num_format_str
    return style