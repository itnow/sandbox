import json
from aiohttp import web


app = web.Application()


async def handle(request):
    response = {'status': 'success'}
    return web.Response(text=json.dumps(response), status=200)


async def new_user(request):
    try:
        username = request.query['name']
        print('Creating a new user with name:', username)
        response = {'status': 'success',
                    'message': 'user created'}
        return web.Response(text=json.dumps(response), status=200)
    except Exception as e:
        response = {'status': 'error',
                    'message': str(e)}
        return web.Response(text=json.dumps(response), status=500)


app.router.add_get('/', handle)
app.router.add_post('/', new_user)

web.run_app(app)
