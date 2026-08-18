# Hotel Management System

A desktop application built with Python that simplifies hotel operations, room bookings, and guest management. It uses a graphical user interface (GUI) to handle data and stores records locally using data files.

## Features
* **Interactive GUI**: Built using Tkinter for a clean, user-friendly desktop experience.
* **Data Management**: Uses Pandas to read, process, and update records seamlessly.
* **Instant Feedback**: Implements Tkinter message boxes for success notifications, warnings, and error alerts.
* **Structured Local Storage**: Organizes data into dedicated relational CSV files.

## Tech Stack
* **Language**: Python 3.x
* **GUI Framework**: Tkinter
* **Data Analysis Library**: Pandas
* **Storage**: CSV (Comma-Separated Values)

## Project Structure
* `pro_2526.py`: The main Python application file containing the source code and GUI logic.
* `customer.csv`: Stores guest profiles, shop purchases, contact details, and transactions.
* `bills.csv`: Tracks transactions, room charges, and overall billing records.
* `room.csv`: Manages structural hotel room availability, layouts, and categories.

## Data Schemas

### 1. Customer Records (`customer.csv`)
The system logs every customer transaction with the following properties:
* `customer_name`: Name of the individual purchasing a product or service.
* `product_name`: The specific item bought or consumed (e.g., Pepsi, Balaji, Sprite, Cheetos, Apple).
* `mode_of_payment`: Method used for the transaction (e.g., Cash, Credit).
* `amt_paid`: Financial total paid for the item.
* `phone_no`: Contact telephone number for the customer record.

### 2. Billing Overview (`bills.csv`)
The system logs every financial transaction with the following properties:
* `booking_id`: Unique identifier for the guest's stay record.
* `total_bill_amount`: Numeric total calculation for charges incurred.
* `payment_method`: Method used for settlement (e.g., Cash, Debit Card, Credit Card).
* `extra_service`: Incidental charges added to the room (e.g., Room Service, Pool & Gym, Food Order).
* `discount_code`: Promotional adjustments applied to the base rate (e.g., Couple, Family, Cactus).
* `payment_status`: Current collection state tracking whether an invoice is **paid**, **partially paid**, or **yet to pay**.

### 3. Room Inventory (`room.csv`)
The system maps physical room configurations using these properties:
* `booking_id`: Foreign key matching the room status to an active guest stay record.
* `room_no`: The assigned alphanumeric room identifier (e.g., 133B, 140A, 111A, 188B).
* `room_type`: Accommodation class tier (e.g., penthouse suite, luxury suite, penthouse).
* `floor_no`: The building level where the unit is situated.
* `no_of_beds`: The total sleeping capacity configuration inside the room.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com
   cd hotel-management
   ```

2. **Install dependencies**:
   Ensure you have Pandas installed before running the application:
   ```bash
   pip install pandas
   ```

3. **Run the application**:
   ```bash
   python pro_2526.py
   ```

   <img width="501" height="412" alt="Screenshot 2026-08-18 224515" src="https://github.com/user-attachments/assets/7f85d4d9-f294-4d61-80de-bc69fbcb119c" />


## How It Works
* The system boots up by loading data from `customer.csv`, `bills.csv`, and `room.csv` into Pandas DataFrames.
* Users execute tasks via Tkinter forms to check-in guests, assign rooms, update services, and generate invoices.
* GUI pop-ups (Tkinter message boxes) validate data entry, flag errors, and confirm successful transactions.
* Modified data frames are written back to their respective CSV files to ensure persistent updates.
