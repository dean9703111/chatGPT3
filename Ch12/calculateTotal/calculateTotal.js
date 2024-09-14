/**
 * 計算購物車中的商品總價、折扣後的價格及節省的金額。
 * @param {Array} items - 包含商品名稱與價格的陣列
 * @param {number} discountRate - 折扣率 (例如：0.1 代表 10% 折扣)
 * @returns {Object} 返回包含原價總額、折扣後總額與節省金額的物件
 */
function calculateTotal(items, discountRate = 0.1) {
    // 使用 reduce 來計算原價總額，避免手動累加
    const originalTotal = items.reduce((total, item) => total + item.price, 0);

    // 計算折扣後的總額
    const discountedTotal = originalTotal * (1 - discountRate);

    // 計算節省的金額
    const savings = originalTotal - discountedTotal;

    // 返回計算結果
    return {
        originalTotal,
        discountedTotal,
        savings
    };
}

module.exports = { calculateTotal };