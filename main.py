
from src import logger
from src.http.app import create_app
from version import __app_version__ as app_version

#app = create_app('postgres://eehhtzmedraihw:92398039175b19236270484e0bde5fe15b7c14543e825f13deb2a2ba7b1bae2f@ec2-50-16-196-57.compute-1.amazonaws.com:5432/db1gognb8fvg36')
app = create_app('postgres://postgres:postgres@localhost:5432/shopping_manager?client_encoding=utf8')

logger.info("[X] START tc-c1-db-http ver. %s", app_version)

if __name__ == "__main__":
    app.run(debug=True,
            threaded=True,
            host='0.0.0.0',
            port=5000)
