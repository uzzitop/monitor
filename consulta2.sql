SELECT fecha_hora, maquina, temp_c
FROM lecturas
WHERE (temp_c < 8 OR temp_c > 14)
  AND fecha_hora < '2026-10-03 19:00'
ORDER BY fecha_hora
