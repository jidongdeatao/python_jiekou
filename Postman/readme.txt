使用说明：
  一.安装配置
    获取POSTMAN工具包，打开Google浏览器：
      菜单栏 -> 更多工具 -> 扩展程序 -> 加载已解压的扩展程序 -> 启用Postman
  二.具体使用介绍
  1.Collections：在Postman中，Collection类似文件夹，可以把同一个项目的请求放在一个Collection里方便管理和分享，Collection里面也可以再建文件夹。
  如果做API文档的话，可以每个API对应一条请求， 如果要把各种输入都测到的话，就需要每条测试一条请求了。
  这里我新建了一个example用于介绍整个流程，五个API对应五条请求。这个 Collection可以通过https://www.getpostman.com/collections/96b64a7c604072e1e4ee 导入你自己的Postman中。
  上面的黑字注册是请求的名字，如果有Request description的话会显示在这下面。下面的蓝字是保存起来的请求结果，点击可以载入某次请求的参数和返回值。我会用这个功能给做客户端的同事展示不同情况下的各种返回值。保存请求的按钮在15.
  2.选择HTTP Method的地方，各种常见的不常见的非常全。
  3.请求URL，两层大括号表示这是一个环境变量，可以在右上角的位置选择当前的environment，环境变量就会被替换成该environment里variable的值。
    设置environment variables和global variables，点击右边的x可以快速查看当前的变量。
    点击可以设置URL参数的key和value，变量名称用双花阔号括起来{{ }}
  4.点击发送请求
  点击保存请求到Collection，如果要另存为的话，可以点击右边的下箭头
  5.设置鉴权参数，可以用OAuth之类的
  6.自定义HTTP Header，有些因为Chrome愿意不能自定义的需要另外装一个插件Interceptor，在右上角上面一行的卫星那里
  7.设置Request body，在发起请求之前执行的脚本，例如request body里的那两个random变量，就是每次请求之前临时生成的。
  8.收到response之后执行的测试，测试的结果会显示在中下的位置
    有四种形式可以选择，form-data主要用于上传文件。x-www-form-urlencoded是表单常用的格式。raw可以用来上传JSON数据
    返回数据的格式，Pretty可以看到格式化后的JSON，Raw就是未经处理的数据，Preview可以预览HTML页面
点击保存请求到Collection，如果要另存为的话，可以点击右边的下箭头
  9.测试执行的结果，一共几个测试，通过几个。
这个界面就是免费版的主要内容，和其他API测试工具相比，已经足够好用。如果要使用自动化测试，需要购买9.99美金的Jetpacks，暂时不想购买的话可以试一下 Team版Postman 。现在是可以免费试用的，不但拥有Jetpacks的功能，还能与其他账户同步Collection。
