# 如何配置

1. 下载安装[python 3.8](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)
，如果需要安装virtualenv，可以[参考](https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480).

2. 安装依赖包：pip install requirements.txt


# 如何爬取、显示、看收益

**以狗狗币为例：**

1、爬取狗狗币

会去著名的数字币网站自动爬取所有的交易数据。

```shell script
# 爬取
python -m dca.crawler --code DOGE
```

2. 显示走势
```shell script
# 显示
python -m dca.show --code DOGE
```

3. 分析
```shell script
# 分析
python -m dca.analysis --code DOGE --start 2019-1-1 --end 2021-1-1

```


