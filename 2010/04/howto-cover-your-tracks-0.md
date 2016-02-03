<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>如何隐藏你的踪迹，避免跨省追捕[0]：为啥要写此文？ - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">如何隐藏你的踪迹，避免跨省追捕[0]：为啥要写此文？</a></h1>
<div class="post-info"><span class="date-header">2010-04-23</span><a href="../../tags/IT.E4BFA1E681AFE5AE89E585A8.md" class="tag">IT.信息安全</a> <a href="../../tags/IT.md" class="tag">IT</a> </div>
<hr>
<div class="post">
<h2>★引子</h2><br />&#12288;&#12288;在早年的安全圈内，也曾有一篇名叫“如何隐藏你的踪迹”的帖子（洋文原名叫“How to cover your tracks”，具体看“<a href="http://freeworld.thc.org/papers/COVER-1.TXT" target="_blank" rel="nofollow">这里</a>”）。那可是国外老牌黑客组织（<a href="http://freeworld.thc.org/" target="_blank" rel="nofollow">The Hacker's Choice</a>）在上个世纪写的。不过那篇帖子有很大篇幅是在教你：如何在入侵系统之后，不留下痕迹。而今天俺要聊的内容，基本和入侵无关。<!--program-think--><br /><br />&#12288;&#12288;<b>本系列的主题是</b>：<br />&#12288;&#12288;如何从各个层面，防止真实身份的暴露？<br />&#12288;&#12288;<b>本系列的受众是</b>：<br />&#12288;&#12288;那些通过互联网进行各种【政治敏感活动】的网友，包括但不限于：异议人士、民运人士、维权人士......不过捏，凡事都有两面性。某些通过网络干坏事的家伙，或许也能从本系列博文中获得启发（技术总是双刃剑，这也是没办法的）<br />&#12288;&#12288;<b>本系列的意义是</b>：<br />请参见博文《<a href="../../2015/08/Technology-and-Freedom.md">“对抗专制、捍卫自由”的 N 种技术力量</a>》<br /><br /><h2>★为啥要写此文？</h2><br />&#12288;&#12288;从最近2年的趋势来看，互联网越来越成为揭露社会阴暗面、批评党的一个利器。因此，党国为了维护统治阶级的利益，也会想方设法扼杀对党不利的言论（具体如何扼杀，可以参见“<a href="../../2009/07/party-pk-internet.md">党和互联网的较量</a>”）。在党国采取的各种措施中，就包括“跨省追捕”这一招。（“跨省追捕”一词来源于09年轰动一时的“<a href="http://zh.wikipedia.org/wiki/%E7%8E%8B%E5%B8%85%E5%8F%91%E8%B4%B4%E4%BA%8B%E4%BB%B6" target="_blank" rel="nofollow">王帅发帖事件</a>”）<br />&#12288;&#12288;俺发觉很多网友非常缺乏这方面的技术常识，这可真是大大便宜了党国的爪牙。另外，近来也有好些个读者来信询问这方面的知识。看来这个扫盲帖还是很有必要滴。所以，今天就开始抽空写一个系列。<br /><br /><h2>★免责声明</h2><br />&#12288;&#12288;为了免遭别人拍砖，省却不必要的麻烦，在介绍正式内容前，先来个免责声明：<br />免责声明一：本系列仅介绍各种保护隐匿性的技术手段及注意事项，并【不】意味着俺鼓励大伙儿去干坏事。<br />免责声明二：本系列介绍的招数，可以大大降低暴露的可能性，但是并【不能确保】百分百不暴露。（要知道，绝对的安全是不存在滴）如果你用了这些招数，还是暴露了，那可别怨俺 :)<br /><br /><h2>★本系列的目录</h2><a name="index"> </a><br /><br />为了方便阅读，把本系列帖子的目录整理如下（需翻墙）：<br />1. <a href="../../2010/04/howto-cover-your-tracks-1.md">网络层面的防范</a><br />2. <a href="../../2010/04/howto-cover-your-tracks-2.md">个人软件的防范</a><br />3. <a href="../../2010/05/howto-cover-your-tracks-3.md">操作系统的防范</a><br />4. <a href="../../2012/02/howto-cover-your-tracks-4.md">通讯工具的防范</a><br />5. <a href="../../2012/03/howto-cover-your-tracks-5.md">用多重代理隐匿公网IP</a><br />6. <a href="../../2013/01/howto-cover-your-tracks-6.md">用虚拟机隐匿公网IP（原理介绍）</a><br />7. <a href="../../2013/01/howto-cover-your-tracks-7.md">用虚拟机隐匿公网IP（配置图解）</a><br />8. <a href="../../2015/04/howto-cover-your-tracks-8.md">如何搭配“多重代理”和“多虚拟机”</a><br />9. （未完待续）<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2010/04/howto-cover-your-tracks-0.md">2010/04/howto-cover-your-tracks-0.md</a>
</div>
</div>
</body>
<.md>
