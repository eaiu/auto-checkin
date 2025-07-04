FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY *.py ./
COPY .env.example ./

# 创建非root用户
RUN useradd -m -s /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# 健康检查
HEALTHCHECK --interval=1h --timeout=30s --start-period=10s --retries=3 \
    CMD python -c "import os; exit(0 if os.environ.get('V2EX_COOKIES') else 1)"

# 默认命令
CMD ["python", "main.py"]