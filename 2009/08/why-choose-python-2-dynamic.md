<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>为什么俺推荐Python[2]：作为动态语言的Python - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">为什么俺推荐Python[2]：作为动态语言的Python</a></h1>
<div class="post-info"><span class="date-header">2009-08-21</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.Python.md" class="tag">编程.Python</a> </div>
<hr>
<div class="post">
<a href="../../2009/08/why-choose-python-1-script.md" target="_blank">上次的帖子</a>介绍了脚本语言的优缺点，然后又拿Python和其它脚本语言PK了一下。今天主要是忽悠一下动态语言，捎带忽悠一下Python。如果你看完本贴，觉得动态语言不错，那俺建议你从Python开始入手。<!--program-think--><br /><br /><h2>★动态语言扫盲</h2><br />　　考虑到还有很多同学对动态语言了解不深入，有必要先来普及一下它的基本常识。已经了解的同学，请略过本节。<br />　　通俗地说：能够在运行时修改自身程序结构的语言，就属于动态语言。那怎样才算是“运行时修改自身程序结构”捏？比如下面这几个例子都 算：在<b>运行时</b>给某个类增加成员函数及成员变量；在<b>运行时</b>改变某个类的父类；在<b>运行时</b>创建出某个函数......<br />　　从这些例子，你应该对动态语言有一个初步的感觉了吧？毕竟传统的静态语言（比如C、C++、Java），是很难达到这些效果滴。<br />　　另外，有个误区需要澄清一下。很多同学以为脚本语言也就是动态语言。其实两者是<b>不等价</b>滴——虽然两者有很大的交集。比如C#在4.0之后，就可以算是动态语言了，但它不能算是脚本语言；另外，有很多Shell脚本语言（比如DOS & Windows下的bat），不能算是动态语言。<br />　　关于动态语言更深入的介绍，大伙儿可以看“<a href="http://en.wikipedia.org/wiki/Dynamic_programming_language" target="_blank" rel="nofollow">这里</a>”。<br /><br /><h2>★为啥要学习动态语言？</h2><br />　　扫盲之后，就该来说一下，学习动态语言的动机了。搞明白动机，学起来才有干劲嘛 <b>:-)</b><br /><br /><h3>◇顺应大趋势</h3><br />　　假如你经常关注<a href="http://www.tiobe.com/content/paperinfo/tpci/" target="_blank" rel="nofollow">TIOBE</a>的排名，那你应该能察觉出来，动态语言近两年的发展势头比较迅猛（在Top10里面，至少占了半壁江山）。这能从某个侧面反映出动态语言的影响力在扩大。<br />　　假使你不相信<a href="http://www.tiobe.com/content/paperinfo/tpci/" target="_blank" rel="nofollow">TIOBE</a>的排名，俺再举一个例子。两大开发阵营（Java和dotNet）最近几年也加大了对动态语言的支持力度。比如，dotNet的CLR加入了对<a href="http://en.wikipedia.org/wiki/IronPython" target="_blank" rel="nofollow">IronPython</a>和<a href="http://en.wikipedia.org/wiki/IronRuby" target="_blank" rel="nofollow">IronRuby</a>的支持；Sun当然也不甘示弱，JVM也开始支持<a href="http://en.wikipedia.org/wiki/Groovy_%28programming_language%29" target="_blank" rel="nofollow">Groovy</a>，<a href="http://en.wikipedia.org/wiki/JRuby" target="_blank" rel="nofollow">JRuby</a>等语言。<br />　　俺费了这许多口水，列位看官应该明白动态语言是大势所趋吧。在这动态语言大行其道的日子里，你如果连一门动态语言都没搞懂，那出门都不好意思跟人打招呼。<br />　　不过，话又说回来，静态语言也是不会消亡滴。毕竟，静态语言有自己的优势（比如严谨、性能）。长期来说，必定是动态语言和静态语言并存。各自弥补对方的缺点。<br /><br /><h3>◇了解新思维、新理念</h3><br />　　学习一门动态语言还有一个好处：。有很多时候，多学习一门语言，并不一定是为了在工作中用它，而是为了学习新的思维方式、体会新的理念。比如俺就曾经花时间去看<a href="http://en.wikipedia.org/wiki/Prolog" target="_blank" rel="nofollow">Prolog</a>，但是俺在工作中，从来不需要用到它。（以后有空的话，俺会介绍一下这玩意儿）<br />　　由于动态语言可以在运行时修改自身结构，因此就会产生很多静态语言所没有编程范式和手法（比如<a href="http://en.wikipedia.org/wiki/Eval" target="_blank" rel="nofollow">eval</a>、<a href="http://en.wikipedia.org/wiki/Mixin" target="_blank" rel="nofollow">Mixin</a>，后面会顺带介绍这两个玩意儿）。如果你以前只使用静态语言，那你在学习了动态语言之后，多半会从它身上领略到很多新的思想和理念。<br /><br /><h3>◇能够化繁为简</h3><br />　　可能有些同学觉得，前面说的都有些务虚，那咱再来说点具体实在的。大牛<a href="http://en.wikipedia.org/wiki/Edsger_W._Dijkstra" target="_blank" rel="nofollow">Edsger Dijkstra</a>（图灵奖得主）曾经说过：“编程的艺术就是处理复杂性的艺术。”咱们来看看，动态语言是如何处理复杂问题滴。<br />　　假设要你实现一个函数，用来完成两个数的<b>某种</b>运算，具体的运算类型作为函数的参数传入，然后该函数返回运算结果。比如：<br /><font face="Courier New"><br />　　Foo("+", 2, 4)　返回 6<br />　　Foo("*", 2, 2)　返回 4<br /></font><br />　　对于上述需求，你会如何实现捏？<br />　　请先暗自盘算1分钟，然后再往下看。<br /><br />　　．．．．．．<br />　　Ｔｈｉｎｋｉｎｇ<br />　　．．．．．．<br /><br />　　如果你用静态语言（比如C、C++、Java）来实现，你可能会在函数内使用一个switch，根据不同的运算符，进行计算，然后返回计算结果。<br />　　对于某些比较ＯＯ的语言（例如C++、Java），你或许还会抽象出一个运算的接口类（纯虚类），然后分别派生出若干个不同的计算类（比如加法类、乘法类），看起来似乎比switch要优雅一些。<br />　　当然，用静态语言还有其它一些玩法，但是代码量都不会少。具体详情可以看很早以前的一个老故事：<a href="http://www.cnblogs.com/linkcd/archive/2005/07/19/196087..md" target="_blank" rel="nofollow">4个程序员的一天</a>。（其实俺这个例子的灵感就是从那个老故事剽窃滴）<br />　　现在，咱们来看看Python是如何实现该需求滴。用Python只需要<b>两行</b>代码即可。请看：<br /><pre><font face="Courier New"><br />def Foo(op, n1, n2) :<br />    return eval( "%d %s %d" % (n1, op, n2) )<br /></font></pre><br />　　不懂Python的同学可能要问了，这两行代码是啥子意思呀？<br />　　其实，第一行代码只不过是定义了一个函数头，第2行代码才是精华。这里面利用了动态语言常见的<b>eval</b>手法（具体参见“<a href="http://en.wikipedia.org/wiki/Eval" target="_blank" rel="nofollow">这里</a>”）。在python里面，内置的<b>eval</b>函数可以把某个字符串当成一个表达式，并对其求值。而语句 <font face="Courier New"><u>"%d %s %d" % (n1, op, n2)</u></font> 只不过格式化出一个表达式的字符串。<br />　　顺便再插一句，Python还有一个<b>exec</b>的内置函数，可以把一段Python源代码作为字符串参数传递给它，让该函数去执行。两个函数结合起来，就能玩出很多花样。具体的花样可以参见“<a href="../../2009/08/examples-of-eval.md" target="_blank">这里</a>”<br /><br /><h2>★为什么是Python？</h2><br />　　说了动态语言的种种好话，有同学会问了，动态语言有很多种，为啥非要学习Python捏？<br />　　首先，俺在<a href="../../2009/08/why-choose-python-0-overview.md">本系列</a>的<a href="../../2009/08/why-choose-python-1-script.md" target="_blank">上一个帖子</a>，已经对比过Python和另外几种脚本语言。那几种脚本语言正好也是知名的动态语言。Python相对于他们的优势，此处就不再重复啰嗦了。<br />　　其次，单就语法本身而言，Python的语法对动态性的支持是很优雅、很简洁滴。通过刚才那个<b>eval</b>小例子，大伙应该已经看出来了。为了更形象一点，咱拿前面提到的<a href="http://en.wikipedia.org/wiki/Mixin" target="_blank" rel="nofollow">Mixin</a>来Show一下Python的语法是如何的简洁。<br />　　通俗地说，<b>Mixin</b>手法需要在<b>运行时</b>给某个类增加基类（也就是父类）。对于Python而言，每一个类都有一个内置属性“__bases__”，里面包含这个类<b>当前</b>的所有基类。假如要在<b>运行时</b>增加基类，操作“__bases__”这个属性即可。<br />　　比如有一个类A和类B。如果要在运行时把B加为A的父类，可以用如下语句：<br /><font face="Courier New">A.__bases__ += (B, )</font><br />　　是不是也很简洁，而且可读性也不差？相比而言，有些动态语言（比如JavaScript），要实现类似的效果，代码就相对复杂了。<br />　　由于Mixin不是今天的重点，就不再深入展开了。<br /><br />　　最后，来个总结发言：如果你之前没有接触过动态语言，建议去学习一下；如果你已经打定主意要学，Python是比较好的候选者。<br />　　好了，今天就聊到这里。<a href="../../2010/08/why-choose-python-3-oop.md">下一个帖子</a>，咱们来讲讲Python作为一个纯粹的面向对象语言，有些啥特色。<br /><br /><a href="../../2009/08/why-choose-python-0-overview.md#index">回到本系列的目录</a><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2009/08/why-choose-python-2-dynamic.md">2009/08/why-choose-python-2-dynamic.md</a>
</div>
</div>
</body>
<.md>