"""
Test runner for github tests
"""
import sys

from loguru import logger

from backends.redoubt.apps import RedoubtAppBackend
from backends.redoubt.tokens import RedoubtTokensBackend
from seasons.s3_5 import S3_5_apps, S3_5_tokens

if __name__ == "__main__":
    backend = RedoubtTokensBackend()
    season = S3_5_tokens
    res = backend.calculate(season, dry_run=len(sys.argv) > 1 and sys.argv[1] == '--dryrun')
    logger.info(res)