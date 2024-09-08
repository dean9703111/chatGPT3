// 引入必要的套件
const express = require('express');  // Express 用來建立 Web 伺服器
const { Client } = require('@line/bot-sdk');  // LINE SDK 用來與 LINE API 互動
const OpenAI = require('openai');  // OpenAI SDK 用來與 OpenAI 互動
require('dotenv').config();  // dotenv 用來載入環境變數

// 建立 Express 應用程式
const app = express();
const port = process.env.PORT || 3000;  // 設定伺服器監聽的埠號，優先使用環境變數 PORT，否則使用 3000

// 設定 LINE Bot 的配置
const lineConfig = {
  channelAccessToken: process.env.LINE_CHANNEL_ACCESS_TOKEN,  // 從環境變數中讀取 LINE 的 Channel Access Token
  channelSecret: process.env.LINE_CHANNEL_SECRET,  // 從環境變數中讀取 LINE 的 Channel Secret
};
const lineClient = new Client(lineConfig);  // 建立一個 LINE 客戶端，稍後用來回應用戶訊息

// 設定 OpenAI 的配置
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,  // 從環境變數中讀取 OpenAI 的 API Key
});

// 設置 Webhook 路徑，讓 LINE 傳來的訊息可以被接收和處理
app.post('/webhook', express.json(), (req, res) => {
  const events = req.body.events;  // 取得來自 LINE 的事件，通常是用戶發送的訊息

  // 遍歷每個事件，處理來自用戶的訊息
  events.forEach(async (event) => {
    if (event.type === 'message' && event.message.type === 'text') {
      // 檢查事件類型是否為訊息，且訊息類型是否為文字
      try {
        // 使用 OpenAI API 來生成 AI 回應
        const chatCompletion = await openai.chat.completions.create({
          messages: [{ role: 'user', content: event.message.text }],  // 將用戶的訊息發送給 OpenAI
          model: 'gpt-3.5-turbo',  // 使用 OpenAI 的 GPT-3.5 模型來生成回應
        });

        // 將 AI 的回應發送回給用戶
        await lineClient.replyMessage(event.replyToken, {
          type: 'text',
          text: chatCompletion.choices[0].message.content,  // 將 AI 生成的回應內容回傳給 LINE 用戶
        });
      } catch (error) {
        // 處理可能發生的錯誤，例如 OpenAI API 請求失敗
        console.error('Error with OpenAI API:', error);
      }
    }
  });

  // 回應 200 狀態碼給 LINE 伺服器，表示請求已成功處理
  res.sendStatus(200);
});

// 啟動 Express 伺服器，並讓伺服器開始監聽指定的埠號
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
