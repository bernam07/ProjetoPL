IMPORT TABLE estacoes FROM "estacoes.csv";
IMPORT TABLE observacoes FROM "observacoes.csv";
PRINT TABLE estacoes;
SELECT * FROM observacoes WHERE Temperatura > 22;
SELECT Id,Temperatura,DataHoraObservacao FROM observacoes WHERE Temperatura > 20 LIMIT 2;
CREATE TABLE quente SELECT * FROM observacoes WHERE Temperatura > 22;
CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);
EXPORT TABLE quente AS "quente.csv";
EXPORT TABLE completo AS "completo.csv";
PROCEDURE atualizar_observacoes DO
  CREATE TABLE quente SELECT * FROM observacoes WHERE Temperatura > 22;
  CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);
END;
CALL atualizar_observacoes;
