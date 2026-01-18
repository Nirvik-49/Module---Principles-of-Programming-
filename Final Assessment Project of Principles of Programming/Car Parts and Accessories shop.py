import sqlite3 # To create, connect, and manage a ightweight SQL database (the file stock.db)
import csv  # Added for CSV file handling
import matplotlib.pyplot as plt # for data visualization

# Base Class : Stock Item 

class StockItem:
    # Shared category for all base stock items
    stockCategory = "Car accessories"

    def __init__(self, stockCode, quantity, price):
        self.__stockCode = stockCode
        self.__quantity = quantity
        self.__price = price

    # Getters for private attributes
    def getStockCode(self):
        return self.__stockCode

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price
    
    def getStockName(self):
        return "Unknown Stock Name"
    
    def getItemType(self):
        return "General Car Accessory"
    
    def getStockDescription(self):
        return "Unknown Stock Description"
    
    def getPriceWithoutVAT(self):
        return self.__price
    
    def getPriceWithVAT(self):
        return self.__price * 1.175 # Calculates 17.5 % VAT
    

    # Increase the number of stocks per unit
    def increaseStock(self, amount):
        """Validates and increments stock quantity."""
        try:
            amount = int(amount) # Type checking for increaseStock() and converts input to integer
        except (ValueError, TypeError):
            print("Error: Amount must be a whole number {integer}.")
            return
        
        if amount < 1:
            print("The error was: Increased item must be greater than or equal to one")
            return
        if amount > 100:
            print("The error was: Increase item must be less than or equal to 100")
            return
        self.__quantity = self.__quantity + amount
        self.save_to_db()

    # Sell stock method - can't sell more than available items
    def sellStock(self, amount):
        """Validates sales and triggers low-stock alerts"""
        try:
            amount = int(amount)
        except (ValueError, TypeError):
            print("Error: Amount must be a whole number (integer).")
            return
            
        if amount < 1:
            print("Error: Cannot sell less than 1 item.")
            return
            
        if amount > self.__quantity:
            print(f"Error: Only {self.__quantity} items in stock. Can't sell more {amount}.")
            return

        # Only reaches here if all checks passed
        self.__quantity = self.__quantity - amount
        self.save_to_db()
        print(f"Sold {amount} and Remaining quantity is {self.__quantity}")

        # Stock Threshold Alerts
        if self.__quantity <= 5:
                print("Restock your items is recommended. Low stock alert!")
        if self.__quantity <= 2:
                print("Stock items are critically low. Only a few units left!")
        if self.__quantity == 0:
                print("Items are unavailable. Out of stock! ")

    # Change the original price per unit to new price
    def setPrice(self, new_price):
        """Updates unit price with type validation"""
        try:
             new_price = float(new_price) # 99.99
        except (ValueError, TypeError):
            print("Error: Price must be a valid number (e.g. 99.99)")
            return
            
        # Check price for input validation
        if new_price < 0:
            print("Error: Price cannot be negative.")
            return
            
        self.__price = new_price
        self.save_to_db()
        print(f"Set new price {new_price:.2f} per unit")

    # Calculate price including 17.5% VAT
    def getVAT(self):
        return self.__price * 1.175
        

    # Base class items representation 
    def __str__(self):
        return (
            f"Stock Category: {self.stockCategory}\n"
            f"Stock Type: {self.getStockName()}\n"
            f"Description: {self.getStockDescription()}\n"
            f"StockCode: {self.getStockCode()}\n"
            f"PriceWithoutVat: {self.getPriceWithoutVAT():.2f}\n"
            f"PriceWithVAT: {self.getPriceWithVAT():.2f}\n"
            f"Total unit in stock: {self.getQuantity()}\n"
        )
             
    # database logic and functions
    @classmethod
    def create_table(cls):
        """Initializes the SQLite database table"""
        try:
            with sqlite3.connect("stock.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS stock_items (
                        stock_code TEXT PRIMARY KEY,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL,
                        category TEXT NOT NULL,
                        brand TEXT
                    )
                """)
                conn.commit()
                print("Database table ready.")
        except Exception as e:
            print("Error creating table:", e)

    def save_to_db(self):
        """Save or update this item in the database"""
        try:
            with sqlite3.connect("stock.db") as conn:
                cursor = conn.cursor()
                # Use NULL for brand if it's not a NavSys
                brand_value = getattr(self, "_NavSys__brand", None)

                cursor.execute("""
                    INSERT OR REPLACE INTO stock_items
                    (stock_code, quantity, price, category, brand)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    self.__stockCode,
                    self.__quantity,
                    self.__price,
                    self.stockCategory,
                    brand_value
                ))
                conn.commit()
                print(f"Saved the records {self.__stockCode} successfully")
        except Exception as e:
            print(f"Error saving the record {self.__stockCode}:{e}")
    
    @classmethod
    def load_from_db(cls, stockCode):
        """Load an item from database using stock code."""
        try:
            with sqlite3.connect("stock.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT quantity, price, category, brand
                    FROM stock_items
                    WHERE stock_code = ?
                """, (stockCode,))
                row = cursor.fetchone()
                if row:
                    quantity, price, category, brand = row
                    if brand is not None:
                        # NavSys item
                        item = NavSys(stockCode, quantity, price, brand)
                        return
                    else:
                        # Regular car accessories
                        item = StockItem(stockCode, quantity, price)
                        return item
                else:
                    print(f"No item found with code: {stockCode}")
                    return None
        except Exception as e:
            print("Error loading the item:", e)
            return None
        
    @classmethod
    def export_to_csv(cls, filename= "export.csv"):
        with sqlite3.connect("stock.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT stock_code, quantity, price, category, brand FROM stock_items")
            rows = cursor.fetchall()

        with open(filename, 'w') as f:
            f.write("Stock Code,Quantity,Price,Category,Brand\n")

            for row in rows:
                code, quantity, price, category, brand = row
                brand = brand or ""
                f.write(f"{code},{quantity},{price:.2f},{category},{brand}\n") 

        print(f"Exported to {filename}")

    @classmethod
    def plot_chart(cls):
        """Generates a bar chart comparing stock types"""
        try:
            with sqlite3.connect("stock.db") as conn:
                navigation_total = conn.execute("SELECT SUM(quantity) FROM stock_items WHERE brand IS NOT NULL").fetchone()[0] or 0
                other_total = conn.execute("SELECT SUM(quantity) FROM stock_items WHERE brand IS NULL").fetchone()[0] or 0

            plt.bar(['Navigation', 'Other'], [navigation_total, other_total])
            plt.title('Stock Inventory Levels')
            plt.ylabel('Quantity')
            plt.show()

            print("\nStock Levels Chart displayed.")
        except Exception as e:
            print("Plot Error:", e)

# Subclass - NavSys class to represent navsys brand
# Inherits from StockItem Class

class NavSys(StockItem):
    def __init__(self, stockCode, quantity, price, brand):
        super().__init__(stockCode, quantity, price)
        self.__brand = brand
    
    # Override methods for navigation system
    def getStockName(self):
        return "Navigation system"
    
    def getStockDescription(self):
        return "Geovision Sat Nav"
    
    def getItemType(self):
        return "Navigation system"
    
    # Sub-class items representation
    def __str__(self):
        base_info = super().__str__()
        return (
            f"{base_info}"
            f"Brand: {self.__brand}")
    

# Testing
if __name__ == "__main__":
    StockItem.create_table()

# Create and save items
print("\nStep 1 example run (Regular item)")
print("Creating a stock with 10 units Unknown item, price 99.99 each, and item code W101")
item = StockItem("W101", 10, 99.99)
item.save_to_db()
print("Printing item stock information:")
print(item)

# Increasing the stock items per unit
print("\nIncreasing 10 more units")
item.increaseStock(10)
print("Printing item stock information:")
print(item)

# Selling the stock items from the available quantity
item.sellStock(2)
print("Printing item stock information:")
print(item)

# Set or change the price of the item
print("\nSet new price 100.99 per unit")
item.setPrice(100.99)
print("Printing item stock information:")
print(item)

print("\nIncreasing 0 more units")
item.increaseStock(0)
print()

print("Creating additional regular item:")
item2 = StockItem("W102", 8, 12.50)
item2.save_to_db()

# Increasing the stock items per unit
print("\nIncreasing 10 more units")
item2.increaseStock(10)
print("Printing item stock information:")
print(item2)

# Selling the stock items
item2.sellStock(2)
print("Printing item stock information:")
print(item2)

# Set or change the price of the item
print("\nSet new price 100.99 per unit")
item2.setPrice(100.99)
print("Printing item stock information:")
print(item2)

print("\nIncreasing 0 more units")
item2.increaseStock(0)


print("\nStep 2 example run (NavSys item)")
print("Creating a stock with 10 units Navigation system, price 99.99, item code NS101, and brand TomTom")
navSys = NavSys("NS401", 10, 99.99, "TomTom")
print("Printing item stock information:")
print(navSys)


print("\nIncreasing 10 more units")
navSys.increaseStock(10)
print("Printing item stock information:")
print(navSys)

print("\nSold 2 units")
navSys.sellStock(2)
print("Printing item stock information:")
print(navSys)

print("\nSet new price 100.99 per unit")
navSys.setPrice(100.99)
print("Printing item stock information:")
print(navSys)

print("\nIncreasing 0 more units")
navSys.increaseStock(0) 
print()

print("Creating additional NavSys item:")
n403 = NavSys("N402", 3, 349.50, "Geomatic")
n403.save_to_db()
print()

items = [
StockItem("W103", 45, 29.99),
NavSys("N403", 12, 249.00, "Cyclo"),]   

for item in items:
    print(f"Code: {item.getStockCode()} and Type: {item.getItemType()}") # same method call but different answers depending on real object type
print()

# Input Validation for increaseStock(), setPrice(), and sellStock()

print("\nTesting invalid input in setPrice (string):")
item.setPrice("abc")  # should print an error message but program will no crash

print("\nTesting negative prices:")
item.setPrice(-20)  # should print an error

print("Testing invalid amount in increaseStock (string)")
item.increaseStock("ten") # should print an error

print("\nTesting sellStock with invalid type:")
item.sellStock("five")  # should print error, no crash, and no sell of items

print("\nTesting sellStock with the given amount which is more than available amount")
item.sellStock(1000)   # error message, no sell of items

print("\nSelling valid amount (should show alert message if low stock)")
item.sellStock(8)

# Data Visualization
print("Stock Levels Bar Chart")
StockItem.plot_chart()

# Export the records to CSV files
print("Exporting current inventory to CSV file")
StockItem.export_to_csv()



        





