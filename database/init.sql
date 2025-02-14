CREATE DATABASE banco_roxinho;
\c banco_roxinho;

CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  saldo NUMERIC(10,2) NOT NULL
);

CREATE TABLE produtos (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  preco NUMERIC(10,2) NOT NULL
);

CREATE TABLE transacoes (
  id SERIAL PRIMARY KEY,
  cliente_id INTEGER NOT NULL REFERENCES clientes(id),
  produto_id INTEGER NOT NULL REFERENCES produtos(id),
  data_transacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO clientes (nome, saldo) VALUES
  ('João', 1000.00),
  ('Maria', 1500.00),
  ('Carlos', 2000.00),
  ('Ana', 2500.00),
  ('Pedro', 3000.00),
  ('Mariana', 3500.00),
  ('Lucas', 4000.00),
  ('Fernanda', 4500.00),
  ('Ricardo', 5000.00),
  ('Beatriz', 5500.00),
  ('Eduardo', 6000.00),
  ('Paula', 6500.00),
  ('Roberto', 7000.00),
  ('Camila', 7500.00),
  ('Gabriel', 8000.00);

INSERT INTO produtos (nome, preco) VALUES
  ('Notebook', 2500.00),
  ('Smartphone', 800.00),
  ('Tablet', 1200.00),
  ('Monitor', 600.00),
  ('Teclado', 150.00),
  ('Mouse', 100.00),
  ('Impressora', 500.00),
  ('Scanner', 450.00),
  ('HD Externo', 300.00),
  ('SSD', 350.00),
  ('Memória RAM', 200.00),
  ('Placa Mãe', 400.00),
  ('Processador', 800.00),
  ('Placa de Vídeo', 1500.00),
  ('Fonte de Alimentação', 250.00);

INSERT INTO transacoes (cliente_id, produto_id) VALUES
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5),
  (6, 6),
  (7, 7),
  (8, 8),
  (9, 9),
  (10, 10),
  (11, 11),
  (12, 12),
  (13, 13),
  (14, 14),
  (15, 15);