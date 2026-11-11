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

## 格式变更记录

### v0.2.0（2026-11-11）
- `layer` 字段改为 `status`，取值 `verified` / `probable` / `self`
- 平台目录与 `platform` 值统一：`famicom` → `nes`，`megadrive` → `md`
- 新增 `probable_original`：`probable` 条目的推荐原版，应用仅作候选，不自动套用
- 新增 `hack_group`：汉化组，与 `vendor`（厂商）分离
- `files` 允许只带 `crc32`（部分条目仅有 CRC，无实体文件），`size` 可为空

## 不包含

- ROM 文件与任何下载链接
- 官方盒封、卡带扫描、宣传图
- 任何凭据

## 许可

数据部分 [CC BY 4.0](LICENSE)。素材版权归各自权利人，见 [NOTICE.md](NOTICE.md)。

## 条目状态（status）

| 状态 | 含义 | 应用行为 |
|---|---|---|
| `verified` | 原版对照由 CRC 或游戏卡带码硬命中（`match: "crc" / "game_code"`） | 可直接采用 `original` |
| `probable` | 由名称、容量、题头等间接证据判定，未经硬命中 | 仅在「修正游戏匹配」窗口作为推荐候选，不自动套用；原版写在 `probable_original` |
| `self` | No-Intro 未收录的中文原创 / 改版 / 合卡 / 工具卡 | 只用于显示名字层信息，无原版对照 |

名字层字段（`titles.zh-Hans`、`vendor`、`hack_group`、`type`、`script`、`version`）描述的是文件本身，`verified` / `probable` / `self` 条目都会提供；原版层只有 `verified` 的 `original` 与 `probable` 的 `probable_original`。
