"App entry point"
from box_packing import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = create_app()

# app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1, x_for=1, x_host=1, x_proto=1)

if __name__ == '__main__':
    app.run(port=8000)
