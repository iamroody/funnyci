import web
from route import CallBack, Index

urls = (
    '/', 'Index',
    '/callback', 'CallBack',
    )

app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('weibo'))
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
    app.run()
