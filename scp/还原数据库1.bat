@echo off

del elife.sqlite3 &&^
copy   elife-bak1.sqlite3   elife.sqlite3


echo:
echo:
echo 数据库还原成功，建议重启 elife-rc-scp 防止缓存脏数据
echo:
echo:

pause