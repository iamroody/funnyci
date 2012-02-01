import web

urls = (
    '/', 'Index',
    '/callback', 'CallBack',
    )

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

class Index:
    def GET(self):
        return 'hello world!'
