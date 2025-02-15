CREATE TABLE IF NOT EXISTS books
(
    book_id VARCHAR(100) UNIQUE NOT NULL,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    quantity INT NOT NULL
);
CREATE TABLE IF NOT EXISTS issue
(
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    book_id VARCHAR(100) NOT NULL,
    issue_date VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS submit
(
    submit_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    book_id VARCHAR(100) NOT NULL,
    submit_date VARCHAR(100)
)