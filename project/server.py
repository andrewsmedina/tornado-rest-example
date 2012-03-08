import tornado.ioloop
import tornado.web
import tornado.database

import json


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/api/service", ServiceHandler)
        ]
        super(Application, self).__init__(handlers)
        self.db = tornado.database.Connection(
            host='localhost', database='project', user='root', password=''
        )


class ServiceHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self):
        query = self.db.query("SELECT * FROM services")
        service_list = []

        for service in query:
            service_list.append({
                'id': service['id'],
                'name': service['name']
            })

        services = {
            'objects': service_list
        }

        self.write(json.dumps(services))


if __name__ == "__main__":
    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()
