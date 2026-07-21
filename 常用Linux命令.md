#### 关机命令：  shutdown -h now 立即关机
#### ls
- ls:查看当前文件夹内容

- ls 目录名：表示显示指定目录内容

- ls / 显示根目录内容

- ls /bin  显示根目录下的bin目录下的内容

- ls -a 显示所有文件，包含隐藏的

- ls -l  显示文件的信息

- ls -al 显示所有文件的信息，包含隐藏的

- ls 结合通配符 *代表任意字符    ?代表任意一个字符    []代表范围

#### cd:切换文件夹
#### touch：touch a.txt  创建空文件
#### echo:  echo  xxx -> a.txt 创建带有内容的文件
#### mkdir 目录名：创建目录
#### mkdir -p a/b/c  创建一个有嵌套关系的多级目录
#### rm 文件名: 删除文件
#### rm -r 目录名： 删除目录
#### --help:简化版帮助信息
#### man 命令：详细帮助信息：
   - 空格：下一页
   - b 上一页
   - q 退出
#### pwd:当前所在目录
#### chmod 修改文件权限
- rwx 读写执行
- 421 数字法修改
- u： 用户
- g：组
- o：其他用户
- a：所有用户
#### cat test.txt 查看文件内容，一次性打印所有内容
#### less test.txt 查看文件内容，分页查看，空格翻页，q退出
#### more test.txt 简易分页
#### tail test.txt 查看末尾10行
#### tail -f log.log 实时跟踪日志
#### tail -n 100 test.txt
#### head test.txt 查看前10行
#### cp a.txt /temp/   复制文件到temp目录
#### cp -r folder /temp/ 复制文件夹
#### mv old.txt new.txt 重命名文件
#### mv file /temp/  移动文件
#### find / -name "*.log"  全盘搜索后缀log文件
#### find ./ -type f  只搜索文件
#### grep "关键词" file.txt 在文件中匹配文字
#### grep -i "error" log 忽略大小写搜索
#### grep -r "404" ./ 递归搜索文件夹内所有文件