SELECT substr(fecha_hora, 1, 10) AS dia, ROUND(AVG(temp_c), 2) AS promedio
FROM lecturas
WHERE fecha_hora < '2026-10-03 19:00'
GROUP BY dia
ORDER BY dia;