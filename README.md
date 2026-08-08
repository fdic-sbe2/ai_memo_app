# ai_memo_app

## このリポジトリのルール
```
main
  ▲
  │　@kaitoakamatsuがマージ
  │
dev
  ▲
  │　各メンバーが PR
  │
├── feature/a
├── feature/b
└── feature/c
```

## コードを編集する方法
### 操作方法、用語が分からなかったら、この画面をGeminiに貼って解説してもらってください。
0. Windows Terminalを開く
1. リポジトリをパソコンにダウンロードする  
```git clone https://github.com/fdic-sbe2/ai_memo_app.git```
2. リポジトリに移動する  
```cd  ai_memo_app```
3. 現在いるブランチを確認  
```git branch```
4. `dev`ブランチに切替  
```git switch dev```
5. 新しいブランチを切って、切替  
〇〇=機能名を短い英語で  
```git switch -c feature/〇〇```
6. 現在いるブランチを確認  
  feature/〇〇になってる?  
```git branch```
7. VSCodeで好きに編集しよう  
 ```code .```  
終わったらこの画面に戻ってくる 
8. ステージングする  
```git add -A```
9. コミットする  
xx=変更点を簡潔に説明する  
```git commit -m "xx"```
10. githubにブランチをアップロードする  
```git push -u origin feature/〇〇```