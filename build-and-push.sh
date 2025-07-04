#!/bin/bash

# 构建和推送Docker镜像脚本
# 使用方法: ./build-and-push.sh [version]

set -e

# 默认版本
VERSION=${1:-latest}
IMAGE_NAME="eaiu/v2ex-checkin"

echo "🚀 开始构建Docker镜像..."

# 构建镜像
docker build -t ${IMAGE_NAME}:${VERSION} .

# 如果不是latest，也打一个latest标签
if [ "$VERSION" != "latest" ]; then
    docker tag ${IMAGE_NAME}:${VERSION} ${IMAGE_NAME}:latest
fi

echo "✅ 镜像构建完成"

# 检查是否已登录Docker Hub
if ! docker info | grep -q "Username"; then
    echo "⚠️  请先登录Docker Hub:"
    echo "   docker login"
    read -p "按Enter继续推送，或Ctrl+C取消..."
fi

echo "📤 推送镜像到Docker Hub..."

# 推送镜像
docker push ${IMAGE_NAME}:${VERSION}

if [ "$VERSION" != "latest" ]; then
    docker push ${IMAGE_NAME}:latest
fi

echo "🎉 镜像推送完成!"
echo "   镜像地址: ${IMAGE_NAME}:${VERSION}"
echo "   拉取命令: docker pull ${IMAGE_NAME}:${VERSION}"