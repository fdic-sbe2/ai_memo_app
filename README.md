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
### 以下の内容を「理解できないな」と感じた時
- 操作方法、用語が分からなかったら、この画面をGeminiに貼って解説してもらってください
- 事前に以下の動画を見るとわかりやすいと思います
  - [【初心者でもわかる！】Gitの使い方講座](https://www.youtube.com/watch?v=cyOTQzI2AFU)
  - [【初心者プログラマ必見】しっかりマスターできる「GitHubの使い方講座」](https://www.youtube.com/watch?v=ZEc0PFPm7Pk)
### 操作方法
- Git/VSCodeをインストール済みとして解説します
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
例)
    ```
    ログイン機能を追加する
    git switch -c feature/login
    ```
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
10. Githubにブランチをアップロードする  
```git push -u origin feature/〇〇```
11. Pull Requestを作成
    1. [Github](https://github.com/fdic-sbe2/ai_memo_app)に移動
    2. 緑色のボタン`Compare & pull request`をクリック
    3. `Add a title`に、編集内容を短くまとめたタイトルを入力
    4. `Add a description`に詳しく、簡潔に、箇条書きで、編集内容の説明を書く
    6. 右側`Reviewers`に[@kaitoakamatsu](https://github.com/kaitoakamatsu)、[@kmakoo251266-maker](https://github.com/kmakoo251266-maker)を入れる
    7. 緑色のボタン`Create pull request`を押す
12. Pull Requestがレビューされ、承認・マージされたとき([@kaitoakamatsu](https://github.com/kaitoakamatsu)がLINEか何か送ります...)
13. `dev`ブランチに切替、現状を更新、作業していたローカルブランチを削除
    ```
    git switch dev
    git fetch -p
    git pull
    git branch -d feature/〇〇
    ```
14. 別の機能を作る場合...  
`5.`から始める