INSERT INTO Customer (name, email, phone_number, address, credit_score)
VALUES
    ('John Doe', 'john@example.com', '123-456-7890', '123 Main St', 750),
    ('Jane Smith', 'jane@example.com', '987-654-3210', '456 Elm St', 800),
    ('Michael Johnson', 'michael@example.com', '111-222-3333', '789 Oak St', 700),
    ('Emily Brown', 'emily@example.com', '444-555-6666', '101 Pine St', 780),
    ('David Wilson', 'david@example.com', '777-888-9999', '222 Maple St', 720),
    ('Sarah Johnson', 'sarah@example.com', '333-111-2222', '789 Walnut St', 740),
    ('Robert Davis', 'robert@example.com', '666-999-1111', '888 Cedar St', 760),
    ('Amanda Martinez', 'amanda@example.com', '222-444-6666', '333 Birch St', 780),
    ('Daniel Thompson', 'daniel@example.com', '555-777-8888', '555 Pine St', 720),
    ('Olivia Garcia', 'olivia@example.com', '888-222-4444', '777 Oak St', 790);

INSERT INTO Account (account_type, balance, customer_id)
VALUES
    ('Savings', 5000.00, 1),
    ('Current', 3000.00, 2),
    ('Savings', 7000.00, 3),
    ('Current', 4000.00, 4),
    ('Savings', 6000.00, 5),
    ('Savings', 5500.00, 6),
    ('Current', 4500.00, 7),
    ('Savings', 8000.00, 8),
    ('Current', 3500.00, 9),
    ('Savings', 9000.00, 10);

INSERT INTO Transactions (account_number, description, date, transaction_type, transaction_amount)
VALUES
    (1001, 'Initial deposit', '2024-05-15', 'Deposit', 1000.00),
    (1002, 'Initial deposit', '2024-05-15', 'Withdraw', 500.00),
    (1003, 'Initial deposit', '2024-05-15', 'Deposit', 1500.00),
    (1004, 'Initial deposit', '2024-05-15', 'Withdraw', 2000.00),
    (1005, 'Initial deposit', '2024-05-15', 'Deposit', 2500.00),
    (1006, 'Initial deposit', '2024-05-15', 'Withdraw', 1000.00),
    (1007, 'Initial deposit', '2024-05-15', 'Deposit', 3500.00),
    (1008, 'Initial deposit', '2024-05-15', 'Withdraw', 1500.00),
    (1009, 'Initial deposit', '2024-05-15', 'Deposit', 1800.00),
    (1010, 'Initial deposit', '2024-05-15', 'Withdraw', 1200.00);