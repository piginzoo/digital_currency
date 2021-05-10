# 数字币收益率计算小工具

## 介绍

这个是为朋友开发的一个小工具，可以实现以下功能：
- 按照数字币代码，可以获得其所有的交易数据（每天的开盘、收盘、最高、最低等价格）
- 可以使用图像化展示交易数据走势
- 可以按照时间来计算收益率

数字币代码可以通过访问[coinmarketcap](https://coinmarketcap.com/)获得！

## 实现机制

我使用了一个[Github数字币获取项目 - cryptoCMD](https://github.com/guptarohit/cryptoCMD)，
来获取[coinmarketcap.com](https://coinmarketcap.com/)上的数字币的交易信息，然后保存到data目录中，csv格式。

然后通过程序分析其收益率。

## 如何配置

1. 下载安装[python 3.8](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)
，如果需要安装virtualenv，可以[参考](https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480).

2. 安装依赖包：pip install -r requirements.txt


## 如何爬取、显示、看收益

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


