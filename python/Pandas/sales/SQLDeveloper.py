from pywinauto.application import Application

APP_PATH=r"C:\Users\amaindola\apps\sqldeveloper\sqldeveloper.exe"

sqldeveloper = Application(backend="uia")

# Connect to the already running app
try:
    sqldeveloper = Application(backend="uia").connect(path=r"sqldeveloper64W.exe")
    # sqldeveloper = Application(backend="uia").connect(process=15760)
except:
    sqldeveloper = Application(backend="uia").start(path=APP_PATH)

app_window = sqldeveloper.window(title='Oracle SQL Developer : Welcome Page')
# sqldeveloper.app_window.menu_select("Tools -> Prefrence")
sqldeveloper.Properties.print_control_identifiers()
# app_window.child_window(title="System", control_type="MenuItem").click_input()