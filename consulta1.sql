SELECT maquina, COUNT(*) AS lecturas_con_error
FROM lecturas
WHERE errores > 0
  AND fecha_hora < '2026-10-03 19:00'
GROUP BY maquina
ORDER BY lecturas_con_error DESC, maquina;