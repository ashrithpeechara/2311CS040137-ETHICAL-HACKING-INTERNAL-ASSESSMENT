-- =============================================================================
-- SQL Injection Assessment Lab Database Schema
-- Database Target: SQLite 3 / MySQL Compatible
-- =============================================================================

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS system_audit_logs;

-- User Authentication & Role Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Financial / Accounts Table (Target for Privilege Escalation / Data Theft)
CREATE TABLE accounts (
    account_number VARCHAR(20) PRIMARY KEY,
    user_id INTEGER NOT NULL,
    account_type VARCHAR(30) NOT NULL,
    balance DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    ssn_last4 VARCHAR(4) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Products Catalog Table (Target for UNION-Based Extraction)
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL,
    description TEXT,
    is_hidden BOOLEAN DEFAULT 0
);

-- Audit Logs Table
CREATE TABLE system_audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action VARCHAR(100) NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
