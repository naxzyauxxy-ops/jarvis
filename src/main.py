import sys
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
from orchestrator import JarvisOrchestrator
from utils import MemoryMonitor
from bridge import TelegramBridge

class JarvisUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Central Widget (Glass-Card)
        self.central_widget = QWidget()
        self.central_widget.setObjectName("GlassCard")
        self.layout = QVBoxLayout(self.central_widget)
        
        # Arc Reactor Visualizer (Placeholder for SVG/Animation)
        self.arc_reactor = QLabel("●")
        self.arc_reactor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.arc_reactor)
        
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet(open("../assets/style.qss").read())
        
        # Initialize Subsystems
        self.orchestrator = JarvisOrchestrator()
        self.memory_monitor = MemoryMonitor(threshold=75)
        self.telegram_bridge = TelegramBridge(self.orchestrator)
        
        # Start Threads
        threading.Thread(target=self.telegram_bridge.start_polling, daemon=True).start()
        
    def keyPressEvent(self, event):
        # Emergency Kill Switch: Ctrl+Shift+K
        if event.modifiers() == (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.ShiftModifier) and event.key() == Qt.Key.Key_K:
            print("[!] EMERGENCY STOP TRIGGERED")
            sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = JarvisUI()
    jarvis.show()
    sys.exit(app.exec())
