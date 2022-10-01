from typing import List
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi import Response, status, responses
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.exc import IntegrityError

from config.db import conn
from models.recipe import recipes
from schemas.recipe import Recipe
from webapp.forms.recipes import RecipesForm

principal = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")

key = Fernet.generate_key()
funcf = Fernet(key)

recipe = APIRouter()


@recipe.get('/recipes/', response_model=List[Recipe], tags=['Recipes'])
def get_recipe(request: Request):
    connection = get_recipes()
    len_recipes = len(connection)
    return templates.TemplateResponse('recipes/recipes.html', \
                                      {'request': request, \
                                       'recipes': connection, \
                                       'len': len_recipes})


@recipe.get('/recipes', response_model=List[Recipe], tags=['Recipes'])
def get_recipes():
    return conn.execute(recipes.select()).fetchall()


@recipe.get('/{username}/recipes/', response_model=List[Recipe], tags=['Recipes'])
def get_recipe_user(username: str, request: Request):
    connection = get_recipes()
    len_recipes = len(connection)
    return templates.TemplateResponse('recipes/recipesprivate.html',
                                      {'request': request, \
                                       'recipes': connection, \
                                       'len': len_recipes, \
                                       'username': username})


@recipe.get('/{username}/recipes/recipes_form', response_model=Recipe, tags=['Recipes'])
def get_recipe_form(username: str, request: Request):
    return templates.TemplateResponse('recipes/recipes_form.html', \
                                      {'request': request, 'username': username})


@recipe.post('/{username}/recipes/recipes_form')
async def create_recipe(request: Request):
    recipe = RecipesForm(request)
    await recipe.load_data()
    if await recipe.is_valid():
        new_recipe = {'name': recipe.name,
                      'servings': recipe.servings,
                      'time_preparation_h': recipe.time_preparation_h,
                      'time_preparation_m': recipe.time_preparation_m,
                      'difficulty': recipe.difficulty,
                      'is_public': recipe.is_public,
                      "ingredients": recipe.ingredients,
                      'description': recipe.description}
        res = conn.execute(recipes.insert().values(new_recipe))
        try:
            if res.is_insert:
                return conn.execute(recipes.select().where(recipes.c.recipe_id \
                                                           == res.inserted_primary_key[0])).first()
                return responses.RedirectResponse(f'/recipes/', \
                                                  status_code=status.HTTP_302_FOUND
                                                  )
            else:
                templates.TemplateResponse('/recipes/recipes.html', recipe.__dict__)
        except IntegrityError:
            recipe.__dict__.get('errors').append('Duplicate recipe')
    return templates.TemplateResponse('recipes/recipes_form.html', recipe.__dict__)


@recipe.get("/recipes/{recipe_id}")
def get_recipe():
    return conn.execute(recipes.select().where(recipes.c.recipe_id == id)).first()


@recipe.delete("/recipes/{recipe_id}")
def delete_recipe():
    conn.execute(recipes.delete().where(recipes.c.recipe_id == id)).first()
    return Response(status_code=HTTP_204_NO_CONTENT)


@recipe.put('/recipes/{recipe_id}', response_model=Recipe, tags=['Recipes'])
def update_recipe(recipe: Recipe):
    conn.execute(recipes.update().values(
        recipe_id=recipe.recipe_id,
        name=recipe.name,
        servings=recipe.servings
    ).where(recipes.c.recipe_id == id))
    return conn.execute(recipes.select().where(recipes.c.recipe_id == id)).first()
