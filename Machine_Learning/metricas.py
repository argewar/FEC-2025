#metrica avaliaçao modelo
matrix_c = [
    [37, 0, 7, 1, 0, 0],
    [0, 11, 0, 0, 1, 0],
    [0, 0, 53, 0, 1, 0],
    [2, 0, 0, 19, 2, 1],
    [0, 0, 0, 0, 69, 0],
    [5, 0, 0, 1, 0, 22]
]

for i in range(len(matrix_c)):
    classe = i

# VP
    vp = matrix_c[classe][classe]

# FN: soma da linha da classe, excluindo o VP
    fn = sum(matrix_c[classe]) - vp

# FP: soma da coluna da classe, excluindo o VP
    fp = sum(row[classe] for i, row in enumerate(matrix_c) if i != classe)

# Soma total da matriz
    total = sum(sum(row) for row in matrix_c)

# VN
    vn = total - (vp + fn + fp)

    print(f"Classe {classe}:")
    print(f"VP = {vp}")
    print(f"FN = {fn}")
    print(f"FP = {fp}")
    print(f"VN = {vn}")

    print("Valores variáveis de análise:")
    if (vp + fn) > 0:
        sens = vp / (vp + fn)
    else:
        sens = 0.0

    if (vn + fp) > 0:
        espec = vn / (vn + fp)
    else:
        espec = 0.0

    if (vp + fp) > 0:
        prec = vp / (vp + fp)
    else:
        prec = 0.0

    if (prec + sens) > 0:
        f1_scor = 2 * (prec * sens) / (prec + sens)
    else:
        f1_scor = 0.0

    print(f"Sensibilidade (Recall): {sens:.4f}")
    print(f"Especificidade: {espec:.4f}")
    print(f"Precisão: {prec:.4f}")
    print(f"F1-Score: {f1_scor:.4f}")