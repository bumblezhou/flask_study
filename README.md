# flask_study

##功能实现
    1.做一个用户名/密码的登录认证。
    2.通过认证的用户，因为安全原因考虑，只能存储其登录后的token到sessionStorage。
    3.通过认证后，页面跳到管理首页面。管理首页面的所有静态资源都要求加在HTTP headers中加token的方式进行加载。
    4.登录页面可以不用在HTTP header中加载token而直接加载出来。
    5.后端登录验证的api接口也可以不用在 HTTP header中加载token而直接调用

##参考引用
    1.动态加载字体： https://usefulangle.com/post/74/javascript-dynamic-font-loading
    2.javascript正则表达式： https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
    3.javascript正则表达式在线测试： https://regex101.com/
    4.javascript代码在线编辑器： https://playcode.io/
    5.httpRequest在线参考： https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
    6.flask在线参考： https://flask.palletsprojects.com/en/1.1.x/quickstart/
