import uuid

from flask import Blueprint, url_for, request, session, render_template, make_response, redirect, abort

blue = Blueprint("first", __name__)


@blue.route("/")
def index():
    return "index"


@blue.route("/heheheheheheheheheehhehe/", methods=["GET","POST","PUT"])
def hehe():
    return "呵呵哒"


@blue.route("/gethehe/")
def get_hehe():

    p = url_for("first.hehe")

    return p


@blue.route("/getstudent/<id>/")
def get_student(id):
    return "学生%s" % id


@blue.route("/getperson/<path:name>/")
def get_person(name):
    print(name)
    print(type (name))
    return "观察string类型"


@blue.route("/makemoney/<int:money>/")
def make_money(money):
    print(money)
    print(type(money))
    return "今天赚了%d" % money


@blue.route("/makemoneyfloat/<float:money>/")
def make_money_float(money):
    print(money)
    print(type(money))
    return "今天赚了"


@blue.route("/getuser/<uuid:uu>")
def get_user(uu):
    print(uu)
    print(type(uu))
    return "Hello"


@blue.route("/getuuid/")
def get_uu():
    uu = uuid.uuid4()
    print(type(uu))
    return str(uu)


@blue.route("/getpath/<any(a,b,c):p>")
def get_path(p):
    print(p)
    print(type(p))
    return "获取路径"


@blue.route("/request/", methods=["GET", "POST", "PUT", "PATCH"])
def get_request():

    print(request)
    print(type (request))

    print(request.method)

    print(request.url)

    print(request.args)

    print(request.form)

    print(request.remote_addr)

    print(request.base_url)

    print(request.files)

    print(request.cookies)

    print(session)

    return "Request"


@blue.route("/response/")
def get_response():
    return "德玛西亚", 404


@blue.route("/rendertemplate/")
def render_temp():
    resp = render_template("Response.html")

    print(resp)

    print(type(resp))

    return resp, 500


@blue.route("/makeresponse/")
def make_resp():

    resp = make_response("<h2>站着的同学好帅</h2>", 502)

    print(resp)

    print(type (resp))

    return resp


@blue.route("/redirect/")
def make_redir():

    # return redirect("/makeresponse/")
    return redirect(url_for("first.make_resp"))


@blue.route("/makeabort/")
def make_abort():

    abort(502)

    return "睡着了"


@blue.errorhandler(502)
def handler502(exception):
    return "不能出现crash，被人看到很丢人"


@blue.route("/setcookie/")
def set_cookie():

    temp = render_template("Response.html")

    resp = make_response(temp)

    resp.set_cookie("name", "Tommy")
    # resp.charset = ""

    return resp
