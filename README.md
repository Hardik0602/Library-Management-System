# Library Management System – A Digital Book Management Solution

A Python-based console application designed to manage library operations including book inventory, issuing, returning, and tracking with MySQL database integration.

## Features

- 📚 Book inventory management (Add/Remove/View books)
- 📖 Book issuing system with user tracking
- 📝 Book return/submission system
- 📊 Automatic quantity management
- 🗄️ MySQL database integration for data persistence
- 📅 Date tracking for issue and return operations
- 🖥️ Interactive console-based interface
- 🔍 Real-time book availability checking

## Tech Stack

- **Python** - Core programming language
- **MySQL** - Database management system
- **mysql-connector-python** - Database connectivity
- **datetime** - Date operations for tracking

## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.6 or higher
- MySQL Server
- MySQL Workbench (optional, for database management)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Hardik0602/Library-Management-System.git
cd Library-Management-System
```

### Step 2: Install Required Dependencies

```bash
pip install mysql-connector-python
```

### Step 3: Database Setup

1. **Create MySQL Database:**
   ```sql
   CREATE DATABASE database_name;
   USE database_name;
   ```

2. **Run the Database Schema:**
   ```bash
   mysql -u your_username -p database_name < tables.sql
   ```
   
   Or manually execute the SQL commands from `tables.sql` file in your MySQL client.

### Step 4: Configure Database Connection

Update the database configuration in the Python file:
```python
db = mysql.connector.connect(
    host="localhost",      # Your MySQL host
    user="your_username",  # Your MySQL username
    password="your_password", # Your MySQL password
    database="database_name"      # Your database name
)
```

### Step 5: Run the Application

```bash
python library_management.py
```

## How to Use

### Main Menu Options

1. **Add Book** - Add new books to the library inventory
2. **Show Books** - Display all available books with quantities
3. **Remove Book** - Delete books from the inventory
4. **Issue Book** - Issue books to users (decreases quantity)
5. **Submit Book** - Return books from users (increases quantity)
6. **Exit** - Close the application

## Database Schema

### Books Table
- `book_id` - Unique book identifier (VARCHAR(100))
- `title` - Book title (VARCHAR(100))
- `author` - Book author (VARCHAR(100))
- `quantity` - Available quantity (INT)

### Issue Table
- `issue_id` - Auto-increment primary key
- `name` - User name who issued the book (VARCHAR(100))
- `book_id` - Book identifier (VARCHAR(100))
- `issue_date` - Date when book was issued (VARCHAR(100))

### Submit Table
- `submit_id` - Auto-increment primary key
- `name` - User name who returned the book (VARCHAR(100))
- `book_id` - Book identifier (VARCHAR(100))
- `submit_date` - Date when book was returned (VARCHAR(100))

## Dependencies

```python
mysql-connector-python==8.0.33
```

## Key Features Implementation

### Book Management
- Add new books with unique IDs
- Remove books from inventory
- Real-time quantity tracking
- Duplicate book ID prevention

### Transaction Management
- Issue books with automatic quantity reduction
- Return books with automatic quantity increment
- Date tracking for all transactions
- User identification for each transaction

### Database Operations
- CRUD operations for book management
- Transaction logging
- Data persistence and integrity
- Efficient query execution

## Error Handling

- Database connection error management
- Invalid input validation
- Duplicate book ID handling
- Quantity availability checking
- Menu option validation
  
## Limitations

- Console-only interface
- Basic user authentication (name-based)
- No fine calculation for late returns
- Single-session operation
- No book search functionality

## Future Enhancements

- GUI interface using Tkinter
- User authentication and role management
- Advanced search and filter options
- Fine calculation system
- Book reservation system
- Report generation
