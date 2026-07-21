Postman 接口测试全套核心知识点.md
### 一、接口基础分类（P2）
#### 外部接口：对外提供服务，仅需测试正向业务用例
#### 内部接口：仅供公司内部系统调用（预算系统、保单系统等），核心覆盖正向流程
接口测试核心前置：先区分接口归属，再规划测试范围
### 二、完整接口测试流程（P3）
需求梳理 → 2. 接口文档研读 → 3. 测试用例设计 → 4. Postman 手工调试接口
接口关联处理 → 6. 编写断言校验结果 → 7. 批量执行用例
数据驱动批量测试 → 9. Newman 命令行运行 → 10. Jenkins 持续集成自动化
### 三、Postman 基础操作模块
1. 环境搭建（P5、P6）
安装、注册、登录 Postman 客户端 / 网页版
主界面分区：Collections 集合、请求编辑区、响应结果区、环境变量面板
2. HTTP 请求实战（P7、P8）
GET 请求
参数放置位置：Params 查询参数
适用场景：查询数据、无数据修改操作
POST 请求
传参类型：form-data、x-www-form-urlencoded、raw (JSON)、binary 文件上传
GET 与 POST 核心区别：
GET 参数拼接在 URL，长度受限，明文可见，不适合传敏感数据
POST 参数放在请求体，无长度限制，适合提交表单、JSON、文件
3. 请求头处理（P17）
必带请求头：Content-Type、token、User-Agent、Cookie
常见 ContentType：application/json、multipart/form-data、application/x-www-form-urlencoded
### 四、变量与接口关联（自动化核心 P9-P11）
1. 变量层级
全局变量 Global：所有集合、请求共用，生命周期全局
环境变量 Environment：仅当前选中环境生效，多项目隔离使用
变量调用语法：{{变量名}}
2. 接口关联两种提取方案

（1）JSON 提取器（P10，最常用）
在 Tests 脚本中提取返回 JSON 字段，存入变量
js 运行
// 示例提取token
var res = pm.response.json();
pm.environment.set("token", res.data.token);

（2）正则表达式提取（P11）
适配非标准 JSON 返回、HTML 文本、不规则返回数据
js
运行
// 正则提取示例
var reg = /"token":"(.*?)"/;
var match = reg.exec(pm.response.text());
pm.environment.set("token", match[1]);
### 五、动态参数（P12）
内置动态参数

{{$timestamp}}：时间戳

{{$randomInt}}：随机数字

{{$randomEmail}}：随机邮箱

自定义动态参数：Tests/Pre-request Script 编写 JS 生成自定义数据
### 六、文件上传与业务闭环（P13）
form-data 模式实现图片、文档上传接口测试
业务闭环：登录→获取 token→查询→新增→修改→删除完整业务链路串联测试
### 七、断言体系（P14）
三类断言

常规状态断言：校验响应码、响应时间、响应头

js 运行

pm.test("响应码200", function () {
  pm.response.to.have.status(200);
});

动态参数断言：校验返回 JSON 指定字段值、字段存在性
全局断言：集合级别统一添加，所有请求共用校验规则
### 八、批量执行与数据驱动（P15、P16）
批量运行 Collection：Runner 面板执行集合，可视化查看成功 / 失败用例
数据驱动测试
支持文件：CSV、JSON
使用场景：登录接口多账号、参数边界值批量校验
文件内字段直接通过{{表头字段名}}调用
### 九、Mock Server 模拟接口（P18）
作用：后端未开发完成时，模拟接口返回数据，前端 / 测试先行调试
配置：定义请求匹配规则、自定义返回 JSON、状态码、延时
### 十、鉴权体系（P19）
Cookie 鉴权：登录自动保存 Cookie，同域名请求自动携带
Token 鉴权（主流）
登录接口提取 token 存入环境变量
后续接口请求头添加 Authorization: Bearer {{token}}
### 十一、Newman 命令行执行（P21）
作用：脱离 GUI，服务器 / 终端批量运行 Postman 集合
常用参数：指定集合文件、环境文件、输出测试报告
输出格式：控制台文本、JSON 报告、搭配 Allure 生成可视化测试报告
### 十二、CI/CD 持续集成（P22）
Postman + Newman + Jenkins 自动化流水线流程：
Jenkins 拉取 Postman 集合文件
调用 Newman 执行接口用例
生成测试报告
失败用例邮件 / 消息告警
更新版支持 Postman CLI 替代旧 Newman 方案，集成更简洁
### 十三、进阶实战专题
加密接口测试：请求参数加密、响应解密校验

接口自动化完整技术体系三阶段：手工接口→脚本自动化→CI 持续测试

接口性能批量测试：Runner 批量加压简易性能验证

十四、接口测试用例设计思路

正向用例：正常参数、完整业务流程

反向用例：空参数、超长参数、非法字符、不存在 ID

边界值：最大 / 最小数值、长度临界值

异常场景：无 token、错误 token、权限不足、重复提交