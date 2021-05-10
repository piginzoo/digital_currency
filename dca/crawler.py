import argparse
import logging

from cryptocmd import CmcScraper

from dca import utils

"""
参考：# https://github.com/guptarohit/cryptoCMD
"""

logger = logging.getLogger(__name__)


def main(code):
    # initialise scraper without time interval
    scraper = CmcScraper(code)

    # get raw data as list of list
    headers, data = scraper.get_data()

    # get data in a json format
    xrp_json_data = scraper.get_data("json")

    # export the data as csv file, you can also pass optional `name` parameter
    scraper.export("csv", name="data/" + code)

    logger.info("爬取[%s]完成！", code)


# python -m fund_analysis.invest.show --code 519778
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--code', '-c', type=str, default=None)
    args = parser.parse_args()
    utils.init_logger()
    main(args)
