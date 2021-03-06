<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>2015年1月翻墙快报 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">2015年1月翻墙快报</a></h1>
<div class="post-info"><span class="date-header">2015-01-06</span><a href="../../tags/IT.md" class="tag">IT</a> <a href="../../tags/IT.E7BFBBE5A299.md" class="tag">IT.翻墙</a> </div>
<hr>
<div class="post">
<h2>★近期翻墙动态</h2><br />&#12288;&#12288;12月27日，<a href="../../2014/12/weekly-share-78.md">GFW 刚刚封了 Gmail</a> 的客户端通道（POP3/SMTP/IMAP）。紧接着到了元旦，GFW 又加强了封锁，显著的至少影响包括：<br />VPN gate 很难找到能连通的 server（在这之前，VPNgate 如果走 UDP 协议，还是能找到可用的 Server；现在貌似连 UDP 方式也很难连接）<br />自由门最近的几个版本都失效（7.4.2、7.5.0、7.5.2）<br /><a name='more'></a><!--program-think--><br /><br />&#12288;&#12288;有些同学或许会纳闷——VPN gate 的 Server 那么多，而且是动态变化的，GFW 如何封杀？<br />&#12288;&#12288;其实俺在2013年的<a href="../../2013/01/gfw-news.md">某篇《翻墙快报》</a>中有提及——GFW 开始采用“基于行为特征的检测技术”，以此来封锁 VPN 和 SSH——估计 GFW 封锁 VPN gate，用的就是这类招数。<br /><br /><h2>★还有哪些翻墙工具可用？</h2><br />&#12288;&#12288;经读者反馈以及俺本人测试，【至少】有如下几款工具还是可用滴。<br />赛风3（俺测试的是目前最新的 3.81 版本，旧版本未测试）<br />无界（必须是版本14.05，或更高）<br />TOR+meek（从 TOR Browser 4.0 之后开始内置 meek，扫盲教程在“<a href="../../2014/10/gfw-tor-meek.md">这里</a>”）<br />I2P（俺测试的是目前最新的 I2P 0.9.17 版本，稍微旧一点的版本，应该也能用）<br /><br />&#12288;&#12288;上述这几款，I2P 的速度比较慢，建议只留作备份（当其它工具都失效之后，用 I2P 救急）。提醒一下：你拿到 I2P 之后，先要让它补种（reseed）并运行一段时间。至于如何补种，俺的教程有介绍（参见《<a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a>》）。<br />&#12288;&#12288;因为本人的时间/精力有限，只测试上述几款。或许还有其它翻墙工具依然可用，大伙儿可以到博客评论中补充。<br /><br />&#12288;&#12288;本文发出后，某读者在评论中反馈说：世界通（GPass）的 Skype 通道依然可用。<br /><br /><h2>★不会翻墙的同学，如何获取？</h2><br />&#12288;&#12288;建议先用【国外】邮箱获取赛风3——很简单，只需往赛风官网提供的邮箱<b> get@psiphon3.com </b>发送任意邮件，即可收到自动回复。<br />&#12288;&#12288;拿到赛风之后，再用赛风下载其它几个翻墙工具。上面列举的这些工具，俺博客都有教程（链接在本文末尾）。每个教程中都列出了该工具的官网网址。<br />&#12288;&#12288;<b>由于近期 GFW 加强封锁，大伙儿手头要同时配备几款不同的翻墙工具，以防不测。</b><br /><br /><h2>★几项跟“翻墙”有关的通知</h2><br /><h3>◇俺博客开通了【免翻墙】镜像</h3><br />&#12288;&#12288;（此事之前已经说过，今天再唠叨一次）<br />&#12288;&#12288;此镜像由 Greatfire 友情赞助（Greatfire 是专门对抗 GFW 的组织）。<br />&#12288;&#12288;因为要防范 GFW 的封杀，镜像的域名是动态变化的。你可以到 <b><a href="https://github.com/greatfire/wiki/" target="_blank" rel="nofollow">https://github.com/greatfire/wiki/</a></b> 查看镜像的网址。该页面上，除了俺博客的镜像，还有其它一些知名网站的镜像。<br /><br /><h3>◇ help_gfw@yahoo.com 已失效</h3><br />&#12288;&#12288;其实半年前就失效了，一直忘了跟大伙儿说。<br />&#12288;&#12288;原先俺登录到该邮箱，配置界面中有一个“自动回复”的选项。大约从2014年2季度开始，这个选项就没了。不知为何？<br />&#12288;&#12288;从那之后，俺原先设置好的“自动回复功能”，也跟着消失了。<br />&#12288;&#12288;（俺这个雅虎邮箱是国际域名，不是 cn 域名。2013年阿里巴巴关闭雅虎中国的邮箱，俺这个邮箱【没有】受影响）<br /><br /><h3>◇关于 TOR 的 meek</h3><br />&#12288;&#12288;有些读者反馈说：使用 TOR 的 meek 插件之后，又在 TOR 的配置文件中屏蔽某些国家的节点。屏蔽之后，meek 就没法联网了。<br />&#12288;&#12288;针对这种情况，俺在《<a href="../../2014/10/gfw-tor-meek.md">“如何翻墙”系列：TOR 已复活——meek 流量混淆插件的安装、优化、原理</a>》一文的末尾补充了一个“疑难解答”章节，介绍这个问题如何搞定。<br /><br /><h2>★相关翻墙教程</h2><br />&#12288;&#12288;下面这些教程都在俺博客上（需翻墙）。<br />&#12288;&#12288;从2014年4月开始，俺博客会定期提供打包下载（电子书形式），请看“<a href="../../2014/04/blog-ebook.md">这篇博文</a>”。<b>一旦你能够翻墙，强烈建议先把俺博客的打包电子书下载到自己硬盘上。一旦今后无法翻墙，至少手头还有一些翻墙教程可以参考。</b><br /><br /><h3>◇基础教程</h3><br /><a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>（传说中的全方位扫盲教程，定期更新）<br /><a href="../../2011/03/how-to-get-gfw-tools.md">获取翻墙软件方法大全</a>（教你在无法翻墙的情况下拿到翻墙软件）<br /><a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何共享翻墙通道</a><br /><br /><h3>◇各种翻墙软件使用教程</h3><br /><a href="../../2014/10/gfw-tor-meek.md">“如何翻墙”系列：TOR 已复活——meek 流量混淆插件的安装、优化、原理</a><br /><a href="../../2013/11/tor-faq.md">关于 TOR 的常见问题解答</a><br /><a href="../../2011/10/gfw-psiphon.md">双管齐下的赛风3</a><br /><a href="../../2011/12/gfw-wujie.md">新版本无界——赛风3失效后的另一个选择</a><br /><a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a><br /><a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a><br /><a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a><br /><a href="../../2013/04/gfw-vpngate.md">扫盲 VPN Gate——分布式的 VPN 服务器</a><br /><a href="../../2010/03/choose-free-gate.md">自由門——TOR 被封之后的另一个选择</a><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2015/01/gfw-news.md">2015/01/gfw-news.md</a>
</div>
</div>
</body>
<.md>
