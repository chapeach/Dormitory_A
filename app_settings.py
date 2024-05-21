from flask import Blueprint, session, render_template, redirect, request
import sqlite3

app_settings = Blueprint('app_settings', __name__)

# page setting user login
@app_settings.route('/settings/userlogin')
def User_login():
    try:
        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql = 'SELECT userId, password, level, status, no FROM Employee'
        data1 = cur.execute(sql)
        data1 = data1.fetchall()

        sql_list_level = 'SELECT level FROM LevelList'
        data_list_level = cur.execute(sql_list_level)
        data_list_level = data_list_level.fetchall()

        con.close()
    except:
        pass
    return render_template("/settings/userlogin.html", data1=data1, data_list_level=data_list_level)

# fn add userlogin
@app_settings.route('/settings/userlogin/addUser', methods = ["POST"])
def User_login_adduser():
    try:
        userId = request.form["userId"]
        password = request.form["password"]
        level = request.form["level"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql_userlogin_adduser = 'INSERT INTO Employee (userId, password, level, status) VALUES ("{}","{}","{}","{}")'.format(userId, password, level, "disable")
        data1 = cur.execute(sql_userlogin_adduser)

        con.commit()
        con.close()
    except:
        pass
    return redirect('/settings/userlogin')

# fn edit userlogin
@app_settings.route('/settings/userlogin/editUser', methods = ["POST"])
def User_login_edituser():
    try:
        userId = request.form["userId"]
        password = request.form["password"]
        level = request.form["level"]
        status = request.form["status"]
        no = request.form["no"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql_userlogin_edit = 'UPDATE Employee SET userId = "{}", password = "{}", level = "{}", status = "{}" WHERE no = "{}"'.format(userId, password, level, status, no)
        data1 = cur.execute(sql_userlogin_edit)

        con.commit()
        con.close()

    except:
        pass
    return redirect('/settings/userlogin')

# fn delete userlogin
@app_settings.route('/settings/userlogin/deleteUser', methods = ["POST"])
def User_login_deleteUser():
    try:
        no = request.form["no"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor() 
        sql_userlogin_delete = 'DELETE FROM Employee WHERE no = "{}"'.format(no)
        data1 = cur.execute(sql_userlogin_delete)

        con.commit()
        con.close()

    except:
        pass
    return redirect('/settings/userlogin')

# page setting level login
@app_settings.route('/settings/level')
def User_setting_level():
    try:
        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql_list_level = 'SELECT no, level FROM LevelList'
        data_list_level = cur.execute(sql_list_level)
        data_list_level = data_list_level.fetchall()

        con.close()
    except:
        pass
    return render_template("/settings/levellogin.html", data_list_level = data_list_level)

# fn add level name
@app_settings.route('/settings/userlogin/addLevelName', methods = ["POST"])
def User_login_addLevelName():
    try:
        levelName = request.form["levelName"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql_userlogin_addLevelName = f"INSERT INTO LevelList (level) VALUES ('{levelName}')"
        print(sql_userlogin_addLevelName)
        data1 = cur.execute(sql_userlogin_addLevelName)

        con.commit()
        con.close()
    except:
        pass
    return redirect('/settings/level')

# fn edit level login
@app_settings.route('/settings/userlogin/editLevelLogin', methods = ["POST"])
def User_login_editLevelLogin():
    try:
        no = request.form["no"]
        levelName = request.form["levelName"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql_edit_level_name = f'UPDATE LevelList SET level = "{levelName}" WHERE no = "{no}"'
        data1 = cur.execute(sql_edit_level_name)

        con.commit()
        con.close()

    except:
        pass
    return redirect('/settings/level')

# fn delete level name
@app_settings.route('/settings/userlogin/deleteLevelName', methods = ["POST"])
def User_login_delete_level_name():
    try:
        no = request.form["no"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor() 
        sql_userlogin_level_name_delete = 'DELETE FROM LevelList WHERE no = "{}"'.format(no)
        data1 = cur.execute(sql_userlogin_level_name_delete)

        con.commit()
        con.close()

    except:
        pass
    return redirect('/settings/level')