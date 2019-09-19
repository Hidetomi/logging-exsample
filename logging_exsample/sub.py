import logging

log = logging.getLogger(__name__)


def print_log():
    log.debug("sub")
    log.info("sub")
    log.warning("sub")
    log.error("sub")
