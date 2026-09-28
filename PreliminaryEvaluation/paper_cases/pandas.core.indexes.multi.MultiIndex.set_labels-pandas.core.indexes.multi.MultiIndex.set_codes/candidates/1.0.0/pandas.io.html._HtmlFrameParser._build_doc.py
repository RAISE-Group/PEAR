def _build_doc(self):
    """
        Return a tree-like object that can be used to iterate over the DOM.

        Returns
        -------
        node-like
            The DOM from which to parse the table element.
        """
    raise AbstractMethodError(self)