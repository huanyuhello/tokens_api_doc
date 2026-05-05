# Trae 配置使用 API 教程

**Trae** 是一款强大的、由 AI 驱动的集成开发环境 (IDE)，它基于 VS Code 构建，如果你用过 VS Code，会对 Trae 的界面感到非常熟悉。

本教程主要通过安装并配置 **Trae** 中的 Cline 插件，以接入 Tokens平台提供的 API。

**Trae** 官方下载地址：[https://www.trae.cn/](https://www.trae.cn/)

由于 **Trae** 兼容 VS Code 插件，我们可以直接在 **Trae** 的插件市场中进行安装。

1.打开插件市场，搜索 Cline

2.点击 “安装”

3.等待安装完成，左侧活动栏看到 Cline 图标

如下图所示：

## 二、Trae 配置第三方 API#
1.点击 **Trae** 左侧活动栏的 **Cline** 图标，在其设置界面中填写配置信息，如下图所示。

```
Base URL：http://47.102.134.41:3000/v1 
API Key：sk-xxx（你的 Tokens 平台令牌密钥）
```
2.在 Model ID 中，可以选择或输入希望使用的模型名称，例如 gpt-5.2，然后保存完成。

注意

选择或输入的模型名称必须与平台模型广场中的模型名称保持一致，可以直接复制黏贴过来。