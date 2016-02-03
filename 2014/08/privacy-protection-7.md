<!DOCTYPE.md>
.md xmlns="http://www.w3.org/1999/..md" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text.md; charset=utf-8" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>如何保护隐私[7]：其它桌面软件的隐私问题 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">如何保护隐私[7]：其它桌面软件的隐私问题</a></h1>
<div class="post-info"><span class="date-header">2014-08-15</span><a href="../../tags/IT.md" class="tag">IT</a> <a href="../../tags/IT.E4BFA1E681AFE5AE89E585A8.md" class="tag">IT.信息安全</a> </div>
<hr>
<div class="post">
&#12288;&#12288;<b>插播一个广而告之：</b><br />&#12288;&#12288;最近连续好几天，俺分享电子书的“Dropbox 网盘”总显示【共享网址流量耗尽】（This account's public links are generating too much traffic and have been temporarily disabled! ）。如果你碰到此问题，请改道“微软网盘”下载。所谓的“流量耗尽”是因为：Dropbox 对【免费帐号】的共享网址，限制了每天的下载流量（大约每天几个GB）。<br />&#12288;&#12288;以前这种现象也出现过，但从来没有连续发生这么多天。有两种可能：<br />可能性1：俺分享的电子书越来越多了，而且读者也越来越多了。所以就更加容易出现“流量耗尽”<br />可能性2：有人（比如朝廷走狗）来捣乱，通过重复下载大文件，人为制造“流量耗尽”（在安全行业中，这称之为“拒绝服务攻击”）<br />&#12288;&#12288;至于是哪一种情况，俺暂时还不清楚，需要再多观察几日再说。<br /><hr><br />&#12288;&#12288;前几天又有热心读者来催促，让俺尽快把以前挖的“坑”填平。今天来继续补充<a href="../../2013/06/privacy-protection-0.md">《如何保护隐私》系列</a>。在本系列之前的部分，俺已经花了5篇帖子，大谈特谈【浏览器】相关的隐私问题。接下来要聊聊其它桌面软件的隐私问题。<br />&#12288;&#12288;为了避免歧义，先声明一下：本文所说的“桌面软件”泛指各种“PC 端软件”。至于移动设备（手机、平板）的隐私问题，会在本系列的后续博文中另外介绍。<a name='more'></a><!--program-think--><br /><br /><h2>★安全类</h2><br />&#12288;&#12288;在安全界混过的人或许明白一个道理——不靠谱的安全软件反而更危险。所以俺首先来介绍一下安全软件导致的隐私问题。<br /><br /><h3>◇利用“扫描硬盘”收集隐私</h3><br />&#12288;&#12288;安全软件如果要查杀病毒/木马，通常需要先扫描硬盘文件。如果某款安全软件不靠谱，那么它在扫描硬盘的过程中，就会悄悄滴收集你硬盘上有价值的个人资料。而且这类安全软件通常都需要定期升级“病毒特征库”或“木马特征库”。要升级特征库必然要联网（连接到厂商的服务器）。如此一来，这类不靠谱的安全软件就可以利用升级的时机，把收集到的用户信息发送到厂商服务器上。整个过程可谓是神不知鬼不觉啊。<br /><br />&#12288;&#12288;举例1：<br />&#12288;&#12288;还记得前几年的“3Q 大战”吗？当时的导火索之一就是 QQ 存在隐私问题——据说 QQ 软件会偷偷地扫描硬盘。后来腾讯官方也承认了这点，但是又辩解说这是“QQ 电脑管家”在进行安全检查。不过懂行的网友分析了“QQ 电脑管家”的行为，发现它扫描硬盘的过程更像是在收集用户信息，而不像是查杀病毒/木马。具体参见“<a href="http://www.chinagfw.org/2010/01/windows7qq..md" target="_blank" rel="nofollow">这篇</a>”和“<a href="http://www.chinagfw.org/2010/05/qq_28..md" target="_blank" rel="nofollow">这篇</a>”。<br /><br />&#12288;&#12288;举例2：<br />&#12288;&#12288;在《<a href="http://www.nbd.com.cn/articles/2013-02-26/716855..md" target="_blank" rel="nofollow">360黑匣子之谜——奇虎360“癌”性基因大揭秘 @ 每日财经新闻</a>》一文中，提及了奇虎是如何利用“360”这款所谓的“安全工具”来收集用户隐私。<br /><br /><h3>◇利用“网络监控”收集隐私</h3><br />&#12288;&#12288;除了查杀病毒/木马需要扫描硬盘，某些安全软件还需要进行流量监控，以此来防范网页挂马。如果某个安全软件不靠谱，那么它可以利用“网络流量监控”的机会，收集你的上网行为（比如你常看的网站）。收集好信息之后，同样可以利用升级特征库的机会，把用户隐私发送到厂商的服务器上。<br /><br /><h3>◇其它收集隐私的手段</h3><br />&#12288;&#12288;除了上述这两招，安全厂商还有其它一些手段来收集用户隐私。<br />&#12288;&#12288;比如奇虎大力推广的“360安全浏览器”。这款浏览器会把“用户访问的网址、网址对应的 cookie、用户在地址栏输入的内容”等信息上传到奇虎的服务器上。具体的报道请看《<a href="http://tech.sina.com.cn/i/2012-11-23/08517825584...md" target="_blank" rel="nofollow">中科院报告：360产品存在三大隐私安全问题 @ 新浪科技</a>》。说到这里，俺顺便感叹一下：奇虎/360 的老板周鸿祎，当年就是做流氓软件起家的（老网友应该还记得臭名昭著的“3721插件”）。如今已经过了10多年了，这厮真是“狗改不了吃屎”啊。<br />&#12288;&#12288;说到浏览器，再次罗嗦一下：<br />其一，千万别用【国产的】浏览器<br />其二，全球三大桌面浏览器，在隐私保护方面的排序是：Firefox 优于 Chrome/Chromium 优于 IE<br />（Chrome/Chromium 的粉丝如果不服，可以看本系列“<a href="../../2013/06/privacy-protection-2.md">第2篇博文</a>”的分析）<br /><br /><h3>◇国产安全软件有靠谱的吗？</h3><br />&#12288;&#12288;对这个问题，俺倾向于【否定】的回答。虽然俺无法拿出确凿证据来证明“每一款国产安全软件都有问题”，但是俺可以给出如下一些分析供参考。<br />&#12288;&#12288;刚才提到过，在安全软件中植入后门具有某种天生的优势——其一，杀毒软件或木马查杀软件天生就需要扫描硬盘；其二，杀毒软件或木马查杀软件天生就需要定期升级特征库（在线升级就需要联网）。于是乎，假如某款国产的杀毒软件或木马查杀软件达到【足够大】的装机量，通常会受到朝廷“有关部门”的青睐。对于国产软件公司而言，如果“有关部门”找你谈话，要求你在软件中植入后门，你有胆量拒绝吗？显然没有。<br />&#12288;&#12288;某些读者可能会反问说——那美国的杀毒软件（比如赛门铁克、迈克菲）也可能有 NSA（美国国安局）的后门啊。这类猜测是有道理滴。但是俺要提醒一下：本博客的大部分读者都是大陆网民，<b>美国国安局对你是没有“司法管辖权”滴</b>。所以就算美国的安全软件有 NSA 的后门，其危险性【远小于】咱们党国的后门。再退一步讲，假设你对隐私性的要求非常高，容不得一丁点后门，那俺的建议是：干脆放弃 Windows，改用 Linux（如此一来，也就无需杀毒软件了）。没用过 Linux 的同学可以看俺之前写的扫盲教程《<a href="../../2013/10/linux-newbie-guide.md">新手如何搞定 Linux 操作系统？</a>》。<br /><br /><h2>★文字输入类</h2><br />&#12288;&#12288;为啥俺把“输入法”排在第二项捏？首先是输入法非常普及（几乎每个天朝网民都会装）；其次是输入法可以暴露你本人的很多信息，从而导致比较严重的隐私问题。<br /><br /><h3>◇敏感词监控</h3><br />&#12288;&#12288;跟安全软件类似，那些装机量巨大的输入法，对朝廷是很有吸引力滴。如果能通过这些输入法监控网民的文字输入，就可以发现潜在的“不和谐分子”。这种风险可不是俺瞎编出来吓唬大家滴。不信请看如下的举例。<br /><br />&#12288;&#12288;举例：<br />&#12288;&#12288;《<a href="http://internet.solidot.org/article.pl?sid=08/03/24/0624233" target="_blank" rel="nofollow">国产软件的隐私问题 @ Solidot</a>》，其中提到了：<q style="background-color:#DDD;">拼音加加2004v3.02，新华五笔，这两个软件已经发现有后门和<b>敏感词汇汇报功能</b>的存在，会在不知不觉中泄漏隐私。</q>请注意俺标了粗体的“敏感词汇汇报功能”。这类功能很显然是为朝廷量身定做滴。<br />&#12288;&#12288;虽然这篇报道只提到了“拼音加加、新华五笔”这两款，但这【不】表示其它输入法就【没有】问题——可能只是尚未发现而已。<br /><br /><h3>◇个性化词库同步</h3><br />&#12288;&#12288;“词库同步功能”，大伙儿应该不陌生吧？目前主流的输入法都会根据输入频率存储用户的“个性化词库”。“个性化词库”是为了提高输入效率的——比如当你的输入出现二义性，你经常选中的那个候选词会出现在靠前的位置。<br />&#12288;&#12288;所谓的“词库同步功能”，就是把你本机的个性化词库同步到云端。这个功能对那些拥有多台电脑的网友而言，是有帮助滴。但是这也带来了隐私的风险。因为个性化词库存储在云端，那么该输入法厂商就可以对你的“个性化词库”进行分析，从而了解你本人的种种信息。假如说你经常用输入法进行网络聊天、撰写邮件、写文章、等等，那么你的个性化词库包含的信息量就非常非常大。<br />&#12288;&#12288;而且俺有充分的理由相信，朝廷六扇门的人肯定会去分析存储在云端的“用户个性化词库”。<br /><br /><h3>◇“服务器泄露”导致的隐私问题</h3><br />&#12288;&#12288;比如很有名的“搜狗输入法”就在去年（2013）曝出高危漏洞，具体参见《<a href="http://www.solidot.org/story?sid=35033" target="_blank" rel="nofollow">搜狗输入法收集用户隐私信息，未屏蔽爬虫 @ Solidot</a>》一文。据说该漏洞曝光了很长时间（超过1个月）才修复。在这段时间内，别有用心的骇客可以利用这个漏洞，收集到搜狗输入法用户的大量聊天内容（尤其利用它输入的图片网址）。<br /><br /><h2>★即时通信类</h2><br />&#12288;&#12288;考虑到 QQ 是天朝即时通信（以下简称“IM”）的老大，下面以 QQ 为主介绍一下 IM 导致的隐私问题。关于 QQ 扫描硬盘的问题，前面已经提到了，所以本章节聊聊另外的几个问题。<br /><br /><h3>◇敏感词监控</h3><br />&#12288;&#12288;刚才介绍“输入法”的隐私问题，其中之一是“敏感词监控”。对于 IM 而言，同样也存在“敏感词监控”的问题，道理跟“输入法”一样。像 QQ 这种用户量如此巨大的软件，朝廷肯定不会放过滴。所以 QQ 系统中早就安插了朝廷方面的监控工具（据说是部署在腾讯的服务器上）。如果你在 QQ 聊天过程中频繁涉及到一些敏感的政治词汇，就会引起六扇门的注意。相关报道如下：<br />《<a href="http://tech.163.com/05/0728/10/1POADRE500091589..md" target="_blank" rel="nofollow">QQ 是如何监视你的聊天记录的 @ 网易科技</a>》<br />&#12288;&#12288;不光是 QQ，其它一些 IM 工具也存在敏感词监控的问题。比如臭名昭著的“TOM 版 Skype”。该版本完全是针对天朝的国情进行定制，内置了庞大的“敏感词词库”。一旦用户在聊天时输入了词库中的某个敏感词，相关的聊天内容和聊天帐号会被记录在 TOM 的服务器上。外媒的报道如下：<br />《<a href="http://chinese.wsj.com/gb/20081002/tec142111.asp?source=NewSearch" target="_blank" rel="nofollow">Skype 中国合资企业监控用户网络行为 @ 华尔街日报</a>》<br />《<a href="http://news.bbc.co.uk/chinese/simp/hi/newsid_7640000/newsid_7649400/7649459.stm" target="_blank" rel="nofollow">Skype 中国合作伙伴“监控用户” @ BBC</a>》<br />&#12288;&#12288;说到“TOM 版 Skype”，顺便提一下：TOM 跟 Skype 的合作已经在2013年11月到期。如今 Skype 换了一个新的合作伙伴，叫做“光明方正”（这是《光明日报》跟北大方正的合资公司）。以前在天朝访问 Skype 官网会自动跳转到 skype.tom.com 网站，如今则自动跳转到 skype.gmw.cn 网站。考虑到《光明日报》是朝廷的喉舌，估计现在这个“光明版 Skype”也不会是啥好鸟。<br /><br /><h3>◇“服务器泄露”导致的隐私问题</h3><br />&#12288;&#12288;除了“敏感词监控”，还有其它一些问题也会导致隐私泄露。比如腾讯的系统如果出现安全方面的漏洞并且被骇客利用，那么腾讯用户的很多隐私都会暴露无遗。<br /><br />&#12288;&#12288;举例1：<br />&#12288;&#12288;如果你在 QQ 的聊天内容中发送过 URL 网址，这个网址会被“腾讯搜搜”抓取。如果这是一个公开的网址，倒也无所谓。但万一这是个【私密的网址】，那就麻烦啦。比如有些网民会在 QQ 聊天中发送“微信支付（财付通）”的订单网址，那么这些私密订单网址就会被“腾讯搜搜”收录下来。然后骇客就可以去“腾讯搜搜”里面收集大量网友的订单信息。相关报道如下：<br />《<a href="http://news.itxinwen.com/2013/1114/542576...md" target="_blank" rel="nofollow">腾讯 QQ 微信均现安全隐患 漏洞十分严重 @ IT商业网</a>》<br /><br />&#12288;&#12288;举例2：<br />&#12288;&#12288;去年（2013）11月，腾讯的 QQ 群数据被泄露，数据量高达90GB，涉及了7000多万个 QQ 群。根据这批数据，你可以用 QQ 号查询到姓名、年龄、社交关系网等大量个人隐私。如果你是 QQ 的长期用户，你的个人喜好（包括那些猥琐的喜好）就一览无遗啦 :)<br />&#12288;&#12288;相关报道如下：<br />《<a href="http://news.xinhuanet.com/legal/2013-11/21/c_125741520.htm" target="_blank" rel="nofollow">腾讯 QQ 群数据库泄露事件追踪 @ 新华网</a>》<br />《<a href="http://www.wooyun.org/bugs/wooyun-2013-043251" target="_blank" rel="nofollow">腾讯群关系数据泄漏（可根据 QQ 号获得该人姓名经历等详细信息） @ 乌云</a>》<br /><br /><h2>★下载类</h2><br />&#12288;&#12288;国内最知名的下载工具大概就是“迅雷”了。所以重点说说它的劣迹。<br /><br /><h3>◇暴露你的私有文件</h3><br />&#12288;&#12288;正常的 P2P 下载软件，只会上传“用户共享出来的目录里的文件”。但是迅雷可没有这么规矩。据说它会擅作主张，查找你电脑硬盘中的文件。如果某个文件正好是当前的热门下载，迅雷就会把该文件上传给其他正在下载的用户（以此来“提速”）。这种做法从某种程度上暴露了你的隐私。相关报道如下：<br />《<a href="http://www.cnbeta.com/articles/48566.htm" target="_blank" rel="nofollow">小心，你的文件正在被迅雷盗窃！ @ cnBeta</a>》<br />《<a href="http://tech.163.com/08/0220/07/454J7F85000915BF..md" target="_blank" rel="nofollow">迅雷被疑盗窃用户文件 @ 网易科技</a>》<br />&#12288;&#12288;顺便说一下：这种搞法除了引发隐私问题，还会（在未经你许可的情况下）浪费你的网络带宽和硬盘性能。从某种意义上讲，这就是“耍流氓”。<br /><br /><h3>◇收集你的下载网址——并有可能暴露你的【私有网址】</h3><br />&#12288;&#12288;跟“360安全浏览器”类似，迅雷也会把每一个用户的每一个下载网址收集到自己的服务器上。迅雷公司这么干是为了尽可能多地收集“下载源”，但也导致了一个严重的隐私问题——迅雷公司掌握了你所有的下载历史。具体请看<a href="https://zh.wikipedia.org/wiki/%E8%BF%85%E9%9B%B7" target="_blank" rel="nofollow">维基百科的词条</a>。<br />&#12288;&#12288;如果你用迅雷下载的网址是一个【私有网址】，那么这个私有网址不但会被其他迅雷用户看到，还会被别人用来下载。其中的危害参见“<a href="http://blog.renren.com/share/339395554/4200801364" target="_blank" rel="nofollow">这篇网文</a>”。<br /><br /><h3>◇其它的隐私问题</h3><br />&#12288;&#12288;除了这两个，还有一些迅雷软件的功能也会导致隐私问题，具体请看下面这篇：<br />《<a href="http://www.360doc.com/content/09/0506/01/81932_3387434...md" target="_blank" rel="nofollow">不看不知道——迅雷正在疯狂的吞噬你的隐私</a>》（这篇文章是2009年的，其中的描述可能跟当前的迅雷版本有一定出入）<br /><br /><h2>★媒体播放类</h2><br />&#12288;&#12288;最后再来聊聊媒体播放类的软件。媒体播放软件主要有“视频播放”和“音乐播放”两大类（当然，也有些是二合一的）。不论是“视频播放”和“音乐播放”，播放软件都【有可能】收集你播放的媒体信息，然后发送到厂商的服务器上。<br />&#12288;&#12288;举例：<br />&#12288;&#12288;请看2007年的一篇报道——《<a href="http://tech.163.com/07/0803/09/3KV9TFAR000915AS..md" target="_blank" rel="nofollow">暴风排行榜正式发布 1.4亿用户观影习惯揭晓 @ 网易科技</a>》。暴风影音是如何统计出几亿用户的“观影习惯”？它收集用户的“观影习惯”，得到用户许可了吗？<br />&#12288;&#12288;经读者在评论中提醒，除了上述这种方式（播放器主动发送媒体信息），还有一种方式是利用“自动下载字幕”这一功能。比如“射手影音”提供的“智能字幕”功能，会自动去射手网匹配字幕。此时，字幕服务器会收集到你正在播放的视频信息。<br /><br /><h2>★其它软件的隐私问题</h2><br />&#12288;&#12288;前面俺列出了几类特别有代表性的桌面软件导致的隐私问题。千万【不要】以为，只有这几类软件会导致隐私问题。<b>其它类别的软件，同样也可能有隐私问题。</b><br /><br />&#12288;&#12288;举例：<br />&#12288;&#12288;比如前几天被曝光的“支付宝监控网络丑闻”，率先曝光的是“<a href="http://blog.superliufa.com/2014/07/Alipaybsm-RawSocket..md" target="_blank" rel="nofollow">这篇博文</a>”（此文已被广为流传）。<br />&#12288;&#12288;阿里巴巴旗下的支付宝安全控件，同样是一个装机量非常巨大（亿级）的桌面软件。考虑到阿里巴巴在电子商务和在线支付的市场份额，支付宝控件的装机量说不定比 360 还高。这么大的装机量，阿里巴巴动了邪念，那是很正常滴（马云本来就没啥人品可言）。退一步讲，就算阿里巴巴没有动邪念，朝廷也会动邪念滴——此中的道理，前面已经解释过了。<br /><br /><h2>★结尾</h2><br />&#12288;&#12288;本文列举了几类特别具有代表性的软件类型（分别是：安全类、输入法类、即时通信类、下载类、媒体播放类）。如果你认为其它某个分类也很有代表性，欢迎到本文留言。<br />&#12288;&#12288;在<a href="../../2013/06/privacy-protection-0.md">本系列</a>的下一篇，俺会来介绍一下，如何反击桌面软件偷窥隐私的流氓行为。另外，有些读者可能会问：为啥本文聊了“即时通信”，但是却没有聊“电子邮件”和“社交网络”。因为俺觉得这两类更偏重于“服务器端”，所以在本系列的下下篇，再来单独聊“互联网服务”导致的隐私问题。俺初步考虑，会介绍“搜索引擎、电子邮件、社交网络、网盘、......”的隐私问题。<br /><br /><a href="../../2013/06/privacy-protection-0.md#index">回到本系列的目录</a><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="2014/08/privacy-protection-7.md">2014/08/privacy-protection-7.md</a>
</div>
</div>
</body>
<.md>