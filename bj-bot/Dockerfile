# 第一阶段：构建
FROM node:16.20.2-alpine3.18 AS builder
WORKDIR /app

# 安装构建工具
RUN apk add --no-cache python3 make g++

# 复制依赖描述
COPY package*.json ./

# 限制并发编译负载为 1
# 1) 设置 npm_config_jobs=1，npm install 时 node-gyp 用单线程编译
# 2) 设置 MAKEFLAGS="-j1"，确保所有 make 调用都只用一个作业
ENV npm_config_jobs=1
ENV MAKEFLAGS="-j1"

# 安装所有依赖，包括 native 模块的编译
RUN npm install --registry=https://registry.npmmirror.com

# 复制项目源代码
COPY . .

# 第二阶段：运行时
FROM node:16.20.2-alpine3.18 AS runtime
WORKDIR /app

# 只复制 production 依赖
COPY --from=builder /app/node_modules ./node_modules
# 复制项目源代码
COPY --from=builder /app ./

# 删除构建工具，保持镜像精简
RUN apk del --no-cache python3 make g++

ENTRYPOINT ["node", "index.js"]
