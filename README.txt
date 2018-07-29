createDb.py：用3755个一级汉字穷举方法生成2个汉字的姓名及MD5加密库，使用PyMySQL模块写入MYSQL数据库。使用InnoDB引擎，只有ID一个primary index的情况下，跑完脚本生成1000多万记录约40多分钟。

createDbMultiThread.py：目的功能同上，计划使用多线程加快创建速度，但应逻辑错误，创建的库不全；缺少不同string里汉字组合。

decodeName.py：批量解密MD5加密姓名，使用方法为"python decodeName.py hashname.xlsx"。

数据库相关:数据库包含ID，NAME，HASHNAME三列，共约1400万数据，使用"select NAME from user where HASHNAME='7a7884a510a2fe4707ede9f57ed763cd'"查询需要约20s,为HASHNAME这一列增加index后查询时间缩短到0.12s。增加index可以加快查询速度，但会减慢插入更新等操作的速度，因为插入更新时也要维护索引。索引文件可能比数据文件更快达到文件上限。
