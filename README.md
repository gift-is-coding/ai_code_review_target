# AI 代码审核项目

简化的AI代码审核工具，支持多种编程语言。

## 项目结构

```
ai_code_review_target/
├── ai_code_review/                    # AI 代码审核工具
│   ├── auto_review.py                # 主要审核脚本
│   ├── requirements.txt              # Python 依赖
│   ├── README.md                     # 工具使用说明
│   └── standards/                    # 代码标准文件
│       └── code_standards.txt        # 通用代码标准
├── target_project_code/              # 目标项目代码
│   ├── demo.py                       # 示例代码文件
│   └── README.md                     # 项目说明
└── azure-pipelines.yml               # Azure DevOps Pipeline
```

## 功能特点

- **统一标准**: 使用通用的代码标准，适用于所有编程语言
- **简化配置**: 只需要一个Pipeline文件
- **自动触发**: 在PR和主分支提交时自动运行
- **结果保存**: 审核结果保存到Build Artifacts和Wiki

## 使用方法

### 1. 配置Azure DevOps

1. 创建变量组 `AI_CODE_REVIEW`，包含：
   - `MOONSHOT_API_KEY`: Moonshot/Kimi API密钥
   - `WIKI_URL_BASE`: Azure DevOps Wiki API基础地址
   - `WIKI_PAT`: 用于Wiki上传的PAT Token

2. 在Azure DevOps中创建Pipeline，选择 `azure-pipelines.yml` 文件

### 2. 支持的代码类型

- Python (`.py`)
- JavaScript (`.js`, `.ts`)
- Java (`.java`)
- Go (`.go`)
- C++ (`.cpp`)
- Vue (`.vue`)
- HTML (`.html`)
- CSS (`.css`)

### 3. 审核流程

1. 提交代码到仓库
2. Pipeline自动触发
3. AI分析代码变更
4. 生成审核报告
5. 保存到Artifacts和Wiki

## 注意事项

1. 确保变量组配置正确
2. 检查Wiki权限设置
3. 监控API使用量 