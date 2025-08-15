-- Scripts utilizados no projeto
-- Montagem e estrutura do banco de dados PostgreSQL na plataforma https://supabase.com/

--Criação da tabela Cotações 
-- Em casos de SQL Server
create table if not exists public.contacoes (
  id  int primary key identity (1,1) -- Iniciar em 1 e Incrementar 1 a cada novo registro
  ativo nvarchar(10) not null,
  preco decimal(18,2) not null, -- Define que o inteiro terá até 18 dígitos e apenas 2 casas decimais
  moeda varchar(10) not null default 'USD', -- Define que a moeda sempre será USD
  hora_coleta timestamp not null, -- Horário de Coleta da Pipeline
  inserido_em timestamp not null default NOW() -- Coluna de auditoria
 )

 --Criação da tabela Cotações 
-- Em casos de PostgreSQL
create table if not exists public.contacoes (
  id  BIGSERIAL primary key,
  ativo text not null,
  preco numeric(18,2) not null, -- Define que o valor terá até 18 dígitos e apenas 2 casas decimais
  moeda char(3) not null default 'USD', -- Define que a moeda sempre será USD
  hora_coleta timestampTz not null, -- Horário de Coleta da Pipeline
  inserido_em timestampTz not null default NOW() -- Coluna de auditoria
 )