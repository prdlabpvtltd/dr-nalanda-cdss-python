class DrNalandaError(Exception):
    """Base exception for all Dr. Nalanda CDSS errors."""
    pass

class APIConnectionError(DrNalandaError):
    """Raised when unable to reach the Dr. Nalanda CDSS API server."""
    pass

class DisclaimerRequiredError(DrNalandaError):
    """Raised when the mandatory statutory disclaimer has not been acknowledged."""
    pass
