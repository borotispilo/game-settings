import sys
from PyQt5.QtWidgets import QApplication, QDialog
from main_settings_ui import Ui_Dialog as Ui_MainSettings
from graphics_settings_ui import Ui_Dialog as Ui_GraphicsSettings
from keybinds_settings_ui import Ui_Dialog as Ui_KeyBindsSettings

class GraphicsSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GraphicsSettings()
        self.ui.setupUi(self)
        self.ui.pushButtonApply.clicked.connect(self.apply_settings)
        self.ui.pushButtonBack.clicked.connect(self.reject)

    def apply_settings(self):
        settings = {
            "anti_aliasing": self.ui.checkBoxAntiAliasing.isChecked(),
            "shadows": self.ui.checkBoxShadows.isChecked(),
            "high_textures": self.ui.checkBoxHighTextures.isChecked()
        }
        print("Graphics settings applied:", settings)
        self.accept()

class KeyBindsSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_KeyBindsSettings()
        self.ui.setupUi(self)
        self.ui.lineEditJumpKey.setText("Space")
        self.ui.lineEditRunKey.setText("Shift")
        self.ui.lineEditAttackKey.setText("Ctrl")
        self.ui.pushButtonApply.clicked.connect(self.apply_settings)
        self.ui.pushButtonBack.clicked.connect(self.reject)

    def apply_settings(self):
        settings = {
            "jump_key": self.ui.lineEditJumpKey.text(),
            "run_key": self.ui.lineEditRunKey.text(),
            "attack_key": self.ui.lineEditAttackKey.text()
        }
        print("Key bindings applied:", settings)
        self.accept()

class MainSettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainSettings()
        self.ui.setupUi(self)
        self.ui.pushButtonGraphics.clicked.connect(self.open_graphics_settings)
        self.ui.pushButtonKeyBinds.clicked.connect(self.open_keybinds_settings)
        self.ui.pushButtonSave.clicked.connect(self.save_settings)
        self.ui.pushButtonCancel.clicked.connect(self.reject)

    def open_graphics_settings(self):
        graphics_dialog = GraphicsSettingsDialog(self)
        graphics_dialog.exec_()

    def open_keybinds_settings(self):
        keybinds_dialog = KeyBindsSettingsDialog(self)
        keybinds_dialog.exec_()

    def save_settings(self):
        settings = {
            "resolution": self.ui.comboBoxResolution.currentText(),
            "sound_volume": self.ui.sliderSound.value(),
            "lobby_music": self.ui.checkBoxLobbyMusic.isChecked(),
            "mouse_sensitivity": self.ui.sliderMouseSensitivity.value()
        }
        print("Settings saved:", settings)
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainSettingsDialog()
    window.show()
    sys.exit(app.exec_())