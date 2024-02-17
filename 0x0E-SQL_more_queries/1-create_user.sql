-- script that creates the MySQL server user user_0d_1.
-- Query to list all privileges (GRANT) of the MySQL users
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
