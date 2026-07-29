import logging
def get_logger(name: str = "customer-analytics") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))
        logger.addHandler(h)
    return logger
