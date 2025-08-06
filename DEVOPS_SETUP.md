# Azure DevOps Pipeline 配置指南

## 概述

由于项目文件夹结构已更改，Azure DevOps平台上的Pipeline配置需要进行相应调整。

## 1. 变量组配置

### 创建变量组
在Azure DevOps中创建变量组 `AI_CODE_REVIEW`：

1. 进入Azure DevOps项目
2. 点击 `Library` → `Variable groups`
3. 点击 `+ Variable group`
4. 设置名称为 `AI_CODE_REVIEW`
5. 添加以下变量：

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `MOONSHOT_API_KEY` | Moonshot/Kimi API密钥 | `sk-xxxxxxxxxxxxxxxx` |
| `WIKI_URL_BASE` | Azure DevOps Wiki API基础地址 | `https://dev.azure.com/org/project/_apis/wiki/wikis/wiki.wiki/pages` |
| `WIKI_PAT` | 用于Wiki上传的PAT Token | `xxxxxxxxxxxxxxxx` |

### 获取Wiki URL Base
1. 进入Azure DevOps项目
2. 点击 `Wiki` → 选择你的Wiki
3. 在浏览器地址栏中，复制基础URL，格式类似：
   ```
   https://dev.azure.com/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages
   ```

### 创建PAT Token
1. 进入Azure DevOps → `User Settings` → `Personal access tokens`
2. 点击 `New Token`
3. 选择 `Custom defined`，设置权限：
   - `Wiki (Read & Write)`
4. 复制生成的token

## 2. Pipeline配置更新

### 目标项目Pipeline
目标项目的 `azure-pipelines.yml` 已更新为：

```yaml
# 目标项目的 azure-pipelines.yml
trigger:
  - main

pr:
  - main

extends:
  template: ai_code_review/templates/ai-review.yml
  parameters:
    projectName: 'target-project'
    standardsFile: ai_code_review/standards/python_standards.txt
    codeTypes:
      - '.py'
      - '.js'
      - '.ts'
    enableWikiUpload: true
    enableArtifacts: true
```

### 路径说明
- **模板路径**: `ai_code_review/templates/ai-review.yml` (相对于项目根目录)
- **标准文件路径**: `ai_code_review/standards/python_standards.txt` (相对于项目根目录)

## 3. 权限配置

### Pipeline权限
确保Pipeline有权限访问：
1. 变量组 `AI_CODE_REVIEW`
2. Wiki仓库
3. 代码仓库

### 安全设置
1. 所有敏感信息（API密钥、PAT Token）都存储在变量组中
2. 变量组设置为"Secret"类型
3. 限制变量组的访问权限

## 4. 测试配置

### 测试步骤
1. 提交代码到仓库
2. 创建Pull Request
3. 检查Pipeline是否正常触发
4. 验证AI代码审核是否执行
5. 检查Wiki是否成功上传审核结果

### 常见问题排查
1. **模板路径错误**: 确保模板路径正确，相对于项目根目录
2. **变量组访问失败**: 检查Pipeline是否有权限访问变量组
3. **Wiki上传失败**: 验证PAT Token权限和Wiki URL是否正确
4. **API调用失败**: 检查Moonshot API密钥是否有效

## 5. 监控和维护

### 监控指标
- Pipeline执行成功率
- AI审核响应时间
- Wiki上传成功率
- 审核结果质量

### 定期维护
- 更新API密钥
- 检查PAT Token有效期
- 更新代码标准文件
- 监控API使用量

## 6. 最佳实践

1. **环境分离**: 为不同环境（开发、测试、生产）创建不同的变量组
2. **权限最小化**: 只授予必要的权限
3. **日志记录**: 启用详细的Pipeline日志
4. **备份配置**: 定期备份Pipeline配置
5. **文档更新**: 及时更新配置文档 