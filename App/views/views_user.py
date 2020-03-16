from flask import Blueprint, render_template, request, Response, make_response, redirect, url_for, session

user = Blueprint("user", __name__)


@user.route("/userlogin/")
def user_login():
    return render_template("UserLogin.html")


@user.route("/douserlogin/", methods=["POST"])
def do_user_login():
    username = request.form.get("username")
    print(username)

    # resp = Response("登录成功%s" % username)
    resp = redirect(url_for("user.user_index"))

    # resp.set_cookie("username", username)
    session["username"] = username

    return resp


@user.route("/userindex/")
def user_index():

    # username = request.cookies.get("username", "游客")
    username = session.get("username")


    temp = render_template("index.html", username=username)

    resp = make_response(temp)

    return resp


@user.route("/userlogout/")
def user_logout():

    resp = redirect(url_for("user.user_index"))

    # resp.delete_cookie("username")
    # resp.delete_cookie("session")
    session.pop("username")

    return resp
