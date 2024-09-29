# Ch11 新手如何用 ChatGPT 學寫程式（以LINE Bot 串接OpenAI為例）

### 11.2 詢問可以使用什麼技術達成

```
我是一個完全沒寫過程式的新手，想要開發一個 LINE Bot 串接OpenAI 的專案，請問可以使用什麼技術達成呢？
```

### 11.3 將大步驟拆分成小步驟（以安裝環境舉例）

```
我想使用 [Node.js] 來開發這個專案，目前使用的電腦作業系統為 [macOS]，請考量到日後版本升級等議題後，一步步告訴我要如何安裝開發環境、設定專案，並確認環境可以使用嗎？
```

- 步驟 1：安裝 Node.js 版本管理工具 (NVM)
    - 安裝 NVM: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash`
    - 檢查 NVM 是否正確安裝: `nvm --version`
- 步驟 2：安裝 Node.js
    - 安裝最新的穩定版 Node.js: `nvm install --lts`
    - 設定默認使用此版本: `nvm alias default node`
    - 驗證安裝是否成功：`node --version`、`npm --version`
- 步驟 3：安裝開發工具
    - 安裝 Visual Studio Code：https://code.visualstudio.com/
- 步驟 4：設定專案
    ```
    mkdir line-bot-project
    cd line-bot-project
    npm init -y
    ```
- 步驟 5：安裝必要的套件
    - 安裝 Express.js（用來建立 Web 伺服器）和 LINE Messaging API 的套件：`npm install express line-bot-sdk openai dotenv`
- 步驟 6：編寫基本的 LINE Bot 代碼
    ```js
    const express = require('express');
    const { Client } = require('@line/bot-sdk');
    const { Configuration, OpenAIApi } = require('openai');
    require('dotenv').config();

    const app = express();
    const port = process.env.PORT || 3000;

    const lineConfig = {
    channelAccessToken: process.env.LINE_CHANNEL_ACCESS_TOKEN,
    channelSecret: process.env.LINE_CHANNEL_SECRET
    };

    const client = new Client(lineConfig);

    const openaiConfig = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
    });
    const openai = new OpenAIApi(openaiConfig);

    app.post('/webhook', express.json(), (req, res) => {
    const events = req.body.events;

    // 處理每個來自 LINE 的事件
    events.forEach(async (event) => {
        if (event.type === 'message' && event.message.type === 'text') {
        const response = await openai.createChatCompletion({
            model: 'text-davinci-003',
            messages: [{ role: 'user', content: event.message.text }],
        });

        client.replyMessage(event.replyToken, {
            type: 'text',
            text: response.data.choices[0].message.content,
        });
        }
    });

    res.sendStatus(200);
    });

    app.listen(port, () => {
    console.log(`Listening on port ${port}`);
    });
    ```
- 步驟 7：設定環境變數，在專案根目錄下創建「.env」檔案
    ```env
    LINE_CHANNEL_ACCESS_TOKEN=你的LINE_CHANNEL_ACCESS_TOKEN
    LINE_CHANNEL_SECRET=你的LINE_CHANNEL_SECRET
    OPENAI_API_KEY=你的OPENAI_API_KEY
    ```
- 步驟 8：測試專案
    - 在本地運行你的專案：`node index.js`


### 11.4 如何解決遇到的問題（Debug）


#### 11.4.1	ChatGPT 可能會使用到過時套件

把錯誤訊息貼給 ChatGPT，向他詢問要如何解決:
```
執行步驟 8，輸入「node index.js」出現如下錯誤，請問我要如何處理呢？
Error: Cannot find module '@line/bot-sdk'
```

- 步驟 1：確認你已經安裝 @line/bot-sdk
    - 運行以下命令來安裝 @line/bot-sdk：`npm install @line/bot-sdk`
- 步驟 3：再次運行程式
    - 安裝完成後，重新運行以下命令：`node index.js`

#### 11.4.2	ChatGPT使用套件的方式可能有錯

```
安裝完 @line/bot-sdk 後，重新執行程式時遇到了新的錯誤訊息，請問如何解決？
const openaiConfig = new Configuration({
TypeError: Configuration is not a constructor
```

將官網範例複製起來，向 ChatGPT 詢問如何修改程式：
```js
我在 openai 官網看到的範例程式如下，是否使用上有所差異呢？可以幫我整合到原有程式中嗎？

import OpenAI from 'openai';
 
const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});
 
async function main() {
  const chatCompletion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'Say this is a test' }],
    model: 'gpt-3.5-turbo',
  });
}
 
main();
```

### 11.5 逐步完成後續任務

#### 11.5.1	了解 LINE Bot 基本概念

```
關於[2. 了解 LINE Bot 基本概念]這塊，可以給予我詳細的操作步驟嗎？
```

#### 11.5.2	使用 Webhook 來處理用戶請求

```
我目前在本地開發，關於 [3. 使用 Webhook 來處理用戶請求] 這塊，想使用前面提到的 ngrok 來將本地伺服器公開到網際網路上，以便接收 LINE 的訊息。
請問如何完成這些任務呢？請告訴我詳細的操作步驟。
```

- 步驟 1：安裝 ngrok
    - 進入 ngrok 官方網站：https://ngrok.com/，並註冊一個免費帳戶
    - 執行以下命令來確認 ngrok 是否安裝成功: `ngrok --version`
- 步驟 2：啟動 Node.js 專案
    - 啟動 Node.js：`node index.js`
- 步驟 3：使用 ngrok 將本地伺服器公開到網際網路上
    - 啟動 ngrok：`ngrok http 3000`
- 步驟 4：設定 Webhook URL
    - 前往 LINE Developers：https://developers.line.biz/

#### 11.5.3	串接 OpenAI API

```
目前已經完成 LINE Bot 的 Webhook 設定，關於 [4. 串接 OpenAI API] 這塊，接下來如何使用 [Node.js]來完成這個任務呢？請告訴我詳細的操作步驟。
```

- 步驟 1：註冊 OpenAI 帳戶並獲取 API Key
    - OpenAI 官方網站： https://beta.openai.com/signup/
    - 進入 API Keys 頁面 https://beta.openai.com/account/api-keys，點擊「Create new secret key」來生成一個 API Key
- 步驟 2：設定專案環境變數
    - 在專案根目錄創建 .env 檔案，並添加 OpenAI API Key 與 LINE 的相關資訊
        ```env
        LINE_CHANNEL_ACCESS_TOKEN=你的LINE_CHANNEL_ACCESS_TOKEN
        LINE_CHANNEL_SECRET=你的LINE_CHANNEL_SECRET
        OPENAI_API_KEY=你的OPENAI_API_KEY
        ```
- 步驟 3：安裝 OpenAI SDK: `npm install openai`

### 11.6 根據自己的程度解釋程式、加上註解

```
我是 Node.js 程式的[新手]，雖然專案可以順利執行，但我看不太懂程式是如何運作的，請仔細向我說明每個元件扮演的角色，並加上中文註解讓我了解哪些邏輯是可以調整的。
```

### 11.7 補充：關於 OpenAI 你應該要知道的事

錯誤訊息可以參考網址：https://platform.openai.com/docs/guides/error-codes/api-errors 

不同模型（Model）的價格不同，細節請參考網址：https://openai.com/api/pricing/

估算文字與 Token 的對應關係的網址：https://platform.openai.com/tokenizer

### 參考資料：
1.	[最終版 LINE Bot 串接OpenAI 程式](https://github.com/dean9703111/chatGPT3/tree/master/Ch11)
2.	[與 ChatGPT 的完整對話](https://chatgpt.com/share/519904f5-f501-43a4-b942-26d8408d77f4)

