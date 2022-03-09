from conftest import get_api_star_wars_people_one


def test_deve_conter_nome_do_Luky(get_api_star_wars_people_one):
    name = get_api_star_wars_people_one['name']
    assert name == 'Luke Skywalker'


def test_deve_ter_participado_de_quatro_filmes(get_api_star_wars_people_one):
    films = get_api_star_wars_people_one['films']
    assert len(films) == 4

