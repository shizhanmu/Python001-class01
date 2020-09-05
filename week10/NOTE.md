# 学习笔记

## 作业使用说明：
  - 在mysql中创建名为 smzdm 的数据库
  - 先用 mysqldump 导入 stat_table.sql，然后导入 qipaoshui_cleaned.sql。
  - 在 MyDjango目录中运行： python manage.py runserver

## 1. pandas和python中的三种空值 None, np.NaN, ""
  空值类型比较

```
>>> from numpy import NaN
>>> import numpy as np
>>> import pandas as pd
>>> type(NaN)
<class 'float'>
>>> type(None)
<class 'NoneType'>
>>> type("")
<class 'str'>
```

## 2. 用pandas读取mysql数据库用 DataFrame.read_sql

```python
conn = pymysql.connect(host, username, password, db, charset='utf8mb4')
sql = f'SELECT * FROM `qipaoshui`'
df = pd.read_sql(sql, conn)
```

## 3. 将pandas数据写入mysql：DataFrame.to_sql

   数据库的表无需事先创建，to_sql会根据DataFrame自动创建表。
   参数说明：

```python
DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)
```

  - name：输出的表名
  - con：连接mysql数据库的引擎要用pymysql和sqlalchemy，
  
```python
    from sqlalchemy import create_engine
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{db}')
```

  - if_exists：三种模式{“fail”,“replace”,"append"}，默认是"fail"。
  fail：若表存在，引发一个ValueError；
  replace：若表存在，先删掉原数据再写入；
  append：若表存在，将数据添加到原表数据的后面。
  - index：是否将DataFrame的index单独写到一列中，默认为“True”
  - index_label：当index为True时，指定列作为DataFrame的index输出
  - chunksize：int 指定每次批量写入的行数，缺省为所有行一次写入 
  - dtype：指定列的数据类型，字典形式存储{column_name: sql_dtype}，常见数据类型是sqlalchemy.types.INT()和sqlalchemy.types.CHAR(length=x)。注意：INT和CHAR都需要大写，INT()不用指定长度。

  ## 4. 使用pandas更新DataFrame某一列（值位于另一个DataFrame）
```python
import pandas as pd
df1=pd.DataFrame({'id':[1,2,3],'name':['Andy1','Jacky1','Bruce1']})
df2=pd.DataFrame({'id':[1,2],'name':['Andy2','Jacky2']})
s = df2.set_index('id')['name']
df1['name'] = df1['id'].map(s).fillna(df1['name']).astype(str)
```
