-- creates a database name 'seajro_app'

CREATE DATABASE IF NOT EXISTS `seajro_app`;
CREATE USER IF NOT EXISTS 'seajro_admin'@'localhost' IDENTIFIED BY 'Seajro_admin1';
GRANT ALL PRIVILEGES ON seajro_app.* TO 'seajro_admin'@'localhost';
