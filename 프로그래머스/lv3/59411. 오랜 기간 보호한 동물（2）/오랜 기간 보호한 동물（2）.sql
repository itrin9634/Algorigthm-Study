SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A, ANIMAL_INS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY A.DATETIME - B.DATETIME DESC
LIMIT 2
