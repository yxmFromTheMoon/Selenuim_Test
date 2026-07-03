### Selenium Web浏览器自动化方案

### 1.简介

通过Selenium，我们可以写出自动化程序，像人一样在浏览器里操作web界面。 比如点击界面按钮，在文本框中输入文字 等操作。
而且还能从web界面获取信息。 比如获取 火车、汽车票务信息，招聘网站职位信息，财经网站股票价格信息 等等，然后用程序进行分析处理。

#### 原理图：

@selenium原理图.png

#### selenium 自动化流程如下：

1.自动化程序调用Selenium 客户端库函数（比如点击按钮元素）

2.客户端库会发送Selenium 命令 给浏览器的驱动程序

3.浏览器驱动程序接收到命令后 ,驱动浏览器去执行命令

4.浏览器执行命令

5.浏览器驱动程序获取命令执行的结果，返回给我们自动化程序

6.自动化程序对返回结果进行处理

### 2.使用

#### 关闭日志

options = webdriver.ChromeOptions()<br>
options.add_experimental_option('excludeSwitches', ['enable-logging'])<br>
wd = webdriver.Chrome(options=options)

#### 选择元素的方法

1.根据属性ID选择（规范来讲id必须是当前html中唯一的）

返回WebElement对象，找不到元素会抛出异常
element = wd.find_element(By.ID,'id') 查找元素
element.send_keys('xxx') 给元素赋值

2.根据class属性来选择
WebElement列表，查询所有class符合的元素
wd.find_elements(By.CLASS_NAME,'class')

3.根据标签名来选择
wd.find_elements(By.TAG_NAME,'nav')

4.根据WebElement对象选择

element = wd.find_element()
element对象也可以调用find_element方法,在这个WebElement下来查找

#### 等待元素出现

wd.implicitly_wait(1)

隐式等待,查找元素时进行等待.原理：循环查找元素,找不到时隔0.5s再去找，一直到指定的时间为止

#### 操控元素

1.点击元素 click()

2.在元素中输入字符串

clear()清除输入

send_keys('xxx') 输入值

3.获取元素包含的信息,比如文本内容,元素的属性

element.text属性，获取展示在界面上的

element.get_attribute('属性名称')：获取属性

element.get_attribute('outerHTML')获取整个元素的html标签

element.get_attribute('innerHTML')获取元素内部的html标签

输入框类型的值不能直接用text获取,要用get_attribute("value")获取

get_attribute("innerText")、get_attribute("textContent")
获取文本内容，适合文本内容没有展示在界面上或者没有完全展示在界面上

#### CSS表达式

wd.find_elements(By.CSS_SELECTOR,'css表达式')

#### 使用标签选择时,和By.TAG_NAME使用方式一样

#### 根据id来选择,前面加一个#(#id)

#### 根据class来选择,前面加一个.

xxx > span,一级范围 查找直接子元素（儿子）
xxx span 二级范围 查找后代元素，只要在父标签范围内就行（孙子）
多级用多个 > 连接
限定范围选择：使用方式 xxx > span

#### 使用CSS选择器根据属性选择,使用方括号，注意引号

多个属性拼接[][]
wd.find_elements(By.CSS_SELECTOR,'[href="xxxx"']')

wd.find_elements(By.CSS_SELECTOR,'[href]') 也可以

#### 选择多个标签

#id > span,#id > p

#### 按次序选择

nth-child()第几个子元素

nth-last-child()倒数的第几个元素

nth-of-type()某种类型的第几个
span:nth-of-type(1)

nth-last-of-type()倒数的某种类型的第几个元素
span:nth-last-of-type(1)

偶数节点、奇数节点

nth-child(even)、nth-child(odd) 按照父节点中的位置选取奇偶节点

nth-of-type(even)、nth-of-type(odd)先把类型选取出来,再选取奇偶节点

h3 + span 紧跟h3后的span

h3 ～ span h3后所有的span

### frame切换

wd.switch_to.frame(xx),可以传id或者name或者WebElement对象
在内部frame操作完后要切回到主html中，调用wd.switch_to_default_content()

### 切换到新的窗口

wd.switch_to_window(),切换到新的窗口
wd.window_handlers会存储每个打开的页面的句柄，遍历句柄来处理
最好是在打开新的窗口操作完之后关掉该窗口，调用wd.close(),再切回原来的窗口

### 选择框

radioBox:

默认选中的'input[name=teacher][checked]'

当前选中的'input[name=teacher]:checked'

CheckBox:
有正反选,选择其他选项时可以把选中的先取消选择,再选择要选择的item

Select:
有专门提供的Select类，通过Select(find_element())实例化

select.all_selected_options()返回当前选中的所有option元素

select_by_value()根据option元素的value属性值选择

select_by_index()根据索引选择

select_by_visible_text()根据显示的文本选择

deselect_xxxx和select系列方法一样,取消选中

### 其他操作 鼠标右键点击、双击、移动鼠标到某个元素、鼠标拖拽

使用ActionChains(wd)包装wd对象

ac.move_to_element(WebElement).perform(),鼠标悬停到元素上

ac.drag_and_drop(WebElement source,WebElement target).perform()拖放

### 弹框处理

1.alert弹框
有一个按钮的弹框
wd.switch_to_alert().accept() 点击弹框的确定按钮
wd.switch_to_alert().text 获取弹框内容

2.confirm弹框
有两个按钮的弹框
accept()、dismiss()

3.Prompt
有两个按钮和一个输入框
wd.switch_to_alert().send_keys()赋值输入框

有些弹窗是html元素,用定位查找就可以

### XPath 选择元素

/代表根节点

绝对路径：/html/body/div 表示查找html下的body下的div元素

相对路径：//div   //表示只要出现div,不管层级都会被选中
//div/* 通配符，选择所有子节点

支持根据属性选择：

[@属性名='属性值']

找所有带某个属性的元素，把属性值去掉即可
根据id //*[@id='xx']

根据class //*[@class='xx'],有多个class属性时，都要写上

包含某个属性值： //*[contains(@style,'color')] style属性值包含color

以猴哥属性值开头： //*[start-with(@style,'color')] style属性值以color开头

以某个属性值结尾： //*[ends-with(@style,'color')] style属性值以color结尾 (xpath2.0才支持)

某类型的第几个子元素：//p[2]

任何类型的第几个子元素： //*[2]

倒数第几个子元素：//p[last()-n]

和CSS不同的地方：

支持范围选择：

//p[position()<=2] 范围小于等于2

可以选择父节点：

/..表示选择父节点,适合查找父节点没有什么特征，但是他的子节点有明显特征的元素

可以选择前后兄弟节点：

前兄弟节点：preceding-sibling::  冒号后还可以指定标签类型
后兄弟节点：following-sibling::

wd.find_element(By.XPATH,'path')

使用XPATH查找某个元素内部的元素时，要在//前加一个.


