import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check NG")
        self.setFixedSize(750,560)

        self.MainUI()

    def MainUI(self):
        main_layout = QVBoxLayout()
        # frame for the main content
        frame_show = QFrame()
        frame_show.setStyleSheet("background-color: #f9f9f9; border: 1px solid #ccc;")
        frame_show.setFrameShape(QFrame.StyledPanel)
        frame_show.setFrameShadow(QFrame.Raised)

        # tạo các layout, widget cho các frame để hiển thị nội dung trong frame_show
        # với tab Check NG khi nhấn btn Check_NG thì hiển thị chức năng như Frame1.py
        # tạo hàm để hiển thị nội dung trong frame_show
        self.tab_view = QWidget()
        self.tab_view.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")       
        self.table_view = QWidget()
        self.table_view.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;") 




        main_layout.addWidget(frame_show)

        # Group button layout
        group_btn = QHBoxLayout()
        btn_check = QPushButton("Check_NG")
        btn_check.setFixedWidth(150)

        btn_check.setStyleSheet("background-color: #4CAF50; color: #353D38; font-weight: bold; font-size: 12px;")
        
        btn_settings = QPushButton("Settings")
        btn_settings.setFixedWidth(150)

        btn_settings.setStyleSheet("background-color: #E6D230; color: #353D38; font-weight: bold; font-size: 12px;")
        
        btn_config = QPushButton("Config")
        btn_config.setFixedWidth(150)
        btn_config.setStyleSheet("background-color: #2353D9; color: #353D38; font-weight: bold; font-size: 12px;")
        
        group_btn.addWidget(btn_check)
        group_btn.addWidget(btn_settings)   
        group_btn.addWidget(btn_config)
        
        main_layout.addLayout(group_btn)
        
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
