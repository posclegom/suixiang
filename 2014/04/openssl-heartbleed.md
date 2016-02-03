<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>对 OpenSSL 高危漏洞 Heartbleed 的感慨、分析和建议 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">对 OpenSSL 高危漏洞 Heartbleed 的感慨、分析和建议</a></h1>
<div class="post-info"><span class="date-header">2014-04-11</span><a href="../../tags/IT.md" class="tag">IT</a> <a href="../../tags/IT.E4BFA1E681AFE5AE89E585A8.md" class="tag">IT.信息安全</a> </div>
<hr>
<div class="post">
&#12288;&#12288;4月7日曝光的 Heartbleed 漏洞（编号CVE-2014-0160）已经在相关的 IT 领域（尤其是信息安全领域）造成很大的风波。在安全圈混了十多年，不写点啥有些说不过去。所以今天就这个话题，谈谈俺个人的观点，并给普通用户、程序员、开源社区、安全从业人员 分别提点建议。<a name='more'></a><!--program-think--><br /><br /><center><img src="../../images/2014/04/JCDXhWmeg8kJcSWTxfbUxMugX1Ryo1gHdjNiLA-OYO_MVtFAVEs2BBFwi2BlhRhj2bD7UZeEByZZl9YxvL73JdaVEU7wD2pt0KVHlNLlEYIt8hMUV-Bdru0tW5pSPQAs4BC-" alt="不见图 请翻墙"></center><br /><h2>★关于 Heartbleed 漏洞</h2><br />&#12288;&#12288;这个 Heartbleed，直译成中文就是“心脏出血”。听上去挺吓人滴，现实中也确实挺吓人滴。简而言之，这个漏洞足以载入史册。这几天，大伙儿正在经历信息安全历史上的一个重要时刻。或许你应该觉得荣幸 :)<br />&#12288;&#12288;关于这个漏洞的描述，请看中文维基百科的“<a href="https://zh.wikipedia.org/wiki/%E5%BF%83%E8%84%8F%E5%87%BA%E8%A1%80%E6%BC%8F%E6%B4%9E" target="_blank" rel="nofollow">这里</a>”，俺就不浪费口水了。<br /><br /><h2>★先发点感慨</h2><br />&#12288;&#12288;先发一通抱怨。不喜欢听俺抱怨的，请直接略过。<br /><br /><h3>◇安全行业的耻辱</h3><br />&#12288;&#12288;对整个安全行业而言，这是巨大的耻辱。<br />&#12288;&#12288;OpenSSL 是安全行业内应用非常广泛的开源加密库。一个用来保护安全的软件包，本身居然出现如此严重的漏洞（导致内存信息泄漏），实在太讽刺了。<br />&#12288;&#12288;耻辱的还不光是 OpenSSL——就在一个月之前，GnuTLS 同样出现过高危漏洞（编号CVE-2014-0092）。这么短的时间之内，涉及到加密的两个最常用的基础库接连爆出高危漏洞，俺不禁要问：整个安全行业的面子要往哪儿搁？<br /><br /><h3>◇开源社区的耻辱</h3><br />&#12288;&#12288;对整个开源社区而言，这是巨大的耻辱。<br />&#12288;&#12288;OpenSSL 作为非常知名的开源项目之一，这么严重的漏洞居然两年后才曝光（2012年3月的稳定版就已经包含此漏洞）。难道关键模块的代码变更之后不进行【Code Review】？亦或是 Code Review 只是走过场？<br /><br /><h2>★对该漏洞的风险评估</h2><br />&#12288;&#12288;该漏洞曝光前后，风险是不同滴。以下俺分别介绍。<br />&#12288;&#12288;下面会涉及两个术语——“未公开漏洞”和“零日漏洞”——两者的区别请看<a href="../../2010/08/howto-prevent-hacker-attack-4.md">俺之前的博文</a>。<br /><br /><h3>◇漏洞曝光【之前】——作为“未公开漏洞”</h3><br />&#12288;&#12288;目前已经有报道指出，在4月7日之前，这个漏洞就已经被骇客利用（报道在“<a href="http://arstechnica.com/security/2014/04/heartbleed-vulnerability-may-have-been-exploited-months-before-patch/" target="_blank" rel="nofollow">这里</a>”）。另外，圈内也有小道消息流传，说某些攻击者早已拿到此漏洞并加以利用。<br />&#12288;&#12288;在这个阶段，知道漏洞的人很少。这时候，该漏洞属于“宝贵资源”，掌握它的人只会拿来攻击“高价值目标”。所以，如果你只是一个普通网友，或者只是一个小型网站，通常不用担心这个阶段的风险。<br /><br /><h3>◇漏洞曝光【之后】——作为“零日漏洞”</h3><br />&#12288;&#12288;4月7日那天，OpenSSL 发布了公告。发现漏洞的 CloudFlare 公司也发布了公告。于是这个漏洞瞬间传遍全球。几小时之内，大量的攻击工具应运而生（这个漏洞太容易利用了）。然后大量的“脚本小子”（洋文叫 script kiddie）就拿着这些别人写好的工具，对大量的网站进行扫描。<br />&#12288;&#12288;由于时差的关系，以及某些大公司的官僚风气，很多网站来不及在第一时间升级 OpenSSL 这个软件包（这就是所谓的“零日风险”）。估计某些效率低下的公司，甚至到今天都还没升级。<br />&#12288;&#12288;在这个阶段，对于普通网友<br />假设你登录过某个网站<br />假设该网站没有及时升级 OpenSSL<br />假设该网站存储的是【明文密码】 或者 该网站只在【服务端】加密/Hash密码<br />假设在你登录期间正好有人利用该漏洞进行信息收集<br />如果上述几个条件【同时】成立，那么你的密码【有一定的概率】可能被攻击者收集到。<br /><br /><h2>★对该漏洞的技术分析</h2><br />&#12288;&#12288;（本节聊的是该漏洞在技术层面的细节。对 C 语言了解不多的同学，请自行略过，以免浪费时间）<br />&#12288;&#12288;这个漏洞从本质上讲，就是“缓冲区溢出（buffer overflow）”。几乎所有这类漏洞的根源，都是由于程序员的疏忽——对缓冲区涉及的相关“长度”没有仔细检查。<br />&#12288;&#12288;已经有老外写了详细的 Heartbleed 漏洞分析文档（洋文在“<a href="http://blog.existentialize.com/diagnosis-of-the-openssl-heartbleed-bug..md" target="_blank" rel="nofollow">这里</a>”）。对于懒得看长篇的同学，俺把精华摘录如下：<br />&#12288;&#12288;问题出在 OpenSSL 中的 ssl/d1_both.c 文件中的 dtls1_process_heartbeat 函数（看名称就知道该函数是干啥滴）。相关代码有如下（俺补了中文注释）<br /><blockquote style="background-color:#DDD;"><font face="Courier New"><br />int dtls1_process_heartbeat(SSL *s)<br />{          <br />&#12288;&#12288;unsigned char *p = &s->s3->rrec.data[0], *pl;  <span style="color:green;">//p 指向对端发来的心跳数据包</span><br />&#12288;&#12288;unsigned short hbtype;<br />&#12288;&#12288;unsigned int payload;<br />&#12288;&#12288;unsigned int padding = 16; /* Use minimum padding */<br />......<br />&#12288;&#12288;hbtype = *p++;  <span style="color:green;">//心跳数据包的第0个字节，表示心跳包的类型</span><br />&#12288;&#12288;n2s(p, payload);  <span style="color:green;">//接下来2个字节是长度。n2s 是个宏，把这2个字节取出，保存为整型，然后指针移2字节</span><br />&#12288;&#12288;pl = p;  <span style="color:green;">//此时p指向第3个字节——也就是对端提供的心跳包载荷</span><br />......<br />&#12288;&#12288;unsigned char *buffer, *bp;<br />&#12288;&#12288;int r;<br />&#12288;&#12288;buffer = OPENSSL_malloc(1 + 2 + payload + padding);  <span style="color:green;">//根据 payload 分配内存，额外的3字节用于存放类型和长度</span><br />&#12288;&#12288;bp = buffer;<br />......<br />&#12288;&#12288;*bp++ = TLS1_HB_RESPONSE; <span style="color:green;">//填充类型</span><br />&#12288;&#12288;s2n(payload, bp);  <span style="color:green;">//填充长度</span><br />&#12288;&#12288;memcpy(bp, pl, payload);  <span style="color:green;">//填充回应包的载荷【亮点在这里】</span></font></blockquote><br />&#12288;&#12288;如果对端发来的心跳包有猫腻——包长度跟实际载荷不匹配，那么在发送回应包的时候，那句 memcpy 语句就会把心跳包之后的内存区块也一起 copy 进去，然后发给对端。内存信息就泄露了。<br />&#12288;&#12288;搞清楚问题的根源之后，补丁其实很简单——只需加入2个判断语句（寥寥4行代码）。<br /><blockquote style="background-color:#DDD;"><font face="Courier New"><br />if (1 + 2 + 16 > s->s3->rrec.length)<br />&#12288;&#12288;return 0; <span style="color:green;">//忽略长度为 0 的心跳包</span><br />hbtype = *p++;<br />n2s(p, payload);<br />if (1 + 2 + payload + 16 > s->s3->rrec.length)<br />&#12288;&#12288;return 0; <span style="color:green;">//忽略长度与载荷不匹配的心跳包</span><br />pl = p;</font></blockquote><br /><h2>★给普通用户的建议</h2><br />&#12288;&#12288;前面的“风险评估”已经分析了——对于普通网友而言，你的风险主要在于“漏洞曝光之后那1-2天”（也就是“0day”导致的风险）。<br />&#12288;&#12288;从4月7日开始的这几天（尤其是4月8日和4月9日），如果你曾经登录过某个重要的帐号，为了以防万一，改一下密码。国内的很多大网站（包括：电子邮件、电子商务、网银、社交网络、等等）都被发现有 Heartbleed 漏洞。<br />&#12288;&#12288;不过值得庆幸的是，Google 应该没事。根据 OpenSSL 官方的公告（链接在“<a href="http://www.openssl.org/news/secadv_20140407.txt" target="_blank" rel="nofollow">这里</a>”），漏洞的发现者之一 Neel Mehta 是 Google 的人。所以，俺非常确信，Google 的服务器肯定在4月7日之前就解决此问题了。<br /><br /><h2>★给程序员/架构师的建议</h2><br /><h3>◇“多进程”在安全方面的优点</h3><br />&#12288;&#12288;刚开博的头一个季度，俺就发过一篇帖子《<a href="../../2009/02/multi-process-vs-multi-thread.md">架构设计：进程还是线程？是一个问题！</a>》，其中提到了多进程的若干优点。今天再来老调重弹，说说“多进程”在安全方面的优点。<br />&#12288;&#12288;<b>针对“缓冲区溢出”</b><br />&#12288;&#12288;绝大多数的“缓冲区溢出攻击”，都只对当前进程有效。如果你的系统切分成若干个进程，一旦不幸碰上这类攻击，顶多只有一个进程出问题——不至于死得太难看。<br />&#12288;&#12288;不少程序员存在一个误解：以为只有 C/C++ 才会存在缓冲区溢出。其实不然。像 Java/Python 之类的，虽然没有原生的指针，虽然语言的虚拟机/解释器本身对缓冲区越界有严格的检查。但是不要忘了：这些语言的虚拟机/解释器本身也是用 C/C++ 来编写的。说不定虚拟机自己就有问题。<br />&#12288;&#12288;<b>针对“信息泄露”</b><br />&#12288;&#12288;这次的“Heartbleed漏洞”，从技术上讲属于“缓冲区溢出”类型，从逻辑讲属于“信息泄漏”类型。<br />&#12288;&#12288;如果整个系统切分成很多轻量级的进程，每个进程包含的内存信息自然就少了。一旦出现“信息泄漏”的漏洞，损失会小很多。<br />&#12288;&#12288;<b>针对“拒绝服务”</b><br />&#12288;&#12288;多进程除了可以降低上述两类的受伤程度，还可以降低“拒绝服务攻击”导致的受伤程度。<br />&#12288;&#12288;比如某些漏洞通过让“进程崩溃”来起到“拒绝服务”的效果。如果系统的架构是多进程的，并且相关进程具有一定的自我恢复机制，那么就可以降低这类攻击造成的伤害程度。<br /><br /><h3>◇关于密码的“客户端加密/散列”</h3><br />&#12288;&#12288;如今比较成熟的网站，应该不会采用“明文”的方式存储用户密码了。很多程序员/架构师都明白，要把用户密码进行散列（Hash）之后再存储。但是这里面有一个细节，很多人忽略了。那就是：“服务端散列”vs“客户端散列”？<br /><br />&#12288;&#12288;<b>“服务端散列”和“客户端散列”的差异</b><br />&#12288;&#12288;所谓的“服务端散列”就是：用户输入密码之后，以明文的方式传送到服务端，然后在服务端进行散列，散列的结果保存到数据库。<br />&#12288;&#12288;所谓的“客户端散列”就是：用户输入密码之后，现在浏览器这端用 JavaScript 计算散列值，然后把算好的散列值传送到服务端，再保存到数据库。<br /><br />&#12288;&#12288;<b>HTTPS 可能出现的问题</b><br />&#12288;&#12288;到目前为止，大多数网站（包括很多大型网站）还是采用服务端散列。其实捏，“客户端散列”比“服务器散列”的安全性更好。为啥捏？<br />&#12288;&#12288;对于成熟的大型网站，虽然用户登录过程都是基于加密 HTTPS 传输。但是 HTTPS 不是绝对安全的。俺相信 HTTPS 协议本身的设计是很完备的，但是“协议没问题”不等于“整个HTTPS传输没问题”。整个 HTTPS 传输，可能出问题的环节如下：<br />&#12288;&#12288;<b>1. 软件可能出问题</b><br />&#12288;&#12288;比如这次的 Heartbleed 漏洞，就属于典型的“基础软件库出问题”<br />&#12288;&#12288;<b>2. 中间人攻击（比如证书出问题）</b><br />&#12288;&#12288;因为 HTTPS 的加密需要依赖于证书体系。如果证书体系出问题就没戏了。<br />&#12288;&#12288;说两种常见的可能性。<br />可能性之一：某个 CA 的根证书私钥被盗，那么盗用者就可以随意伪造CA证书。真实的案例是 2011年 DigiNotar 被入侵。<br />可能性之二：某个 CA 自己就不检点。最贴切的例子非 CNNIC 莫属。这方面的介绍请参见俺4年前的博文《<a href="../../2010/02/about-cnnic.md">CNNIC 干过的那些破事儿</a>》、《<a href="../../2010/02/remove-cnnic-cert.md">CNNIC 证书的危害及各种清除方法</a>》<br /><br />&#12288;&#12288;<b>“客户端散列”的优点</b><br />&#12288;&#12288;看完上述介绍，你应该明白，这几个环节出问题，都有可能让攻击者收集到传输过程中的【明文】密码。如果密码已经在客户端进行散列，那么风险就降低很多（但不是完全降为零，后面会提到）。<br />&#12288;&#12288;要采用“客户端散列”，有经验的开发人员会对密码进行【撒盐】的散列处理，并且精心选择合适的散列算法（速度足够慢）。如此一来，即使攻击者拿到散列结果，也非常非常难逆向推导出原始的密码。<br /><br />&#12288;&#12288;<b>“客户端散列”的局限性</b><br />&#12288;&#12288;（看到几条读者留言，补充了本小节）<br />&#12288;&#12288;1、“客户端加密/散列”并不能保证绝对的安全（“绝对安全”是不存在滴）。采用“客户端加密/散列”的前提是——页面的JS代码一定采用可信任的方式传输（HTTPS传输）而不能采用明文的 HTTP 传输。因为 HTTP 传输过程，传输内容是可以被篡改的。如果采用 HTTP 明文传输，万一攻击者篡改了客户端的 JS 脚本，还是会导致密码泄漏。<br />&#12288;&#12288;2、HTTPS 通道出现的安全漏洞，大致可以分为两类：一类是攻击者可以窥探到传输内容，但无法修改传输内容（比如这次的 Heartbleed 漏洞属于此类）；还有一类是攻击者可以篡改内容（比如像 CNNIC 这类流氓 CA 就有条件做到这点）。对于前者，骇客无法突破“客户端加密”的防护；对于后者，骇客可以突破。<br /><br /><h2>★给有志于成为黑客的同学的建议</h2><br />&#12288;&#12288;先声明：“黑客”与“骇客”是完全不同的两类人。俺之前发过一篇《<a href="../../2013/01/weekly-share-37.md">每周转载：关于黑客文化和黑客精神</a>》，或许有助于你了解两者的差异。<br />&#12288;&#12288;俺敢跟任何人打赌，OpenSSL 和 GnuTLS 的代码中，类似的低级错误还有好多。而且 GnuTLS 可能比 OpenSSL 还多。有志于成为黑客的同学，可以考虑去分析这俩的代码，找出其中的漏洞。<br />&#12288;&#12288;通过上面那段代码分析，你应该会意识到：这个漏洞本身并没有涉及到多么高深的 C 语法或技巧。那么，发现该漏洞的难点在哪里？俺觉得难在：<br />1. 对整体结构的把握<br />因为 OpenSSL 和 GnuTLS 的代码量还是比较庞大的。很少有人能把握整体的结构。<br />2. 对相关协议的了解<br />想通过看代码分析这两个软件的漏洞，你还需要对相关的协议很熟悉。比如这次的漏洞，就涉及到“心跳协议”的细节。<br />3. 耐心/恒心<br />同时具备上述两条的人本来就不多。然后捏，这些人还未必有足够的耐心去把整个代码（哪怕是其中某个模块的代码）通读一遍。<br />（第三点或许才是最难的）<br /><br />&#12288;&#12288;如果能够搞定上述三点，并且你的运气足够好，那么你有望独立发现一个高危漏洞。<br /><br /><b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br /><a href="../../2014/11/https-ssl-tls-0.md">扫盲 HTTPS 和 SSL/TLS 协议（系列）</a><br /><a href="../../2010/06/howto-prevent-hacker-attack-0.md">如何防止骇客入侵（系列）</a><br /><a href="../../2010/02/about-cnnic.md">CNNIC 干过的那些破事儿</a><br /><a href="../../2010/02/remove-cnnic-cert.md">CNNIC 证书的危害及各种清除方法</a><br /><a href="../../2013/01/weekly-share-37.md">每周转载：关于黑客文化和黑客精神</a><br /><a href="../../2009/02/multi-process-vs-multi-thread.md">架构设计：进程还是线程？是一个问题！</a><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2014/04/openssl-heartbleed.md">2014/04/openssl-heartbleed.md</a>
</div>
</div>
</body>
<.md>