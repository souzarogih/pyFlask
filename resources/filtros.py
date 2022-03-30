
def normalize_path_params(cidade=None,
                           estelas_min = 0,
                           estelas_max = 5,
                           diaria_min = 0,
                           diaria_max = 10000,
                           limit = 50,
                           offset = 0, **dados):
    if cidade:
        return {
            'estelas_min' : estelas_min,
            'estelas_max' : estelas_max,
            'diaria_min' : diaria_min,
            'diaria_max' : diaria_max,
            'cidade' : cidade,
            'limit' : limit,
            'offset' : offset}
    return {
        'estelas_min': estelas_min,
        'estelas_max': estelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset}


# consulta_sem_cidade = "SELECT * FROM hoteis \
#             WHERE (estrelas >= ? and estrelas <= ?) \
#             and (diaria >= ? and diaria <= ?) \
#             LIMIT ? OFFSET ?"
#
#
# consulta_com_cidade = "SELECT * FROM hoteis \
#             WHERE (estrelas >= ? and estrelas <= ?) \
#             and (diaria >= ? and diaria <= ?) \
#             and cidade = ? LIMIT ? OFFSET ?"


consulta_sem_cidade = "SELECT * FROM hoteis \
            WHERE (estrelas >= %s and estrelas <= %s) \
            and (diaria >= %s and diaria <= %s) \
            LIMIT %s OFFSET %s"


consulta_com_cidade = "SELECT * FROM hoteis \
            WHERE (estrelas >= %s and estrelas <= %s) \
            and (diaria >= %s and diaria <= %s) \
            and cidade = %s LIMIT %s OFFSET %s"