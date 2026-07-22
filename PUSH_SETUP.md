# TrendRadar 推送设置

当前任务每天按北京时间 **08:17、12:17、18:17、22:17** 自动运行，也可以在 GitHub 仓库的 **Actions → Get Hot News → Run workflow** 中手动运行。

## 1. 在哪里填写

进入仓库：

`Settings → Secrets and variables → Actions → New repository secret`

每次添加一项，下方表格左侧填入 **Name**，右侧填入你的实际值。Webhook、Token、邮箱授权码都属于密钥，**不要写入 `config/config.yaml`，不要提交到 Git**。

## 2. 选择一个推送渠道

不需要全部配置。个人使用优先推荐 **ntfy** 或 **Telegram**；国内群聊可用飞书、钉钉或企业微信。

| 渠道 | GitHub Actions Secrets | 说明 |
| --- | --- | --- |
| ntfy | `NTFY_TOPIC` | 必填；建议使用足够随机、难猜的主题名 |
| ntfy 私有服务 | `NTFY_SERVER_URL`、`NTFY_TOKEN` | 可选；默认服务地址为 `https://ntfy.sh` |
| Telegram | `TELEGRAM_BOT_TOKEN`、`TELEGRAM_CHAT_ID` | 两项都必填 |
| 飞书 | `FEISHU_WEBHOOK_URL` | 群机器人 Webhook |
| 钉钉 | `DINGTALK_WEBHOOK_URL` | 群机器人 Webhook |
| 企业微信 | `WEWORK_WEBHOOK_URL` | 群机器人 Webhook |
| 企业微信消息类型 | `WEWORK_MSG_TYPE` | 可选，通常填 `markdown` |
| 邮件 | `EMAIL_FROM`、`EMAIL_PASSWORD`、`EMAIL_TO` | 密码应使用邮箱授权码；多个收件人用英文逗号分隔 |
| 邮件 SMTP | `EMAIL_SMTP_SERVER`、`EMAIL_SMTP_PORT` | 可选，常见邮箱可自动识别 |
| Bark | `BARK_URL` | iPhone Bark 完整推送 URL |
| Slack | `SLACK_WEBHOOK_URL` | Incoming Webhook URL |
| 通用 Webhook | `GENERIC_WEBHOOK_URL` | 支持 Discord、Matrix、IFTTT 等 |
| 通用 Webhook 模板 | `GENERIC_WEBHOOK_TEMPLATE` | 可选，例如 `{"content":"{content}"}` |

同一渠道需要多个账号时，用英文分号 `;` 分隔。Telegram 的 Token 与 Chat ID 数量和顺序必须一一对应。

## 3. 最省事的 ntfy 配置

1. 安装 ntfy 手机应用，或打开 [ntfy.sh](https://ntfy.sh/)。
2. 订阅一个不容易被猜到的主题，例如随机字符串，而不是 `trendradar` 这类公开名称。
3. 在 GitHub Actions Secrets 新增 `NTFY_TOPIC`，值填写该主题。
4. 手动运行一次 `Get Hot News` 工作流验证推送。

公共 ntfy 主题只依赖名称，不适合传输敏感内容。需要访问控制时，请使用私有主题或自托管服务，并设置 `NTFY_TOKEN`。

## 4. Telegram 配置

1. 在 Telegram 中通过 BotFather 创建机器人，取得 Bot Token。
2. 给机器人发送一条消息，再取得对应 Chat ID。
3. 新增 `TELEGRAM_BOT_TOKEN` 和 `TELEGRAM_CHAT_ID` 两个 Secrets。
4. 手动运行一次工作流验证。

## 5. 推送行为

`config/config.yaml` 中的 `notification.enabled` 已开启。当前默认是 `current` 报告模式，所以每次运行都会发送当时的热点；如果只想在出现新内容时收到通知，可将 `report.mode` 改为 `incremental`。

AI 分析内容已加入网页与推送区域。是否执行 AI、何时推送，还可以通过 `config/timeline.yaml` 和 `schedule.enabled` 做更细的分时控制。

## 6. 排查

如果没有收到消息：

1. 打开仓库 **Actions → Get Hot News → 最近一次运行**。
2. 查看 `Run crawler` 日志中对应渠道是否显示已启用。
3. 检查 Secret 名称的大小写、Webhook 是否完整，以及机器人是否仍在群中。
4. 修改 Secret 后重新手动运行；Secret 本身不会显示在日志中。

