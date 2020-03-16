# FlaskDay01







### 插件使用

1. 安装插件
2. 初始化插件
3. 调用插件



### flask-script

1. 安装
   - pip install  flask-script
2. 初始化
   - manager = Manager（app）
3. 调用
   - 在run的地方修改，修改manager.run()
4. 接收参数
   - p  端口 port
   - h  主机  host
   - d  调试模式  debug
   - r   重启（重新加载） reload（restart）





### 蓝图

1. 宏伟蓝图（宏观规划）
2. 蓝图也是一种规划，主要用来规划urls（路由）
3. 蓝图基本使用
   - 安装
     - pip install flask-blueprint
     - 初始化蓝图
     - 调用蓝图进行路由注册





### views路由

1. 路由对应视图函数，并且可以接收参数
2. 语法   <converter:var_name>
3. 书写的converter可以省略，默认类型就是string
4. converter
   - string 字符串，接收的时候也是str， 匹配到 / 的时候是匹配结束
   - path 路径，接收的时候也是str， / 只会当作字符串中的一个字符处理
   - any 任意一个， 指的是any中提供的任意一个，类似于SQL查询中的  in 
     - any(a,b,c,d)   只能匹配我们any后这些路径
   - uuid   必须是uuid格式
   - int  同上
   - float   同上



### 请求方式

1. 默认支持GET，HEAD，OPTIONS
2. 如果想支持某一请求方式，需要自己手动指定
3. 在路由上，使用methods=["GET","POST","PUT","DELETE"]







### 反向解析

1. url_for()
   - 蓝图中使用
     - 蓝图的名字（创建蓝图时的第一个参数）
     - 函数的名字 
     - url_for("蓝图名.函数名")





### Request

1. args
   - get请求参数的包装，args是一个ImmutableMultiDict对象，类字典结构对象
   - 数据存储也是key-value
   - 外层是大列表，列表中的元素是元组，元组中左边是key，右边是value
2. form
   - 存储结构个args一致
   - 默认是接收post参数
   - 还可以接收 PUT，PATCH参数

### Response

1. Response是由开发者创建的
2. 创建方式
   - 直接返回字符串
   - render_template 渲染模板，将模板转换成字符串
   - make_response 创建一个响应，是一个真正的Response
3. 返回配置
   - 内容
     - 直接书写就ok了
     - 将内容传递进去
   - 状态码
     - 字符串形式直接将状态码添加到return 的第二个参数
     - 如果make形势，直接添加到make的第二个参数上
4. 返回重定向
   - redirect  重定向  302
   - url_for  反向解析
5. 抛出异常，终止程序执行
   - abort
   - abort 状态码
6. errorhandler
   - 异常捕获
   - 可以根据状态或 Exception进行捕获
   - 函数中要包含一个参数，参数用来接收异常信息







### 会话技术

1. Cookie
   - 客户端会话技术，浏览器的会话技术
   - 数据全都是存储在客户端中
   - 存储使用的键值对结构进行的存储
   - 特性
     - 支持过期时间
     - 默认会自动携带本网站的所有cookie
     - 根据域名进行cookie存储
     - 不能跨域名
     - 不能跨浏览器
   - Cookie是通过服务器创建的Response来创建的
2. Session
   - 服务端的会话技术
   - 所有数据存储在服务器中
   - 默认存储在内存中
     - django默认做了数据持久化（存在了数据库中）
   - 存储结构也是key-value形势，键值对
   - session 是离不开cookie的
3. Token
   - 手动实现的session
   - 如果在web开发中没有cookie，那么token也是不能使用的
   - 脱了网web前端，Token是可以使用的
     - 传输给客户端，客户端保存
     - 在请求的时候，将token值再传输回来





### 类视图，响应

1. 思想
2. 拆分
   - 按功能进行拆分
   - 当需要多个功能的时候，使用继承来实现

### 

### home

1. 代码熟悉
2. 自己实现一个token









