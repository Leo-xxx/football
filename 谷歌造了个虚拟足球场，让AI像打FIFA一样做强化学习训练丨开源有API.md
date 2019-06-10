## 谷歌造了个虚拟足球场，让AI像打FIFA一样做强化学习训练丨开源有API

原创： 关注前沿科技 [量子位](javascript:void(0);) *昨天*

##### 郭一璞 发自 苏州街  量子位 报道 | 公众号 QbitAI

除了下棋、雅达利游戏和星际，AI终于把“魔爪”伸向了粉丝众多的体育竞技活动：

足球。

今天，谷歌开源了足球模拟环境**Google Research Football**，智能体可以在这个宛若FIFA的世界里自由踢球，学到更多踢球技巧。

用足球进行强化学习训练，对AI来说更有挑战性，不仅要能控球，还得搞懂传球、角球这些概念，知道什么时候会犯规吃红牌黄牌，同时训练出足够机智的策略。虽然AI足球没有体能挑战，但智慧上的要求有增无减。

不少热爱足球的网友看到之后都十分激动，终于能把自己的爱好和研究结合在一起了。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQgIJF8CzvOscPica0nGPr9Tyib5chjCib8hIGLibm7pArRtMfs4kR7Bh5bw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

甚至还有人为中国足球请愿：求谷歌帮帮国足吧！

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQddfTZ1Wecf1sJoC52qeWmicLLFSD2SZ6NvvSPSSiciaG7kHT2SBzll8xg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 可以打人机的足球引擎

这个模拟环境基于开源的足球游戏模拟器Gameplay Football，用C++编写，在GPU和CPU上都能跑。

整个环境包含一场球赛中的各种环节，和正常的人类足球赛一样，两支队伍各11名运动员，一个智能体可以控制一个球员，也可以控制一整只队伍，双方遵循正常的足球规则进行比赛。

比如可以开球。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQXCibEY2gDame9Pl6H1BgDYXMxiakAEhVrpWsxra4iakk9cjxquBrckdCA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

射门。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQicrSKkp4zpJB6MOEBjHZMYhLcETgTmxUKyC2NXRxLV7EvXkX3PVBNIw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

还有裁判会给出判罚，智能体也可能吃红牌黄牌。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQYnLKeQUibVaZHkKD21rpfibUWopG4SzRTAWbFK7R9xQmQfkZGlkB05XA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

必要的时候还得会踢角球。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQAFTLYiazwpJJcQPdxRTPuEJ7FmMq3VOcCtK2K0Q7PWgibcfFJmAHOzDg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

整个模拟环境中，AI球员们可以进行包括上下左右移动、长传、射门等在内的16种动作。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQPJEKbFWM0fIia0sLrsPCAvMJ1BxhUMyzFicFNjnqia4B21HIlIich2PyRA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

甚至，AI球员们还会和人类一样，踢久了就会累，你还能给每支球队准备3个题目。总之，这个模拟环境相当完备，具备各种功能和规则体系。

而且操作也十分方便，你可以直接用API把OpenAI Gym接入进来。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQ4yjq8PibGRyzGjCamlGvt4u8DR00HE2kw9YVgkBDaxDSeZnicj7PLgow/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

而且，整个模拟环境中不仅可以用AI球员，还可以手动控制球员，用键盘上下左右移动，按字母键进行传球、射门等操作，与AI对战。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQHr5cXDQUM9tLzoBPeSoC5z3ufXOsaBwLeteic4qxQYz0HCOlhS6GDyw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

模拟环境内置了高中低三个难度的对手AI，也可以自行调整难度。当然你也可以把两个自己的AI放进去，让他们互相伤害。

## benchmark

Google不只准备了模拟环境，还为这个AI足球设定了一套benchmark。

谷歌用DQN和Impala两个强化学习算法在模拟环境中测试，将它们的奖励均设定为进球得分，在高中低三个难度上得到了运行结果。

![img](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQbfh5Sm5qwgI6pwLEjyrxiaibhWICk22yibDxX59LWtFtS5pCNbCTFlvKg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 足球学院

另外，为了让AI专点突破，Google还推出了足球学院（Football Academy），针对各种难度场景进行单独训练。

包括传球策略

![img](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQKlptgNMFQarttjEbkPbpFibIVwjMg3He7GhAnxEgZDkcgQPhyfabhzQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

队友配合

![img](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQXKI1VnOMSOufLibCU6vicibzCyXiapMTk4ia5grVHOPhBlYohotnH3l0dBw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

碰到2打1怎么办

![img](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQ0PibVl5ZP0mZL3icgGFxMS3bHPZlY3MT2kaxbhGRa1d6uiaYF5OTTkpiag/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

角球得分训练

![img](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtAoQQzgZRTF2EcRW1kDqCyQXekhZgKnhM6kEatT27kNta4KDyeG3EuT1lIKwdbotRaZGzVn7nqEAQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## 传送门

Google AI博客：
https://ai.googleblog.com/2019/06/introducing-google-research-football.html

论文下载地址：
https://github.com/google-research/football/blob/master/paper.pdf?raw=True

GitHub：
https://github.com/google-research/football

— **完** —

**小程序|全类别AI学习教程**

[![img](https://mmbiz.qpic.cn/mmbiz_jpg/YicUhk5aAGtDpADEKp9rvicB48XgA8ueVdwNbXM1wibYx0ic2pYicwu3UCU5BM6fpDvbH8c4e9JV3uGvYaWAhvGiaTVQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247522669&idx=3&sn=b61f45ec1e5fa2a8f92134fd64ba244f&chksm=e8d02e1fdfa7a7094e1e0416e98fa1604db98ca3c5762ccf9edeb22f4993f69ff1f2dc71d4d3&mpshare=1&scene=1&srcid=&key=c47853a08ff0b5df06032ffbb2a4fb15f20538bbc35b35697e315fdde94271c68b3d3c0208175d067dd1a7aae1330e7cc262c58a9379383399181bbadbc6dfd4eb4cea78197c7412ca59cbd06d47dfd9&ascene=1&uin=MjMzNDA2ODYyNQ%3D%3D&devicetype=Windows+10&version=62060833&lang=zh_CN&pass_ticket=GxXW%2BYQX1psMWCJS0GvNHFnezM8ua32guJKAFZ6Q4xS7s09zDR6qrh95cuHftuM4)

**AI社群|与优秀的人交流**



![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)



**量子位** QbitAI · 头条号签约作者





վ'ᴗ' ի 追踪AI技术和产品新动态



喜欢就点「在看」吧 !











微信扫一扫
关注该公众号