SELECT maquina, SUM(errores) AS total_errores
FROM lecturas
WHERE fecha_hora < '2026-10-03 19:00'
GROUP BY maquina
ORDER BY total_errores DESC
LIMIT 1;