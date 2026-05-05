# vscode接入4sapi教程

前置条件：

一个4sapi claudecode的令牌key [http://47.102.134.41:3000](http://47.102.134.41:3000)

**安装 Claude Code：**
要安装 Claude Code，请按以下两个流程进行:
**1、本地安装（推荐）**
**macOS, Linux, WSL，Windows PowerShell，Windows CMD:**

```
npm install -g @anthropic-ai/claude-code
```
**2、配置本地的sttings.json或者环境变量（二选一如有配置请忽略）**
`settings文件路径 C:\Users\用户名\.claude\settings.json`

```
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-hUOgVOGw0qdyk*****************",
    "ANTHROPIC_BASE_URL": "http://47.102.134.41:3000",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-opus-4-6",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-6",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-opus-4-6",
    "ANTHROPIC_MODEL": "claude-opus-4-6",
    "ANTHROPIC_REASONING_MODEL": "claude-opus-4-6"
  },
  "includeCoAuthoredBy": false
}
```
**3、测试使用cmd输入claude是否能正常对话**

```
注意！！！claude code会自动读取文件夹下的文件，建议一个空文件夹测试。防止消耗大量token
```

**安装 VScode插件（Claude Code for VS Code）：**

#### 1、打开VScode界面#

#### 2、打开VScode的扩展#

#### 3、在扩展商城中搜索Claude，就会出现许多相关插件#

##### 在配置中添加以下代码：#

#### 4、打开插件,按照上面流程配置好Claude即可使用#