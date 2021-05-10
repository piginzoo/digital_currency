import datetime
import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)

def init_logger(level=logging.DEBUG):
    # logging.basicConfig(format='%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s : %(message)s',
    #                     level=logging.DEBUG,
    #                     handlers=[logging.StreamHandler()])
    logging.basicConfig(format='%(levelname)s : %(message)s',
                        level=level,
                        handlers=[logging.StreamHandler()])


def load_data(code):
    csv_path = "data/{}.csv".format(code)
    if not os.path.exists(csv_path):
        logger.error("数据文件 %s 不存在", csv_path)
        return None

    try:
        dateparse = lambda x: datetime.datetime.strptime(x, "%d-%m-%Y")
        df = pd.read_csv(csv_path,
                         index_col='Date',
                         parse_dates=True,
                         date_parser=dateparse)
        df.sort_index(inplace=True)
        # logger.debug(df)
    except:
        logger.exception("解析[%s]数据失败", code)
        return None
    logger.info("加载了[%s]数据，行数：%d", csv_path, len(df))
    return df

