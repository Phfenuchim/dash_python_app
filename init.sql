IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'testing_plotly')
    CREATE DATABASE testing_plotly;
GO

USE testing_plotly;
GO

IF OBJECT_ID('roles', 'U') IS NULL
    CREATE TABLE roles (
        id INT PRIMARY KEY IDENTITY(1,1),
        nome VARCHAR(50) NOT NULL UNIQUE
    );
GO

IF OBJECT_ID('users', 'U') IS NULL
    CREATE TABLE users (
        id INT PRIMARY KEY IDENTITY(1,1),
        nome VARCHAR(100),
        email VARCHAR(100) NOT NULL UNIQUE,
        SenhaHash VARCHAR(255) NOT NULL,
        data_criacao DATETIME DEFAULT GETDATE()
    );
GO

IF OBJECT_ID('users_roles', 'U') IS NULL
    CREATE TABLE users_roles (
        user_id INT,
        role_id INT,
        PRIMARY KEY (user_id, role_id),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (role_id) REFERENCES roles(id)
    );
GO

IF NOT EXISTS (SELECT 1 FROM roles WHERE nome = 'admin')
    INSERT INTO roles (nome) VALUES ('admin');
GO

IF NOT EXISTS (SELECT 1 FROM users WHERE email = 'joao@email.com')
    INSERT INTO users (nome, email, SenhaHash)
    VALUES ('João da Silva', 'joao@email.com', '$2b$12$I3kY2mmsolol7nkpIMzpYOnp0Da8qUTe/5nGVjkTmWYRrPTTLrKZW');
GO
-- Relaciona o usuário com a role 'admin'
IF NOT EXISTS (
    SELECT 1 FROM users_roles ur
    JOIN users u ON u.id = ur.user_id
    JOIN roles r ON r.id = ur.role_id
    WHERE u.email = 'joao@email.com' AND r.nome = 'admin'
)

BEGIN
    DECLARE @userId INT, @roleId INT;
    SELECT @userId = id FROM users WHERE email = 'joao@email.com';
    SELECT @roleId = id FROM roles WHERE nome = 'admin';

    INSERT INTO users_roles (user_id, role_id)
    VALUES (@userId, @roleId);
END
GO
