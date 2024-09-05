import random, math

def generar_dist_uniforme(lim_inf, lim_sup, cant):
    lim_inf, lim_sup
    vec = []
    for i in range(0, cant):
        x = lim_inf + random.random() * (lim_sup-lim_inf)
        x_redondeado = round(x, ndigits=4)
        vec.append(x_redondeado)

    return vec


def generar_dist_exponencial(media, cant):
    vec = []
    for i in range(0, cant):
        x = -media * math.log((1 - random.random()), math.e)
        x_redondeado = round(x, ndigits=4)
        vec.append(x_redondeado)

    return vec


def generar_dist_normal(media, desv, cant):
    vec = []
    n = cant // 2 + 1 if cant % 2 else cant // 2
    for i in range(0, n):
        rnd = (random.random(), random.random())
        
        n1 = media + desv * math.sqrt(-2 * math.log(rnd[0])) * math.cos(2 * math.pi * rnd[1])
        vec.append(round(n1, ndigits=4))
        
        if len(vec) != cant:
            n2 = media + desv * math.sqrt(-2 * math.log(rnd[0])) * math.sin(2 * math.pi * rnd[1])
            vec.append(round(n2, ndigits=4))

    return vec