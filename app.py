__author__ = 'spousty'


from bottle import route, run

@route('/')
def index():
    out = ""
    for i in range(20):
        out += " {0:02X}".format(i)
    return "<h1> hello OpenShift Ninjas</h1>" + "<code>{0}</code>".format(out)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
