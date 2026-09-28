def set_table_attributes(self, attributes):
    """
        Set the table attributes.

        These are the items that show up in the opening ``<table>`` tag
        in addition to to automatic (by default) id.

        Parameters
        ----------
        attributes : str

        Returns
        -------
        self : Styler

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4))
        >>> df.style.set_table_attributes('class="pure-table"')
        # ... <table class="pure-table"> ...
        """
    self.table_attributes = attributes
    return self