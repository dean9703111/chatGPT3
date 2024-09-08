# Ch15 用偽代碼要求 ChatGPT 幫我們做一連串的任務

### 15.2 使用偽代碼來提升 ChatGPT 的翻譯能力

摘錄 NVIDIA 創辦人黃仁勳在台大演講的一個片段
```
AI will create new jobs that didn't exist before
Forty years after the computer industry created the home PC, we invented artificial intelligence. Like software that automatically drives a car, or studies x-ray images, AI software has opened the door for computers to automate tasks for the world's largest, multi-trillion dollars of industries.
Healthcare, financial services, transportation, and manufacturing. AI has opened immense opportunities.
Agile companies will take advantage of AI, and boost their position.  Companies less so, will perish. Entrepreneurs, many of them here today, will start new companies.
And like in every computing era before, create new industries.  AI will create new jobs that didn't exist before. Like data engineering, prompt engineering, AI factory operations, and AI safety engineers.
```

- 普通版本
    ```
    請幫翻譯成中文。[貼上演講稿]
    ```
- 偽代碼版本
    ```
    ## 以下是**偽代碼 Prompt**，請依照其語意一步一步地來執行，不該有遺漏
    ## 使用繁體中文回覆

    text = "(貼上演講稿)"
    roles = ["專業的翻譯", "專業的文字編輯", "擅長文字表達的作家"]
    prompts = ["將英文翻譯成中文", "根據台灣的中文用字習慣給出改進建議", "優化成吸引讀者的文字"]
    def translate_process(role, prompt, lyrics):
        final_prompt = "請扮演{role}，閱讀完：{text} 後，執行：{prompt}"
        new_text = 執行(final_prompt)
        print(new_text)
        return new_text

    for role, prompt in zip(roles, prompts):
        text = translate_process(role, prompt, text)
    ```

### 15.4 使用偽代碼生成符合部落格主題的封面

```
## 以下是**偽代碼 Prompt**，請依照其語意一步一步地來執行，不該有遺漏
## 停用代碼解釋器，但開啟上網瀏覽搜尋以及Dalle功能
## 使用繁體中文回覆

topic= "(部落個主題)"
image_prompts= [請根據 topic 產生 10 個不同的封面描述。]
print(image_prompts)

def image_generation(image_prompt):
    final_prompt="使用英文撰寫 prompt，並根據{image_prompt}補充色調、背景描述、具體風格、畫面細節，請至少放 3 個效果詞(光照效果、色彩色調、渲染效果、視覺風格)和 1 個以上的構圖技巧，以構成完整的 final_prompt，並且不要有文字出現在圖中。"
    請根據以下引數內容{size="1792x1024", prompt=final_prompt}來調用內部工具 Dalle 以生成並展示圖片

## 這不是個 python 任務，一定要循環遍歷每個 image_prompt 並生成圖片
for image_prompt in image_prompts:
    image_generation(image_prompt)
```

### 參考資源：
1.	[GPT-4o偽代碼繪本生成術](https://www.youtube.com/watch?v=3rb-54Q5fig)
