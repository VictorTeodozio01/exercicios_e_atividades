-- Criar banco de dados
CREATE DATABASE Filmes;
GO

-- Usar o banco de dados criado
USE Filmes;
GO

-- Criar tabela de Filmes
CREATE TABLE Filmes (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nome NVARCHAR(100) NOT NULL,
    Ano INT NOT NULL,
    Duracao INT NOT NULL
);
GO

-- Criar tabela de Atores
CREATE TABLE Atores (
    Id INT PRIMARY KEY IDENTITY(1,1),
    PrimeiroNome NVARCHAR(100) NOT NULL,
    UltimoNome NVARCHAR(100) NOT NULL,
    Genero NVARCHAR(20) NOT NULL
);
GO

-- Criar tabela de Generos
CREATE TABLE Generos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nome NVARCHAR(50) NOT NULL
);
GO

-- Criar tabela de ElencoFilme (Relacionamento muitos para muitos entre Filmes e Atores)
CREATE TABLE ElencoFilme (
    FilmeId INT,
    AtorId INT,
    Papel NVARCHAR(100),
    FOREIGN KEY (FilmeId) REFERENCES Filmes(Id),
    FOREIGN KEY (AtorId) REFERENCES Atores(Id),
    PRIMARY KEY (FilmeId, AtorId)
);
GO

-- Criar tabela de FilmesGenero (Relacionamento muitos para muitos entre Filmes e Generos)
CREATE TABLE FilmesGenero (
    FilmeId INT,
    GeneroId INT,
    FOREIGN KEY (FilmeId) REFERENCES Filmes(Id),
    FOREIGN KEY (GeneroId) REFERENCES Generos(Id),
    PRIMARY KEY (FilmeId, GeneroId)
);
GO

-- Inserir dados na tabela de Filmes
INSERT INTO Filmes (Nome, Ano, Duracao) VALUES ('De Volta para o Futuro', 1985, 116);
INSERT INTO Filmes (Nome, Ano, Duracao) VALUES ('Titanic', 1997, 195);
INSERT INTO Filmes (Nome, Ano, Duracao) VALUES ('O Senhor dos Anéis: A Sociedade do Anel', 2001, 178);
INSERT INTO Filmes (Nome, Ano, Duracao) VALUES ('Matrix', 1999, 136);
INSERT INTO Filmes (Nome, Ano, Duracao) VALUES ('Forrest Gump', 1994, 142);
GO

-- Inserir dados na tabela de Atores
INSERT INTO Atores (PrimeiroNome, UltimoNome, Genero) VALUES ('Michael', 'J. Fox', 'Masculino');
INSERT INTO Atores (PrimeiroNome, UltimoNome, Genero) VALUES ('Leonardo', 'DiCaprio', 'Masculino');
INSERT INTO Atores (PrimeiroNome, UltimoNome, Genero) VALUES ('Kate', 'Winslet', 'Feminino');
INSERT INTO Atores (PrimeiroNome, UltimoNome, Genero) VALUES ('Elijah', 'Wood', 'Masculino');
INSERT INTO Atores (PrimeiroNome, UltimoNome, Genero) VALUES ('Tom', 'Hanks', 'Masculino');
GO

-- Inserir dados na tabela de Generos
INSERT INTO Generos (Nome) VALUES ('Aventura');
INSERT INTO Generos (Nome) VALUES ('Romance');
INSERT INTO Generos (Nome) VALUES ('Ficção Científica');
INSERT INTO Generos (Nome) VALUES ('Drama');
INSERT INTO Generos (Nome) VALUES ('Fantasia');
INSERT INTO Generos (Nome) VALUES ('Mistério');
GO

-- Inserir dados na tabela de ElencoFilme
INSERT INTO ElencoFilme (FilmeId, AtorId, Papel) VALUES (1, 1, 'Marty McFly');
INSERT INTO ElencoFilme (FilmeId, AtorId, Papel) VALUES (2, 2, 'Jack Dawson');
INSERT INTO ElencoFilme (FilmeId, AtorId, Papel) VALUES (2, 3, 'Rose DeWitt Bukater');
INSERT INTO ElencoFilme (FilmeId, AtorId, Papel) VALUES (3, 4, 'Frodo Baggins');
INSERT INTO ElencoFilme (FilmeId, AtorId, Papel) VALUES (5, 5, 'Forrest Gump');
GO

-- Inserir dados na tabela de FilmesGenero
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (1, 1); -- De Volta para o Futuro - Aventura
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (1, 3); -- De Volta para o Futuro - Ficção Científica
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (2, 2); -- Titanic - Romance
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (2, 4); -- Titanic - Drama
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (3, 1); -- O Senhor dos Anéis - Aventura
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (3, 5); -- O Senhor dos Anéis - Fantasia
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (4, 3); -- Matrix - Ficção Científica
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (6, 6); -- Filmes de Mistério
INSERT INTO FilmesGenero (FilmeId, GeneroId) VALUES (5, 4); -- Forrest Gump - Drama
GO

--1- Buscar o nome e ano dos filmes
SELECT Nome, Ano
FROM Filmes;

--2- Buscar o nome e ano dos filmes, ordenados por ordem crescente pelo ano
SELECT Nome, Ano
FROM Filmes
ORDER BY Ano ASC;

--3- Buscar pelo filme "De Volta para o Futuro", trazendo o nome, ano e a duração
SELECT Nome, Ano, Duracao
FROM Filmes
WHERE Nome = 'De Volta para o Futuro';

--4- Buscar os filmes lançados em 1997
SELECT Nome, Ano
FROM Filmes
WHERE Ano = 1997;

--5- Buscar os filmes lançados APÓS o ano 2000
SELECT Nome, Ano
FROM Filmes
WHERE Ano > 2000;

--6- Buscar os filmes com a duração maior que 100 e menor que 150, ordenando pela duração em ordem crescente
SELECT Nome, Duracao
FROM Filmes
WHERE Duracao > 100 AND Duracao < 150
ORDER BY Duracao ASC;

--7- Buscar a quantidade de filmes lançados no ano, agrupando por ano
SELECT Ano, COUNT(*) AS Quantidade
FROM Filmes
GROUP BY Ano
ORDER BY Quantidade DESC;

--8 - Buscar os atores do gênero masculino, retornando o PrimeiroNome e UltimoNome
SELECT PrimeiroNome, UltimoNome
FROM Atores
WHERE Genero = 'Masculino';

--9 - Buscar os atores do gênero feminino, retornando o PrimeiroNome, UltimoNome, e ordenando pelo PrimeiroNome
SELECT PrimeiroNome, UltimoNome
FROM Atores
WHERE Genero = 'Feminino'
ORDER BY PrimeiroNome ASC;

--10 - Buscar o nome do filme e o gênero
SELECT f.Nome AS Filme, g.Nome AS Genero
FROM Filmes f
JOIN FilmesGenero fg ON f.Id = fg.FilmeId
JOIN Generos g ON fg.GeneroId = g.Id;

--11 - Buscar o nome do filme e o gênero do tipo "Mistério"
SELECT f.Nome AS Filme, g.Nome AS Genero
FROM Filmes f
JOIN FilmesGenero fg ON f.Id = fg.FilmeId
JOIN Generos g ON fg.GeneroId = g.Id
WHERE g.Nome = 'Mistério';

--12 - Buscar o nome do filme e os atores, trazendo o PrimeiroNome, UltimoNome e seu Papel
SELECT f.Nome AS Filme, a.PrimeiroNome, a.UltimoNome, ef.Papel
FROM Filmes f
JOIN ElencoFilme ef ON f.Id = ef.FilmeId
JOIN Atores a ON ef.AtorId = a.Id;


