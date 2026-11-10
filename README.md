# 中文 ROMs 名称对照

中文游戏（汉化版 / 国产原创 / 改版）与 No-Intro 原版名称的对照数据，供 Super Retroid 等模拟器前端作为内置刮削来源。

## 内容

| 层 | 条数 | 说明 |
|---|---:|---|
| `verified` | 910 | 「确定」层：CRC 或游戏码硬命中，可机器复核 |
| `self` | 518 | 自建条目：国产原创、No-Intro 未收录的中文游戏（含标题画面） |

**「较确定」层（约 1,900 条）尚未收录**——其规则仍在收敛，抽检错误率未降到 2% 以下。

## 结构

```
index.json                      总索引（带版本号与每条内容哈希）
entries/<platform>/<id>.json    单条条目
assets/<platform>/<id>/title.png 标题画面（仅 self 层）
schema/entry.schema.json        条目格式
SCHEMA.md                       字段说明
REVIEWS.md                      尚未定论的争议条目（不入库）
```

## 使用方式

1. 拉 `index.json`，按 `crc32` 建索引。
2. 匹配顺序：No-Intro → 本库 → 占位图。
3. 素材缺失时显示占位，**不得借用其他游戏素材**。
4. 按发布标签经 jsDelivr 读取，例如
   `https://cdn.jsdelivr.net/gh/rintenbro/chinese-rom-names@v0.1.0/index.json`

## 不包含

- ROM 文件与任何下载链接
- 官方盒封、卡带扫描、宣传图
- 任何凭据

## 许可

数据部分 [CC BY 4.0](LICENSE)。素材版权归各自权利人，见 [NOTICE.md](NOTICE.md)。
