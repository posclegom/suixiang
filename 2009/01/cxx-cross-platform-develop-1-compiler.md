<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++的可移植性和跨平台开发[1]：编译器 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++的可移植性和跨平台开发[1]：编译器</a></h1>
<div class="post-info"><span class="date-header">2009-01-26</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　在跨平台的开发过程中，很多问题都和编译器有关。因此我们先来聊聊编译器相关的问题。<!--program-think--><br /><br />　　★<b>编译器的选择</b><br />　　首先，GCC是优先要考虑支持的，因为几乎所有操作系统平台都有GCC可用。它基本上成了一个通用的编译器了。如果你的代码在A平台的GCC能够编译通过，之后拿到B平台用类似版本的GCC编译，一般也不会有太大问题。因此GCC是肯定要考虑支持的。<br />　　其次，要考虑是否支持本地编译器。所谓本地编译器就是操作系统厂商自产的编译器。例如相对于Windows的本地编译器就是Visual C++。相对于Solaris的本地编译器就是SUN的CC。如果你对性能比较敏感或者想用到某些本地编译器的高级功能，可能就得考虑在支持GCC的同时也支持本地编译器。<br /><br />　　★<b>编译警告</b><br />　　编译器是程序员的朋友，很多潜在的问题（包括可移植性），编译器都是可以发现并给出警告的，如果你平时注意这些警告信息，可以减少很多麻烦。因此我强烈建议：<b>1把编译器的警告级别调高；2不要轻易忽略编译器的警告信息。</b><br /><br />　　★<b>交叉编译器</b><br />　　交叉编译器的定义参见“<a href="http://en.wikipedia.org/wiki/Cross-compiling" target="_blank" rel="nofollow">维基百科</a>”。通俗地说，就是在A平台上编译出运行在B平台上的二进制程序。假设你要开发的应用是运行在Solaris上，但是你手头没有能够运行Solaris的SPARC机器，这时候交叉编译器就可以派上用场了。一般情况下都使用GCC来制作一个交叉编译器，限于篇幅，这里就不深入聊了。有兴趣的同学可以参见“<a href="http://www.nongnu.org/thug/cross..md" target="_blank" rel="nofollow">这里</a>”。<br /><br />　　关于编译器的话题，暂时聊到这，后面聊聊关于“<a href="../../2009/01/cxx-cross-platform-develop-2-language.md">语法</a>”的问题。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2009/01/cxx-cross-platform-develop-1-compiler.md">2009/01/cxx-cross-platform-develop-1-compiler.md</a>
</div>
</div>
</body>
<.md>
