from behave import *
from works.common import *
from works.pokemonMap import *

@given('first store name')
def step_impl(context):
    context.common = Common()
    context.pokemonMap = PokemonMap()
    context.driver = context.common.openBrowser()

    context.first_store_name_by_API = context.pokemonMap.get_store_info(0)["name"]

    context.pokemonMap.go_to_pokemon_map_page(context.driver)
    context.pokemonMap.search_store_by_name(context.driver, context.first_store_name_by_API)

@when('the search starts')
def step_impl(context):
    context.first_store_name_by_web = context.pokemonMap.get_store_name_by_index(context.driver, "1")

@then('the map gives specific store')
def step_impl(context):
    assert (context.first_store_name_by_API == context.first_store_name_by_web)