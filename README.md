# addingRolesBot

## コマンド

- プレフィックス : `+`
  - `+help` : ヘルプを表示
  - `+role` : ロールを追加

## 例

いい例

✅ +role @ロール

```md
+role @にゃーん
```

✅ +role 絵文字 = @ロール, 絵文字 = @ロール, ...(複数個)

```md
+role 🥵 = @暑いの苦手, 🥶 = @寒いの苦手
```

✅ (任意のコメント) +role 絵文字 = @ロール, ...(複数個)

```md
オフ会来る人はリアクションしてね 😘
+role
🏖 = @オフ会泊まる, 🎡 = @オフ会泊まらない
```

悪い例

❌ +role @ロール, ...(複数個)

```md
+role @電車 @徒歩
```

❌ +role (関係ない文字) @ロール (関係ない文字)

```md
+role 🍣🌾 @ごはん食べたい 😋🍴
```

❌ +role (複数の絵文字) = @ロール

```md
+role 🥁🎺 = @音楽鑑賞, 🎪🤹‍♀️🎭 = @サーカス
```
