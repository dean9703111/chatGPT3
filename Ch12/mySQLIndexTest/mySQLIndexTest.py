import pymysql
import random
import time
from faker import Faker
import logging

# 設定 log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 生成虛擬資料的 Faker
faker = Faker()

# 連接 MySQL 資料庫
def connect_db():
    return pymysql.connect(
        host='localhost',
        user='your_username',  # 替換成你的 MySQL 使用者名稱
        password='your_password',  # 替換成你的 MySQL 密碼
        db='your_database',  # 替換成你的資料庫名稱
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# 建立 users 表
def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("""
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                gender ENUM('Male', 'Female') NOT NULL
            )
        """)
    connection.commit()

# 插入 30 萬筆測試資料
def insert_data(connection, num_records=300000):
    with connection.cursor() as cursor:
        logging.info("開始插入資料...")
        for _ in range(num_records):
            email = faker.email()
            name = faker.name()
            address = faker.address()
            gender = random.choice(['Male', 'Female'])
            cursor.execute("""
                INSERT INTO users (email, name, address, gender) 
                VALUES (%s, %s, %s, %s)
            """, (email, name, address, gender))
        connection.commit()
        logging.info(f"{num_records} 筆資料插入完成")

# 隨機選取 10 個 email 作為搜尋條件
def get_random_emails(connection, num_emails=10):
    with connection.cursor() as cursor:
        cursor.execute("SELECT email FROM users ORDER BY RAND() LIMIT %s", (num_emails,))
        result = cursor.fetchall()
        return [row['email'] for row in result]

# 根據 email 搜尋 name 和 gender
def search_by_email(connection, emails):
    with connection.cursor() as cursor:
        total_time = 0
        for email in emails:
            start_time = time.time()
            cursor.execute("SELECT name, gender FROM users WHERE email = %s", (email,))
            cursor.fetchone()
            total_time += (time.time() - start_time)
        avg_time = total_time / len(emails)
        return avg_time

# 執行主要邏輯
def main():
    connection = connect_db()
    
    try:
        # 建立表格並插入資料
        logging.info("建立資料表")
        create_table(connection)
        
        logging.info("插入測試資料")
        insert_data(connection)
        
        # 隨機選取 10 個 email
        emails = get_random_emails(connection)
        logging.info(f"隨機選取的 10 個 email: {emails}")
        
        # 不加索引的搜尋
        logging.info("不加索引的搜尋")
        avg_time_no_index = search_by_email(connection, emails)
        logging.info(f"不加索引的平均搜尋時間: {avg_time_no_index:.6f} 秒")
        
        # 加上 email 索引
        logging.info("建立索引")
        with connection.cursor() as cursor:
            cursor.execute("CREATE INDEX idx_email ON users(email)")
        connection.commit()

        # 加索引後的搜尋
        logging.info("加上索引的搜尋")
        avg_time_with_index = search_by_email(connection, emails)
        logging.info(f"加上索引的平均搜尋時間: {avg_time_with_index:.6f} 秒")
    
    finally:
        connection.close()

    # 結果輸出
    logging.info(f"搜尋效能比較：無索引: {avg_time_no_index:.6f} 秒, 有索引: {avg_time_with_index:.6f} 秒")

if __name__ == "__main__":
    main()
