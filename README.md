silkpg
======

Postgresql Foreign Data Wrapper for Silk

Initial version which needs optimising, but works.  

1) Install multicorn

2) Install silkpg (python setup.py install)

3) Run sql commands in silk.sql (create server, create foreign table)

4) Test and compare

```
$ rwfilter  --start=2000/01/01 --end=2020/01/01  --all-destination=stdout | rwstats --fields=sip --bytes --count 10
INPUT: 325416 Records for 23796 Bins and 9881665784 Total Bytes
OUTPUT: Top 10 Bins by Bytes
            sIP|               Bytes|    %Bytes|   cumul_%|
192.234.207.174|           588038496|  5.950803|  5.950803|
134.176.116.233|           390631226|  3.953091|  9.903894|
   59.223.61.86|           287629308|  2.910737| 12.814631|
169.177.145.225|           249016228|  2.519982| 15.334614|
     208.4.1.78|           228524054|  2.312607| 17.647220|
 206.241.44.130|           182132498|  1.843136| 19.490356|
 204.116.120.26|           142313365|  1.440176| 20.930532|
  167.130.77.75|           135716770|  1.373420| 22.303952|
 157.26.249.235|           131732957|  1.333105| 23.637056|
  209.28.59.129|           120280839|  1.217212| 24.854268|
```

```
silk=# select sip,sum(bytes) as bytes from silk group by sip order by bytes desc limit 10; 
       sip       |    cc     
-----------------+-----------
 192.234.207.174 | 588038496
 134.176.116.233 | 390631226
 59.223.61.86    | 287629308
 169.177.145.225 | 249016228
 208.4.1.78      | 228524054
 206.241.44.130  | 182132498
 204.116.120.26  | 142313365
 167.130.77.75   | 135716770
 157.26.249.235  | 131732957
 209.28.59.129   | 120280839

```
