import os,sys,time,threading
from PySide6.QtWidgets import QApplication, QSystemTrayIcon
from PySide6.QtGui import QIcon
from PySide6.QtCore import QObject
def show_notification(icon, title, message):
    # 创建一个系统托盘图标
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon('1.png')) 
    tray_icon.setToolTip('888')
    tray_icon.show()
 
    # 发送通知
    tray_icon.showMessage(title, message, icon)
def exitting():
    time.sleep(1)
    app.quit()
if __name__ == '__main__':
    app = QApplication([])
    p=os.popen('apt policy system-core').readlines()
    linenum=len(p)
    # 显示通知
    version=p[4].rstrip('\n').lstrip('     ')
    
    if linenum>6:
        th=threading.Thread(target=exitting)
        th.start()
        show_notification(QSystemTrayIcon.Information,QObject.tr('检测到可用的系统更新'), QObject.tr(version))  
        
        sys.exit(app.exec())
    
    
    