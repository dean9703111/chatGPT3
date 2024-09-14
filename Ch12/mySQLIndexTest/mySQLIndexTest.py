import pymysql
import logging
import random
import time
from faker import Faker

# 設定 logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 建立虛擬資料生成器
fake = Faker()

# 連接 MySQL 資料庫
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='example',
    database='exampledb'
)

try:
    with connection.cursor() as cursor:
        # 清理舊的 users 表
        logging.info("Dropping old table if exists.")
        cursor.execute("DROP TABLE IF EXISTS users")
        connection.commit()

        # 建立新的 users 表
        logging.info("Creating new table 'users'.")
        cursor.execute("""
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                address VARCHAR(255),
                gender ENUM('M', 'F')
            )
        """)
        connection.commit()

        # 固定的 20 個名字
        names = ["Dean", "John", "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", 
                 "George", "Hannah", "Ivan", "Jane", "Kevin", "Laura", "Mike", "Nina", 
                 "Oscar", "Paula", "Quincy", "Rachel"]

        # 插入 30 萬筆測試資料
        logging.info("Inserting 300,000 records into 'users' table.")
        insert_query = """
            INSERT INTO users (name, email, address, gender)
            VALUES (%s, %s, %s, %s)
        """
        for _ in range(300000):
            name = random.choice(names)
            email = fake.email()
            address = fake.address()
            gender = random.choice(['M', 'F'])
            cursor.execute(insert_query, (name, email, address, gender))
        connection.commit()

        # 無 Index 情況下的搜尋效能
        logging.info("Running search query without index.")
        start_time = time.time()
        cursor.execute("EXPLAIN SELECT id, email, gender FROM users WHERE name = 'Dean'")
        result_no_index = cursor.fetchall()
        no_index_time = time.time() - start_time
        logging.info(f"Search without index took {no_index_time:.4f} seconds.")
        
        # 在 name 欄位上建立 Index
        logging.info("Creating index on 'name' column.")
        cursor.execute("CREATE INDEX idx_name ON users (name)")
        connection.commit()

        # 有 Index 情況下的搜尋效能
        logging.info("Running search query with index.")
        start_time = time.time()
        cursor.execute("EXPLAIN SELECT id, email, gender FROM users WHERE name = 'Dean'")
        result_with_index = cursor.fetchall()
        with_index_time = time.time() - start_time
        logging.info(f"Search with index took {with_index_time:.4f} seconds.")

        # 輸出 Explain 結果
        logging.info("EXPLAIN output without index:")
        for row in result_no_index:
            logging.info(row)

        logging.info("EXPLAIN output with index:")
        for row in result_with_index:
            logging.info(row)

finally:
    connection.close()
    logging.info("Database connection closed.")
