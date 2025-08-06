# AI 代码审核项目

本项目包含 AI 代码审核工具和目标项目代码，采用分离式文件夹结构。

## 项目结构

```
ai_code_review_target/
├── ai_code_review/                    # AI 代码审核工具
│   ├── auto_review.py                # 主要审核脚本
│   ├── test_wiki.py                  # Wiki 连接测试脚本
│   ├── requirements.txt              # Python 依赖
│   ├── config.yaml                   # 配置文件
│   ├── azure-pipelines.yml           # 工具自身的 Pipeline
│   ├── README.md                     # 工具使用说明
│   ├── standards/                    # 代码标准文件
│   │   ├── python_standards.txt
│   │   ├── javascript_standards.txt
│   │   └── java_standards.txt
│   ├── templates/                    # Azure Pipeline 模板
│   │   └── ai-review.yml
│   └── examples/                     # 示例项目配置
│       ├── python-project/
│       ├── javascript-project/
│       └── java-project/
└── target_project_code/              # 目标项目代码
    ├── demo.py                       # 示例代码文件
    ├── README.md                     # 项目说明
    └── azure-pipelines.yml           # 项目 Pipeline 配置
```

## 配置说明

### 1. AI 代码审核工具配置

AI 代码审核工具位于 `ai_code_review/` 文件夹中，包含：

- **auto_review.py**: 主要的代码审核脚本
- **test_wiki.py**: Wiki 连接测试脚本
- **config.yaml**: 配置文件，包含 API 密钥和 Wiki 配置
- **templates/ai-review.yml**: Azure Pipeline 模板
- **standards/**: 各种技术栈的代码标准文件

### 2. 目标项目配置

目标项目位于 `target_project_code/` 文件夹中，包含：

- **azure-pipelines.yml**: 配置使用 AI 代码审核的 Pipeline
- **demo.py**: 示例代码文件

### 3. 路径更新

所有相关的 YAML 文件中的路径都已更新为新的文件夹结构：

- 模板路径：`ai_code_review/templates/ai-review.yml`
- 标准文件路径：`ai_code_review/standards/{language}_standards.txt`
- 脚本路径：`ai_code_review/auto_review.py`

## 使用方法

### 1. 配置 AI 代码审核工具

1. 进入 `ai_code_review/` 文件夹
2. 修改 `config.yaml` 文件，配置你的 API 密钥和 Wiki 设置
3. 安装依赖：`pip install -r requirements.txt`

### 2. 测试 Wiki 连接

```bash
cd ai_code_review
python test_wiki.py
```

### 3. 运行代码审核

```bash
cd ai_code_review
python auto_review.py --project_name "your-project" --pr_only
```

### 4. 在目标项目中使用

目标项目的 `azure-pipelines.yml` 已经配置好，可以直接使用 AI 代码审核功能。

## 注意事项

1. 确保在 Azure DevOps 中创建了 `AI_CODE_REVIEW` 变量组
2. 配置正确的 API 密钥和 Wiki 设置
3. 根据项目技术栈选择合适的标准文件
4. 所有路径都已更新为新的文件夹结构 