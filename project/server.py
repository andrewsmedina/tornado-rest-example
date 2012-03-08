import tornado.ioloop
import tornado.web

import json


class ServiceHandler(tornado.web.RequestHandler):
    def get(self):
        services = {
            'objects': [{
                'id': 1,
                'name': 'django'
            }]
        }
        self.write(json.dumps(services))


application = tornado.web.Application([
    (r"/api/service", ServiceHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
