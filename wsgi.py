"App entry point"
from box_packing import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8000)
