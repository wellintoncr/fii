class PageLoadingFailed(Exception):
    """Class intended for page failures (status code 404, 500, and so on)."""
    def __init__(self, args):
        super().__init__(args)

class PageContentInvalid(Exception):
    """Class intended for page content that does not seem valid at now."""
    def __init__(self, args):
        super().__init__(args)

class ItemNotFound(Exception):
    """Class intended for item not found during scraping."""
    def __init__(self, args):
        super().__init__(args)
