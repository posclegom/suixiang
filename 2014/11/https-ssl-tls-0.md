<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>扫盲 HTTPS 和 SSL/TLS 协议[0]：引子 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">扫盲 HTTPS 和 SSL/TLS 协议[0]：引子</a></h1>
<div class="post-info"><span class="date-header">2014-11-08</span><a href="../../tags/IT.md" class="tag">IT</a> <a href="../../tags/IT.E4BFA1E681AFE5AE89E585A8.md" class="tag">IT.信息安全</a> </div>
<hr>
<div class="post">
<img src="../../images/2014/11/H_exzSD20W99qSJhGkLJFPwj3gU7VF_t9VGsbHS19Zkky6Vgrhcn8OG4c3--8-qr3DjL-H6lOQVfYcYEZ5qQp19yOycAvaL-Dnl29AqINsIhWK6ITliRP_tBL4nZ4z_Vw0IO" alt="不见图 请翻墙"><br />&#12288;&#12288;今天这篇算是补之前的欠债——俺在4年前写过几篇关于 CA 证书的扫盲（“<a href="../../2010/02/introduce-digital-certificate-and-ca.md">这里</a>”和“<a href="../../2010/02/remove-cnnic-cert.md">这里</a>”），之后有不止一位热心读者建议俺写一篇关于 HTTPS 的扫盲。因为俺比较懒，当时没动笔，拖了2-3年，都有点忘了。正好今年出了两个跟 HTTPS 相关的高危漏洞（<a href="https://en.wikipedia.org/wiki/Heartbleed" target="_blank" rel="nofollow">Heartbleed</a> 和 <a href="https://en.wikipedia.org/wiki/POODLE" target="_blank" rel="nofollow">PODDLE</a>），于是俺又想起这事儿。<br />&#12288;&#12288;本来想单独写一篇。等写完“背景知识”这一章节，发现篇幅已经很长了。所以就再开一个系列吧。<a name='more'></a><!--program-think--><br />&#12288;&#12288;事先声明：<br />&#12288;&#12288;既然叫做“扫盲”，所以俺不会讲太具体的“技术实现细节”（当然，更不会去讲“代码实现”）。本系列侧重于：尽可能通俗地介绍“设计思路”、“实现原理”，最后再聊聊“针对 HTTPS 的攻击手法”和“相关的安全防范措施”。初步计划写3-4篇。<br />&#12288;&#12288;虽然是扫盲，或许也能让 IT 技术人员从中获益——因为俺发现：连安全行业的某些程序员，对 HTTPS 的原理也所知甚少。<br /><br />为了方便阅读，把本系列帖子的目录整理如下（需翻墙）：<a name="index"> </a><br />1. <a href="../../2014/11/https-ssl-tls-1.md">背景知识、协议的需求、设计的难点</a><br />2. <a href="../../2014/11/https-ssl-tls-2.md">可靠密钥交换的原理</a><br />3. SSL/TLS 协议的实现<br />4. 针对 HTTPS 的各种攻击手法<br />5. 各种相应的防范措施<br /><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2014/11/https-ssl-tls-0.md">2014/11/https-ssl-tls-0.md</a>
</div>
</div>
</body>
<.md>
