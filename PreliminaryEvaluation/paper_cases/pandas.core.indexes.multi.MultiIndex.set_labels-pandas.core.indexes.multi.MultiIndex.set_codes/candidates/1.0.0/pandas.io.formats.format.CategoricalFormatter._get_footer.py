def _get_footer(self) -> str:
    footer = ''
    if self.length:
        if footer:
            footer += ', '
        footer += 'Length: {length}'.format(length=len(self.categorical))
    level_info = self.categorical._repr_categories_info()
    if footer:
        footer += '\n'
    footer += level_info
    return str(footer)