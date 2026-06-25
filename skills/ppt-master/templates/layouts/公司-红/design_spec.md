# 公司-红 Style Template - Design Specification

> 适用于企业介绍、业务展示、云服务解决方案、公司年报等商务场景的专业红色企业模板。

---

## I. Template Overview

| Property       | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| **Template Name** | 公司-红 (Corporate Red Template)                          |
| **Use Cases**  | 企业介绍、云业务能力展示、解决方案汇报、年度总结、商务提案 |
| **Design Tone** | 专业、现代、商务、可信赖、科技感 |
| **Theme Mode** | 混合主题（红色渐变封面+白色内容页） |

---

## II. Canvas Specification

| Property       | Value                         |
| -------------- | ----------------------------- |
| **Format**     | Standard 16:9                 |
| **Dimensions** | 1280 × 720 px                |
| **viewBox**    | `0 0 1280 720`                |
| **Page Margins** | Left/Right 60px, Top 80px, Bottom 40px |
| **Safe Area**  | x: 60-1220, y: 80-680         |

---

## III. Color Scheme

### Primary Colors

| Role           | Value       | Notes                              |
| -------------- | ----------- | ---------------------------------- |
| **Corporate Red** | `#C41E3A` | 主色调，用于封面背景、章节页、强调元素 |
| **Deep Red** | `#8B0000` | 深红色，用于标题栏、装饰线条 |
| **Background White** | `#FFFFFF` | 内容页背景 |
| **Light Gray** | `#F8F9FA` | 辅助背景、卡片底色 |
| **Border Gray** | `#E9ECEF` | 分隔线、边框 |
| **Gold Accent** | `#D4AF37` | 金色点缀，装饰元素 |
| **Dark Navy** | `#1A1A2E` | 深色装饰，用于结束页 |

### Text Colors

| Role           | Value       | Usage                  |
| -------------- | ----------- | ---------------------- |
| **Primary Text** | `#1A1A1A` | 正文、标题 |
| **White Text** | `#FFFFFF` | 深色背景上的文字 |
| **Secondary Text** | `#495057` | 次要信息、说明文字 |
| **Light Text** | `#6C757D` | 注释、页码、提示信息 |

### Functional Colors

| Usage    | Value       | Description    |
| -------- | ----------- | -------------- |
| **Success** | `#28A745` | 完成/正常状态 |
| **Warning** | `#FFC107` | 注意/警告 |
| **Info**    | `#17A2B8` | 一般信息 |

---

## IV. Typography System

### Font Stack

**Font Stack**: `"Microsoft YaHei", "微软雅黑", "PingFang SC", "Source Han Sans SC", Arial, sans-serif`

### Font Size Hierarchy

| Level | Usage              | Size | Weight  |
| ----- | ------------------ | ---- | ------- |
| H1    | Cover main title   | 56px | Bold    |
| H2    | Page heading       | 32px | Bold    |
| H3    | Section title      | 24px | Bold    |
| P     | Body content       | 18px | Regular |
| High  | Highlighted data   | 36px | Bold    |
| Sub   | Supplementary text | 14px | Regular |

---

## V. Page Structure

### General Layout

| Area       | Position/Height | Description                            |
| ---------- | --------------- | -------------------------------------- |
| **Top Decoration** | y=0, h=4px | 红色渐变装饰条，全宽 |
| **Title Bar** | y=30, h=50px | 章节编号块 + 页面标题 |
| **Content Area** | y=100, h=560px | 主要内容区域 |
| **Footer** | y=680, h=40px | 页码、公司简称 |

### Navigation Bar Design

- **顶部装饰线**: Corporate Red渐变 (`#C41E3A` → `#8B0000`)，高度 4px，全宽
- **底部装饰线**: Deep Red (`#8B0000`)，高度 3px，y=717
- **标题栏** (y=30):
  - 章节编号块: Corporate Red圆角矩形 (50×50px，圆角8px)，白色数字居中
  - 页面标题: 距编号块20px，32px字号，`#1A1A1A`

---

## VI. Page Types

### 1. Cover Page (01_cover.svg)

- 红色渐变背景 (Corporate Red → Deep Red)
- 顶部金色装饰线
- 主标题 + 副标题（居中，白色）
- 公司名称
- 底部日期区域
- 几何装饰元素（半透明圆形）

### 2. Table of Contents (02_toc.svg)

- 白色背景 + 左侧红色竖条装饰
- 支持最多5个章节
- 编号使用红色圆角矩形块 + 白色数字
- 右侧数据统计展示区域

### 3. Chapter Page (02_chapter.svg)

- 深红色渐变背景
- 大号章节编号（半透明装饰）
- 章节标题 + 英文副标题
- 几何装饰元素

### 4. Content Page (03_content.svg)

- 白色背景
- 标准导航栏（红色圆角编号块）
- 灵活内容区域
- 支持多种布局模式

### 5. Ending Page (04_ending.svg)

- 深色渐变背景 (Dark Navy)
- 居中感谢语
- 公司名称
- 联系信息

---

## VII. Layout Modes

| Mode               | Use Cases                      |
| ------------------ | ------------------------------ |
| **Single Column Centered** | 封面、结束页、要点强调 |
| **Two Columns (5:5)** | 对比展示 |
| **Two Columns (4:6)** | 图文混排 |
| **Top-Bottom Split** | 流程描述、列表 |
| **Three-Column Cards** | 项目列表、数据展示 |
| **Matrix Grid**    | 分类展示 |
| **Table**          | 数据对比、规格列表 |

---

## VIII. Spacing Guidelines

| Element          | Value  |
| ---------------- | ------ |
| Card spacing     | 24px   |
| Content block spacing | 32px |
| Card padding     | 24px   |
| Card border radius | 12px  |
| Icon-to-text gap | 12px   |

---

## IX. SVG Technical Constraints

### Mandatory Rules

1. viewBox: `0 0 1280 720`
2. Use `<rect>` elements for backgrounds
3. Use `<tspan>` for text wrapping (no `<foreignObject>`)
4. Use `fill-opacity` / `stroke-opacity` for transparency; `rgba()` is prohibited
5. Prohibited: `clipPath`, `mask`, `<style>`, `class`, `foreignObject`
6. Prohibited: `textPath`, `animate*`, `script`, `marker`/`marker-end`
7. Use `<polygon>` triangles instead of `<marker>` for arrows

### PPT Compatibility Rules

- No `<g opacity="...">` (group opacity); set opacity on each child element individually
- Use overlay layers instead of image opacity
- Use inline styles only; external CSS and `@font-face` are prohibited

---

## X. Placeholder Specification

Templates use `{{PLACEHOLDER}}` format placeholders. Common placeholders:

| Placeholder        | Description        |
| ------------------ | ------------------ |
| `{{TITLE}}`        | Main title         |
| `{{SUBTITLE}}`     | Subtitle           |
| `{{AUTHOR}}`       | Organization name (Chinese) |
| `{{AUTHOR_EN}}`    | Organization name (English) |
| `{{PAGE_TITLE}}`   | Page title         |
| `{{CHAPTER_NUM}}`  | Chapter number     |
| `{{CHAPTER_TITLE}}` | Chapter title |
| `{{PAGE_NUM}}`     | Page number        |
| `{{DATE}}`         | Date               |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title |
| `{{TOC_ITEM_N_DESC}}`  | TOC item description |
| `{{THANK_YOU}}`    | Thank-you message  |
| `{{CONTACT_INFO}}` | Contact information |
| `{{CONTENT_AREA}}` | Content area placeholder |

---

## XI. Design Highlights

- **红色渐变主题**: 体现企业活力与专业性
- **金色点缀元素**: 增添品质感
- **圆角设计**: 现代、友好的视觉体验
- **清晰的信息层级**: 确保高效的信息传递
- **灵活的内容布局**: 适应多种商务场景
