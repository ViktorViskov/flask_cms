CREATE DATABASE flask_test;
USE flask_test;
CREATE TABLE sql_requests (name VARCHAR(64), sql_request VARCHAR(255), PRIMARY KEY (name));
CREATE TABLE nav_menu (title VARCHAR(64), href VARCHAR(64));
CREATE TABLE pages (path VARCHAR(64) NOT NULL, title VARCHAR(255), type VARCHAR(32), file_path VARCHAR(64), item_path VARCHAR(64), sql_name VARCHAR(64), PRIMARY KEY (path), FOREIGN KEY (sql_name) REFERENCES sql_requests(name));
CREATE TABLE get (path VARCHAR(64), page VARCHAR(255), PRIMARY KEY (path), FOREIGN KEY (page) REFERENCES pages(path));
INSERT INTO nav_menu VALUES ('Admin panel', 'admin');
