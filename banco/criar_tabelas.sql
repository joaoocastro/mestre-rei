CREATE TABLE barbeiro 
( 
 idBarbeiro INT PRIMARY KEY AUTO_INCREMENT,  
 NomeBarbeiro VARCHAR(n) NOT NULL,  
 telefoneBarbeiro VARCHAR(n),  
 fotoBarbeiro VARCHAR(n),  
); 

CREATE TABLE barbearia 
( 
 nome VARCHAR(n) NOT NULL,  
 endereco VARCHAR(n),  
 idBarbearia INT PRIMARY KEY AUTO_INCREMENT,  
 hrAbertura DATE,  
 hrFechamento DATE,  
); 

CREATE TABLE cliente 
( 
 idCliente INT PRIMARY KEY AUTO_INCREMENT,  
 nomeCliente VARCHAR(n) NOT NULL,  
 telefoneCliente VARCHAR(n),  
 emailCliente VARCHAR(n),  
 sexoCliente VARCHAR(n),  
 barbeiroPreferido VARCHAR(n),  
 fotoCliente VARCHAR(n),  
); 

CREATE TABLE trabalha 
( 
 idBarbeiro INT PRIMARY KEY,  
 idBarbearia INT,  
); 

CREATE TABLE agendamento 
( 
 dataCompleta DATE NOT NULL,  
 idAgendamento INT PRIMARY KEY AUTO_INCREMENT,  
 idBarbeiro INT PRIMARY KEY,  
 idCliente INT PRIMARY KEY,  
 idBarbearia INT PRIMARY KEY,  
); 

ALTER TABLE trabalha ADD FOREIGN KEY(idBarbeiro) REFERENCES barbeiro (idBarbeiro)
ALTER TABLE trabalha ADD FOREIGN KEY(idBarbearia) REFERENCES barbearia (idBarbearia)
ALTER TABLE agendamento ADD FOREIGN KEY(idBarbeiro) REFERENCES barbeiro (idBarbeiro)
ALTER TABLE agendamento ADD FOREIGN KEY(idCliente) REFERENCES cliente (idCliente)
ALTER TABLE agendamento ADD FOREIGN KEY(idBarbearia) REFERENCES barbearia (idBarbearia)