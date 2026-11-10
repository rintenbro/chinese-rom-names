# 接入指南（给 Super Retroid 客户端）

本仓库作为「内置刮削来源」的 L2 层：No-Intro 查不到的游戏，到这里查。

## 1. 拉索引

```
GET https://cdn.jsdelivr.net/gh/rintenbro/chinese-rom-names@v0.1.1/index.json
```

- 固定标签（`@v0.1.1`）而不是 `@main`，避免内容随提交变化。
- 索引约 500 KB，建议启动时拉取并缓存；带 `If-None-Match` 判 304。
- 记录 `version` 字段，版本变化时重建本地索引。

## 2. 建索引

`index.json` 每条含 `id / layer / platform / group / titles / crc32[] / assets / hash`。

建两张表：

- `crc → entry`（主键，最快）
- `platform + 规范化中文名 → entry`（兜底，用于 CRC 不匹配时）

## 3. 匹配顺序

1. **No-Intro**（已有流程）命中 → 用官方素材源，结束。
2. 计算文件 CRC32（大写）→ 查本库 `crc` 表；命中即用。
3. 未命中 → 用 `platform + 文件名去扩展名` 或中文名查 `titles.zh-Hans`（模糊匹配需人工确认）。
4. 仍未命中 → 占位图。

注意：`layer=verified` 的条目描述的是**汉化版与原版的对应关系**，素材仍走 No-Intro 源；
`layer=self` 的条目才是本库自带素材（`assets.title`）。

## 4. 素材

- `assets.title` 为仓库内相对路径，拼接
  `https://cdn.jsdelivr.net/gh/rintenbro/chinese-rom-names@v0.1.1/<path>` 即可。
- 懒加载 + 本地缓存（建议按 `id` 存，带 `hash` 做失效判断）。
- 缺图（`null`）显示占位，**不要回退到其他游戏的素材**。

## 5. 更新

- 新版本发布新标签（v0.1.x），客户端可定期检查最新标签。
- 索引里的 `hash` 是条目 JSON 的 sha256 前 16 位，可用于增量校验。

## 6. 离线

- 首次联网拉完索引与所需素材后，可完全离线使用。
- 建议缓存上限按 50 MB 估算（全部素材约 36 MB）。
