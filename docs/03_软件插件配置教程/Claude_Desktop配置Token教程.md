# Claude Desktop 配置 4SAPI 教程（测试中）

⚠️ 重要前提（必须看）
必须使用最新版 Claude Desktop：低版本可能没有开发者模式或第三方推理配置入口。
建议先保持未登录状态：不需要先登录 Claude 官方账号。如果已经登录，建议先退出后再配置。
必须使用支持 Anthropic-compatible 的第三方 API：单纯 OpenAI-compatible 的接口不一定能用。
Gateway base URL 需要是 HTTPS 地址：并且对应服务需要支持 Anthropic Messages API，通常也就是能处理 /v1/messages 请求。
本教程以 Windows 为例，截图也是 Windows 环境下的界面

## 步骤 1：打开 Claude Desktop 并启用开发者模式#
1.打开 Claude Desktop，先不要登录官方账号。
2.如果当前界面不好直接点菜单，可以按键盘 Tab 切到左上角菜单区域，再按回车打开菜单。
3.在顶部菜单栏选择 Help（帮助） → Troubleshooting（疑难解答）。
4.在弹出的子菜单里点击 Enable Developer Mode（启用开发者模式）

启用成功后，顶部菜单栏会多出一个 Developer（开发者） 菜单

## 步骤 2：进入第三方 API 配置页面#
1.点击新出现的 Developer 菜单。
2.选择 Configure Third-Party Inference…（配置第三方推理…）。

## 步骤 3：填写 Base URL 和 API Key（最关键一步）#
打开配置窗口后，按下面方式设置：

Use this configuration：打开开关，必须开启。

Gateway：选择 Anthropic-compatible。

Gateway base URL：[http://47.102.134.41:3000](http://47.102.134.41:3000)

Gateway API key：粘贴你的 API Key，也就是控制台的令牌管理复制出来的那串密钥。

Gateway auth scheme：一般保持默认即可。

Gateway extra headers：一般不用填写。

设置完后，点击右下角 Apply locally（本地应用）。

选择重新启动软件

选择第一个

选择模型

## 步骤 4：验证是否成功#
配置完成后，Claude Desktop 可能会提示重启；如果没有提示，也建议手动完全退出后重新打开。
重新打开后，进入 Cowork、Code 或 Projects 相关页面。
输入一个简单问题测试。
如果模型能正常响应，或者界面中显示的是你第三方 API 提供的模型，就说明配置成功