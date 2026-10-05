SELECT maquina, substr(fecha_hora, 1, 10) AS dia, COUNT(*) AS lecturas
FROM lecturas
WHERE fecha_hora < '2026-10-03'
GROUP BY maquina, dia
HAVING COUNT(*) <> 288;