class PageLoadingError(Exception):

    """Class intended for page failures (status code 404, 500, and so on)."""


class PageContentError(Exception):

    """Class intended for page content that does not seem valid at now."""


class ItemNotFoundError(Exception):

    """Class intended for item not found during scraping."""
