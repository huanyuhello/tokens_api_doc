## 1、什么是hermes agent#
`Hermes Agent 是 Nous Research 开发的开源自主 AI 智能体，于 2026 年 2 月发布。它不是绑定在 IDE 上的代码补全工具，也不是套壳聊天机器人——它住在你的服务器上，记住它学到的一切，运行越久能力越强。支持 Linux、macOS 和 WSL2，一条 curl 命令即可安装，无需任何前置依赖。`

## 2、hermes agent快速上手#
`linux 安装命令： curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`

![image-20260421151750508.png](../resource/646112.png)

![image-20260421153250906.png](../resource/646113.png)
**因为我此前已经配置过一个了，所以我选择了29，一般的是选择28 Custom endpoint。**
![image-20260421153342382.png](../resource/646114.png)

**填入url key 模型id**

![image-20260421154809060.png](../resource/646115.png)

![image-20260421154942402.png](../resource/646116.png)

`在用户的根目录下
root@tokens:~/.hermes# cd 
root@tokens:~# source ~/.bashrc  //加载环境变量`

![image-20260421165337822.png](../resource/646118.png)