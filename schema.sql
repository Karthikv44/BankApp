-- Create the database
CREATE DATABASE Bank;

-- Use the database
USE Bank;


-- Create the Customer table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(20),
    address VARCHAR(255),
    credit_score INT
);

-- Create the Account table
CREATE TABLE Account (
    account_number INT PRIMARY KEY IDENTITY(1001,1),
    account_type VARCHAR(50),
    balance DECIMAL(18, 2),
    customer_id INT FOREIGN KEY REFERENCES Customer(customer_id)
);

-- Create the Transaction table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY IDENTITY(2001,1),
    account_number INT FOREIGN KEY REFERENCES Account(account_number),
    description VARCHAR(255),
    date DATE,
    transaction_type VARCHAR(50),
    transaction_amount DECIMAL(18, 2)
);