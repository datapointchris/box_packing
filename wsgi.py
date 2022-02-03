"App entry point"
import platform
from box_packing import create_app

develop = False

app = create_app()

if __name__ == '__main__':
    if develop:
        from livereload import Server

        server = Server(app)
        server.watch('static/')
        if platform.system() == 'Darwin':
            # Mac
            server.serve(port=4000, host='0.0.0.0')
        else:
            # Linux Box
            server.serve(port=8000)
    else:
        if platform.system() == 'Darwin':
            # Mac
            app.run(port=4000, host='0.0.0.0')
        else:
            # Linux Box
            app.run(port='8000')
