def parse_tables(self):
    """
        Parse and return all tables from the DOM.

        Returns
        -------
        list of parsed (header, body, footer) tuples from tables.
        """
    tables = self._parse_tables(self._build_doc(), self.match, self.attrs)
    return (self._parse_thead_tbody_tfoot(table) for table in tables)