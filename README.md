# V2EX 自动签到工具

一个简化的V2EX自动签到脚本，只保留V2EX签到功能，支持Telegram通知。

## 功能特点

- ✅ V2EX 每日签到获取铜币
- ✅ 自动获取账户余额
- ✅ 失败重试机制
- ✅ 详细的签到日志
- ✅ Telegram 通知推送

## 安装使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制环境变量模板文件：
```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的配置信息：

#### 2.1 获取 V2EX Cookie（必需）

1. 登录 [V2EX](https://www.v2ex.com/)
2. 打开浏览器开发者工具（F12）
3. 切换到 "Network" 标签
4. 刷新页面（F5）
5. 点击任意一个请求
6. 在 "Request Headers" 中找到 `Cookie` 字段
7. 复制完整的 Cookie 值到 `.env` 文件

#### 2.2 配置 Telegram 通知（可选）

如果需要Telegram通知，请按以下步骤配置：

**创建 Telegram Bot：**
1. 在 Telegram 中搜索 `@BotFather`
2. 发送 `/newbot` 命令创建新机器人
3. 按提示设置机器人名称和用户名
4. 获取 Bot Token，填入 `.env` 文件

**获取用户ID：**
1. 在 Telegram 中搜索 `@userinfobot`
2. 发送任意消息获取你的用户ID
3. 将用户ID填入 `.env` 文件

### 3. 运行签到

```bash
python main.py
```

## 文件说明

- `main.py` - 主程序入口，包含Telegram通知功能
- `v2ex_checkin.py` - V2EX签到核心逻辑
- `requirements.txt` - 依赖包列表
- `.env.example` - 环境变量配置模板
- `.env` - 环境变量配置文件（需要自己创建）

## 注意事项

1. V2EX Cookie 有效期有限，失效后需要重新获取
2. 签到时间为每日任意时间，建议配合定时任务使用
3. 如果遇到人机验证，可能需要手动完成一次登录
4. Telegram通知为可选功能，不配置也能正常使用

## 定时任务配置

**Linux Crontab:**
```bash
# 每天早上8点签到
0 8 * * * cd /path/to/v2ex-checkin && python main.py
```

**Windows 任务计划程序:**
创建基本任务，设置每日定时运行 `python main.py`

## 许可证

MIT License