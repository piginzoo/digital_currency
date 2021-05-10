import argparse
import logging
from datetime import datetime

from dca import utils
from dca.utils import load_data

logger = logging.getLogger(__name__)


def main(code, start, end):
    data = load_data(code)
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    filter_data = data.loc[start_date:end_date]
    logger.debug("%r=>%r过滤后，总体[%d]条=>过滤后[%d]条", start, end, len(data), len(filter_data))
    start_close_price = filter_data.iloc[0]['Close']
    end_close_price = filter_data.iloc[-1]['Close']
    profit = (end_close_price - start_close_price) / start_close_price
    logger.info("从[ %s => %s ] 收益率：%.2f%%", start,end, profit * 100)


# python -m dca.analysis --code DOGE --start 2019-1-1 --end 2021-1-1
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--code', '-c', type=str)
    parser.add_argument('--start', '-s', type=str)
    parser.add_argument('--end', '-e', type=str)
    args = parser.parse_args()

    utils.init_logger()
    main(args.code, args.start, args.end)
