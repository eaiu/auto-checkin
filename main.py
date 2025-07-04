# -*- coding: utf-8 -*-
# V2EX 自动签到工具

import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
from v2ex_checkin import main as v2ex_main

# 加载环境变量文件（自动查找.env文件位置）
script_dir = Path(__file__).parent
env_file = script_dir / '.env'
load_dotenv(env_file)

# Telegram通知功能
def send_telegram_notification(message):
    """发送Telegram通知"""
    try:
        from telegram import Bot
        
        bot_token = os.environ.get("TG_BOT_TOKEN")
        user_id = os.environ.get("TG_USER_ID")
        
        if bot_token and user_id:
            bot = Bot(token=bot_token)
            bot.sendMessage(
                chat_id=user_id,
                text=message,
                parse_mode="HTML"
            )
            print("✅ Telegram通知发送成功")
        else:
            print("ℹ️ 未配置Telegram，跳过通知")
    except Exception as e:
        print(f"❌ Telegram通知发送失败: {e}")

if __name__ == '__main__':
    print("V2EX 自动签到工具")
    print("="*50)
    
    # 调试信息
    print(f"脚本位置: {Path(__file__).parent}")
    print(f".env文件位置: {env_file}")
    print(f".env文件存在: {env_file.exists()}")
    
    # 检查环境变量
    v2ex_cookies = os.environ.get("V2EX_COOKIES")
    if not v2ex_cookies:
        print("错误：请在 .env 文件中设置 V2EX_COOKIES")
        print("提示：复制 .env.example 为 .env 并填入配置信息")
        exit(1)
    else:
        print(f"✅ V2EX_COOKIES 已加载 (长度: {len(v2ex_cookies)} 字符)")
    
    # 开始签到
    start_time = time.time()
    utc_time = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"开始时间: {utc_time}")
    print("="*50)
    
    # 执行签到
    result = v2ex_main()
    print(result)
    
    # 统计信息
    end_time = time.time()
    task_time = int(end_time - start_time)
    summary = f"任务完成，用时: {task_time} 秒"
    print("="*50)
    print(summary)
    
    # 发送Telegram通知
    telegram_message = f"V2EX 自动签到结果\n\n{result}\n\n开始时间: {utc_time}\n任务用时: {task_time} 秒"
    send_telegram_notification(telegram_message)