# Ch12 工程師用 ChatGPT 輔助開發的技巧

### 12.1 撰寫 Regex正則表達式

```
請幫我用 [JavaScript] 撰寫一段程式碼，用Regex來驗證輸入的字串是否符合如下規則[輸入的字串需要包含英文、數字、符號，且長度在 8 到 16 個字，不接受「？」這個字元。]
```

### 12.2 轉換程式語言

```
你是一個熟悉 [JavaScript、PHP] 程式語言的開發人員，你了解這兩個程式語言的語法特性，知道如何在保留功能的狀態下進行轉換。
請幫我將下面的程式從 [JavaScript] 轉換成 [PHP] 語言。
[貼上剛剛生成的 Regex 程式]
```

### 12.3 撰寫邏輯複雜、不熟悉的資料庫語法（MySQL、MongoDB）

#### 12.3.1	MySQL 應用範例

```
請幫我用 [MySQL] 撰寫一段 SQL 語法，我想要用姓名（users table -> user_name）找出某位使用者在過去三個月內（orders table -> create_at）購買了哪些產品（products -> name），並取得這些產品的有效日期（orders table -> product_cache.exp(json)）
資料庫關聯如下：
- users.id vs oreders.user_id
- products.id vs oreders.product_id
```

#### 12.3.2	MongoDB 應用範例

```
請幫我撰寫一段 [MongoDB] 的查詢語法，要根據 VIP 使用者的購買記錄（purchase_records.userType = VIP），統計 2023 年 4 月（purchase_records. purchaseDate） 3C 產品這個類別下（purchase_records. productCategory= 3C）最熱門的產品（purchase_records. productName），並按銷售數量（purchase_records. quantity）排序，取出前 10 名。
```

### 12.4 產生比較真實的假資料（Mock data）

- 產品資訊
    ```
    請幫我產生 [10] 個 [寵物產品] 的資訊，請以現實生活中常見的來做舉例，參考下方格式，並在 [array] 中呈現。 
    { 
        "name": "貓抓板", 
        "price": 800, 
        "description": "您的貓咪需要的不僅僅是一塊抓板，更是一份對環境的守護。我們的貓抓板選用了100%可再生環保材質，讓您在滿足貓咪天性的同時，也能為地球盡一份心力。" 
    }
    ```
- 使用者資訊
    ```
    請幫我產生 [10] 個 [使用者] 的資訊，請以現實生活中常見的名字來做舉例，參考下方格式，並在 [array] 中呈現。 
    { 
        "name": "大黑寶", 
        "age": 18, 
        "gender": "male", 
        "email": "baobaoverycute@baby.com",
        "hobby": "free diving, traveling, workout"
    }
    ```

### 12.5 重構程式（Refactoring）

```
請扮演擅長開發 [JavaScript] 的工程師，你非常注重程式的 [複用性、穩定性、易讀性、演算法、變數與函式命名] 等細節，並會透過註解幫助別人了解你的程式；請幫我重構下面的程式，並告訴我你優化了哪些細節。

function calculate(items) {
    let originalTotal = 0;
    let discount = 0.1;
 
    for (let i = 0; i < items.length; i++) {
        originalTotal += items[i].price;
    }
 
    let discountedTotal = originalTotal * (1 - discount);
    let savings = originalTotal - discountedTotal;
 
    return {
        originalTotal: originalTotal,
        discountedTotal: discountedTotal,
        savings: savings
    };
}
 
let shoppingCart = [
    { name: 'Laptop', price: 1000 },
    { name: 'Phone', price: 600 },
    { name: 'Headphones', price: 200 }
];
 
let result = calculate(shoppingCart);
 
console.log("Original Total Price:", result.originalTotal);
console.log("Discounted Total Price:", result.discountedTotal);
console.log("Total Savings:", result.savings);
```

### 12.6 撰寫單元測試（Unit Test）

```
請扮演擅長撰寫 [JavaScript] 單元測試的工程師，請你使用 [Jest] 這個測試框架來確保下面程式的執行結果符合預期，情境如下：
1. 沒填寫折扣率時，應套用預設的折扣，並正確計算原價總額、折扣後總額與節省金額 
2. 將折扣率設為 0.3 時，有套用設定的折扣，並正確計算原價總額、折扣後總額與節省金額 
3. 若購物車為空，也可以正常運行 若有我沒考量到的情境，請幫我補上，謝謝。
[貼上剛剛重構後的程式]
```

### 12.7 程式語言、框架升級的好幫手

#### 12.7.1	請 ChatGPT 分析 PHP 從 5.6 升級到 8.3 要面對的問題

```
我正在將一個專案從 [PHP 5.6] 升級到 [PHP 8.3]，請問在此過程中需要注意哪些[函式差異、已廢棄的函式，以及有可能會導致的相容性問題]？
如果有可能，請提供具體的函式列表，並附上每個函式的變更原因和替代方案。
```

#### 12.7.2	請 ChatGPT 幫我們升級程式內容

```
你是一位非常細心的 PHP 資深工程師，請幫我將下面 [PHP 5.6] 的程式重構升級成可以在 [PHP 8.3] 順利運行的版本，請考量兼容性的問題，並說明你改動了哪些地方。
<?php
 
function processArray($array) {
    $result = [];
 
    while (list($key, $value) = each($array)) {
        $intValue = intval($value);
        $result[] = $intValue;
    }
 
    $resultString = implode($result, ", ");
 
    return $resultString;
}
 
$inputArray = ["10.5", "20", "30.7", "40", "50"];
echo processArray($inputArray); // 輸出：10, 20, 30, 40, 50
 
?>
```

### 12.8 撰寫驗證效能的程式

```
請扮演擅長 [Python] 的後端工程師，你是 [MySQL] 資料庫的專家。
請按照下面的需求寫一段比較 MySQL 有 index 與沒有 Index 對搜尋效能的影響的程式：
1. 需要建立 [30] 萬筆的測試資料
2. Table 為 users，Columns 有 id, email, name ,address, gender 等資訊
3. 我們會以「name」作為搜尋條件，要回傳「id, email, geander」的資訊
4. email, address, gender 請使用相關接近真實的虛擬資料
5. name 用 20 個固定的名字儲存在陣列即可，要包含「Dean」，這是資料庫要搜尋的 Where 條件
6. 最後使用 Explain 來輸出兩者的結果、執行所需時間
7. 任務開始前會先 Drop 掉 Table 確保資料乾淨
8. 建議使用 pymysql 套件
9. 搭配適當的註解讓我們了解執行過程
10. 在執行過程中加上 log 讓我們知道執行到哪個環節
```