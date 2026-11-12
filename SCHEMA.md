# 条目字段说明（送审版）

一条记录 = 一个 ROM 文件与它的中文名/原版名的对应关系。

## 顶层字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | ✓ | `ver-<平台>-<crc32小写>`（verified）或 `cn-<hash12>`（self），稳定不变 |
| `layer` | enum | ✓ | `verified`（CRC/游戏码硬命中）或 `self`（自建条目） |
| `platform` | enum | ✓ | `nes` / `sfc` / `gb` / `gbc` / `gba` / `nds` / `md` |
| `group` | string | ✓ | 作品组：同一作品的多个汉化版本共用一个组名（取原版名去掉地区/版本后缀，自建条目取中文名） |
| `titles` | object | ✓ | `zh-Hans`（中文名）、`en`（verified 层为 No-Intro 标准名）、可选 `zh-Hant` |
| `vendor` | string | | 汉化组，多个用 ` / ` 分隔 |
| `version` | string | | 汉化版本号（如 `v1.2`、`修正版`） |
| `script` | enum | | `简` / `繁` / `简繁` / 空 |
| `files` | array | ✓ | 每条含 `name`（原始文件名）、`crc32`（大写 8 位）、`size`（字节） |
| `original` | object/null | | verified 层必填：`no_intro_name`、`region`、`crc32`、`size`；self 层为 null |
| `type` | enum | self 层必填 | `original`（国产原创）/ `hack`（改版、合卡、学习卡） |
| `match` | enum | verified 层必填 | `crc`（整文件 CRC）/ `game_code`（卡带头游戏码）/ `version`（dat 版本号+容量，仅个别条目） |
| `serial` | string | | 游戏码（GBA/NDS 如 `ASRJ`），`match=game_code` 时给出 |
| `source` | enum | ✓ | `no-intro` / `community` |
| `assets` | object | | `title` / `box` / `snap[]`，缺省为 null/空数组 |

## index.json

| 字段 | 说明 |
|---|---|
| `version` | 仓库数据版本（与发布标签一致，如 `0.1.0`） |
| `generated_at` | 生成时间（ISO 8601） |
| `count` / `counts` | 总条数与分层计数 |
| `entries[]` | 每条：`id` / `layer` / `platform` / `group` / `titles` / `crc32[]` / `assets` / `hash`（条目 JSON 的 sha256 前 16 位） |

## 约定

- CRC32 一律大写、无 `0x` 前缀。
- 同一条目只对应一个 ROM；同一 ROM 出现在多条属错误（CI 校验）。
- `verified` 层的标准名必须存在于对应平台的 No-Intro dat（CI 校验）。
- 缺素材允许为空，App 回退占位，禁止借用其他游戏素材。

## asset_sources（v0.2.1）

素材来源，与 `assets` 一一对应：

```json
"asset_sources": {
  "box": {
    "type": "ai-generated",
    "model": "MiniMax-H3-Image",
    "date": "2026-11-12",
    "based_on": ["标题画面", "游戏截图"]
  }
}
```

- `type`：`ai-generated`（AI 依据游戏画面绘制的新插画）、`official`、`scan`、`screenshot`
- `based_on`：生成时参考的画面类型
- AI 封面**不是官方包装图**，应用若展示需标注为「AI 插画」
