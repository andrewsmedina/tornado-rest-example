import tornado.ioloop
import tornado.web
import tornado.database

import json


class ServiceHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return tornado.database.Connection(
            host='localhost', database='project', user='root', password=''
        )

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


application = tornado.web.Application([
    (r"/api/service", ServiceHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
