import numpy
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from spaceship.config import Settings
from spaceship.routers import api, health

# JUST A COMMENT WITHOUT ANY SENCE
def make_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        title=settings.app_title,
        description=settings.app_description,
        version=settings.app_version,
    )
    app.state.settings = settings

    if settings.debug:
        app.mount('/static', StaticFiles(directory='build'), name='static')

    app.include_router(api.router, prefix='/api', tags=['api'])
    app.include_router(health.router, prefix='/health', tags=['health'])

    @app.get('/', include_in_schema=False, response_class=FileResponse)
    async def root() -> str:
        return 'build/index.html'

    @app.get('/matrix')
    def matrix() -> dict:
        matrix_A = numpy.random.rand(10, 10)
        matrix_B = numpy.random.rand(10, 10)
        product = numpy.matmul(matrix_A, matrix_B)

        res = {
            "matrix_A": matrix_A.tolist(),
            "matrix_B": matrix_B.tolist(),
            "product of matrices": product.tolist()
        }
        return res

    return app
