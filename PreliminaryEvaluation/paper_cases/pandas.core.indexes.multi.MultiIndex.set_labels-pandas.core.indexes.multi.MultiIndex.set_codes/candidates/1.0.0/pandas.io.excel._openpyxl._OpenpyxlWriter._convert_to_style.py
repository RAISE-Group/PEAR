@classmethod
def _convert_to_style(cls, style_dict):
    """
        Converts a style_dict to an openpyxl style object.

        Parameters
        ----------
        style_dict : style dictionary to convert
        """
    from openpyxl.style import Style
    xls_style = Style()
    for key, value in style_dict.items():
        for nk, nv in value.items():
            if key == 'borders':
                xls_style.borders.__getattribute__(nk).__setattr__('border_style', nv)
            else:
                xls_style.__getattribute__(key).__setattr__(nk, nv)
    return xls_style