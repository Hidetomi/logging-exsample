import yaml
from pathlib import Path
from logging import getLogger
from logging.config import dictConfig
from logging_exsample import sub

with Path("./log.yml").open("r", encoding="utf-8") as __stream:
    dictConfig(yaml.full_load(__stream))
log = getLogger(__name__)


def main():
    log.debug("sub")
    log.info("sub")
    log.warning("sub")
    log.error("sub")
    sub.print_log()


if __name__ == "__main__":
    main()
