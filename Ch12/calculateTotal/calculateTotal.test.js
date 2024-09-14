// 引入 Jest 的測試功能
const { calculateTotal } = require('./calculateTotal'); // 根據實際檔案位置調整路徑

// 定義範例購物車資料
const shoppingCart = [
    { name: 'Laptop', price: 1000 },
    { name: 'Phone', price: 600 },
    { name: 'Headphones', price: 200 }
];

describe('calculateTotal function', () => {

    // 測試情境 1: 沒填寫折扣率時，應套用預設的折扣
    test('應使用預設的折扣並正確計算價格', () => {
        const result = calculateTotal(shoppingCart);
        
        // 預設折扣為 0.1 (10%)
        expect(result.originalTotal).toBe(1800); // 原價總額應為 1800
        expect(result.discountedTotal).toBe(1620); // 折扣後總額應為 1620
        expect(result.savings).toBe(180); // 節省金額應為 180
    });

    // 測試情境 2: 將折扣率設為 0.3 時，應套用設定的折扣
    test('應使用自訂折扣率並正確計算價格', () => {
        const result = calculateTotal(shoppingCart, 0.3);
        
        // 設定折扣為 0.3 (30%)
        expect(result.originalTotal).toBe(1800); // 原價總額應為 1800
        expect(result.discountedTotal).toBe(1260); // 折扣後總額應為 1260
        expect(result.savings).toBe(540); // 節省金額應為 540
    });

    // 測試情境 3: 購物車為空時應能正常運行
    test('當購物車為空時應返回 0 的計算結果', () => {
        const result = calculateTotal([]);
        
        expect(result.originalTotal).toBe(0); // 原價總額應為 0
        expect(result.discountedTotal).toBe(0); // 折扣後總額應為 0
        expect(result.savings).toBe(0); // 節省金額應為 0
    });
});
