from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import numpy as np
from datetime import datetime
import cv2, os, threading

file_name = None
window_size_text = None

def create_median_array(image, window_size, mode='horizontal'):
    result = np.zeros_like(image)
    half_window = window_size // 2
    for channel in range(image.shape[2]):
        padded_channel = np.pad(image[:,:,channel], ((half_window, half_window), (half_window, half_window)), mode='constant', constant_values=0)
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                if mode == 'horizontal':
                    window = padded_channel[i, j:j+window_size]
                elif mode == 'vertical':
                    window = padded_channel[i:i+window_size, j]
                elif mode == 'combined':
                    window_horizontal = padded_channel[i, j:j+window_size]
                    window_vertical = padded_channel[i:i+window_size, j]
                    window = np.concatenate((window_horizontal, window_vertical))
                sorted_window = np.partition(window, window.size // 2)
                median_value = sorted_window[window.size // 2]
                result[i, j, channel] = median_value

    return result.astype('uint8')

class ImageSelectorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clear_noise_thread = None
        self.setWindowIcon(QIcon("C:\\work\\2 semestr\\GUI\\лабы\\Lab1\\noise-remover.ico"))
        self.setWindowTitle("Noise Master")
        self.resize(600, 600)

        self.image_label = QLabel(self)

        central_widget = QWidget(self)
        central_layout = QHBoxLayout(central_widget)
        central_layout.addWidget(self.image_label)

        self.setCentralWidget(central_widget)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.show_image_dialog)
        self.add_noise_action = QAction("Add Noise", self)
        self.add_noise_action.triggered.connect(self.show_noise_input_dialog)
        self.clear_noise_action = QAction("Clear Noise", self)
        self.clear_noise_action.triggered.connect(self.clear_noise)
        self.compare_action = QAction("Compare", self)
        self.compare_action.triggered.connect(self.compare)
        self.save_action = QAction("Save", self)
        self.save_action.triggered.connect(self.save)

        toolbar.addAction(self.open_action)
        toolbar.addAction(self.add_noise_action)
        toolbar.addAction(self.clear_noise_action)
        toolbar.addAction(self.compare_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction("Quit", self.close)

        self.add_noise_action.setEnabled(False)
        self.clear_noise_action.setEnabled(False)
        self.compare_action.setEnabled(False)
        self.save_action.setEnabled(False)

        self.noise_level = 0
        self.active_img = 0

    def show_image_dialog(self):
        global file_name
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Изображения (*.png *.xpm *.jpg *.bmp *.jpeg);;Все файлы (*)', options=options)

        if file_name:
            self.show_image(file_name)

    def show_image(self, file_name):
        global is_noise_added
        self.add_noise_action.setEnabled(True)
        self.clear_noise_action.setEnabled(True)
        self.compare_action.setEnabled(False)
        self.save_action.setEnabled(True)
        is_noise_added = False
        orig_img = cv2.imread(file_name)
        dim = (600, 600)
        orig_img = cv2.resize(orig_img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite("orig_img.jpg", orig_img)
        height, width, _ = orig_img.shape
        bytes_per_line = 3 * width
        rgb_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
        pixmap = QPixmap.fromImage(QImage(rgb_img.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(pixmap)
        self.image_label.show()
        height, width, _ = orig_img.shape
        self.setFixedSize(width, height)
        self.active_img = 1

    def show_noise_input_dialog(self):
        dialog = NoiseInputDialog()
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.noise_level = dialog.slider.value()
            self.noise_level = self.noise_level * 255 // 100
            noise = 255 - self.noise_level
            img = cv2.imread("orig_img.jpg")
            imp_noise = np.zeros_like(img[:, :, 0], dtype=np.uint8)
            cv2.randu(imp_noise, 0, 255)
            imp_noise = cv2.threshold(imp_noise, noise, 255, cv2.THRESH_BINARY)[1]
            in_img = img.copy()
            for channel in range(img.shape[2]):
                in_img[:, :, channel] = cv2.add(img[:, :, channel], imp_noise)
            cv2.imwrite("noise_img.jpg", in_img)
            height, width, _ = in_img.shape
            bytes_per_line = 3 * width
            rgb_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2RGB)
            pixmap = QPixmap.fromImage(QImage(rgb_img.data, width, height, bytes_per_line, QImage.Format_RGB888))
            self.image_label.setPixmap(pixmap)
            self.image_label.show()
            self.clear_noise_action.setEnabled(True)
            self.active_img = 2


    def clear_noise(self):
        global window_size_text
        dialog = InputWindowSizeDialog()
        result = dialog.exec()

        if result == QDialog.Accepted:
            if "noise_img.jpg" in os.listdir():
                img = cv2.imread("noise_img.jpg")
            else:
                img = cv2.imread("orig_img.jpg")
            window_size = int(window_size_text)
            loading_dialog = LoadingDialog(self)
            loading_dialog.show()
            self.clear_noise_thread = threading.Thread(target=self.clear_noise_worker, args=(img, window_size, loading_dialog))
            self.clear_noise_thread.start()
            self.active_img = 3

    def clear_noise_worker(self, img, window_size, loading_dialog):
        worker = ClearNoiseWorker(self.image_label, self.compare_action, self.active_img)
        worker.finished.connect(loading_dialog.close)
        worker.process(img, window_size)

    def closeEvent(self, event):
        os.remove("orig_img.jpg")
        os.remove("noise_img.jpg")
        os.remove("denoise_img.jpg")
        event.accept()

    def compare(self):
        orig_img_path = "orig_img.jpg"
        denoised_img_path = "denoise_img.jpg"
        compare_window = ImageComparer(orig_img_path, denoised_img_path)
        compare_window.show()
        while compare_window.isVisible():
            QApplication.processEvents()

    def save(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
        if self.active_img == 1:
            cv2.imwrite(f"orig_img{formatted_datetime}.jpg", cv2.imread("orig_img.jpg"))
        elif self.active_img == 2:
            cv2.imwrite(f"noise_img{formatted_datetime}.jpg", cv2.imread("noise_img.jpg"))
        elif self.active_img == 3:
            cv2.imwrite(f"denoise_img{formatted_datetime}.jpg", cv2.imread("denoise_img.jpg"))

class ImageComparer(QMainWindow):
    def __init__(self, orig_img_path, denoised_img_path):
        super().__init__()
        self.setWindowTitle("Comparison")

        compare_layout = QHBoxLayout()
        original_label = QLabel("Original", self)
        original_label.setStyleSheet("font: bold 200px;")
        original_img = cv2.imread(orig_img_path)
        original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
        original_pixmap = QPixmap.fromImage(QImage(original_img_rgb.data, original_img_rgb.shape[1], original_img_rgb.shape[0], original_img_rgb.shape[1] * 3, QImage.Format_RGB888))
        original_label.setPixmap(original_pixmap)
        compare_layout.addWidget(original_label, alignment=Qt.AlignCenter)
        denoised_label = QLabel("Denoised", self)
        denoised_img = cv2.imread(denoised_img_path)
        denoised_img_rgb = cv2.cvtColor(denoised_img, cv2.COLOR_BGR2RGB)
        denoised_pixmap = QPixmap.fromImage(QImage(denoised_img_rgb.data, denoised_img_rgb.shape[1], denoised_img_rgb.shape[0], denoised_img_rgb.shape[1] * 3, QImage.Format_RGB888))
        denoised_label.setPixmap(denoised_pixmap)
        compare_layout.addWidget(denoised_label, alignment=Qt.AlignCenter)
        compare_widget = QWidget()
        compare_widget.setLayout(compare_layout)
        self.setCentralWidget(compare_widget)


class NoiseInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Noise picker')
        self.resize(300, 150)
        layout = QVBoxLayout()

        self.label = QLabel('Choose noise level:', self)
        layout.addWidget(self.label)

        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(20)
        self.slider.valueChanged.connect(self.update_label)
        layout.addWidget(self.slider)

        self.input_box = QLineEdit(self)
        self.input_box.setText('20')
        self.input_box.returnPressed.connect(self.update_slider)
        layout.addWidget(self.input_box)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def update_label(self, value):
        self.input_box.setText(f'{value}')

    def update_slider(self):
        try:
            value = int(self.input_box.text())
            if value < self.slider.minimum() or value > self.slider.maximum():
                raise ValueError("Значение вне допустимого диапазона")
            self.slider.setValue(value)
            self.value_label.setText(f'Текущее значение: {value}')
        except ValueError:
            self.input_box.setText("Неверное значение")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.update_slider()

class InputWindowSizeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Clear master')
        layout = QVBoxLayout()

        self.window_size_label = QLabel('Enter window size (odd and more than 1):', self)
        layout.addWidget(self.window_size_label)

        self.window_size_edit = QLineEdit(self)
        self.window_size_edit.setText('5')
        self.window_size_edit.setValidator(QIntValidator(1, 9999, self))
        layout.addWidget(self.window_size_edit)

        self.group = QButtonGroup()

        self.horizontal_checkbox = QCheckBox('Horizontal', self)
        self.horizontal_checkbox.setChecked(True)
        self.group.addButton(self.horizontal_checkbox)
        layout.addWidget(self.horizontal_checkbox)

        self.vertical_checkbox = QCheckBox('Vertikal', self)
        self.group.addButton(self.vertical_checkbox)
        layout.addWidget(self.vertical_checkbox)

        self.combined_checkbox = QCheckBox('Both', self)
        self.group.addButton(self.combined_checkbox)
        layout.addWidget(self.combined_checkbox)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.check_and_accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def check_and_accept(self):
        global window_size_text, mode
        window_size_text = self.window_size_edit.text()
        try:
            window_size = int(window_size_text)
            if window_size > 0 and window_size % 2 == 1:
                if self.horizontal_checkbox.isChecked():
                    mode = 'horizontal'
                elif self.vertical_checkbox.isChecked():
                    mode = 'vertical'
                elif self.combined_checkbox.isChecked():
                    mode = 'combined'
                self.accept()
            else:
                self.window_size_edit.clear()
        except ValueError:
            self.window_size_edit.clear()

class LoadingDialog(QDialog):
    closed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(470, 370)

        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)        
        self.movie_screen.setAlignment(Qt.AlignCenter) 

        self.loading_label = QLabel("Loading...")
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setStyleSheet("font: bold 100px; color: black;")

        main_layout = QVBoxLayout() 
        main_layout.addWidget(self.movie_screen)
        main_layout.addWidget(self.loading_label)
        self.setLayout(main_layout) 

        ag_file = "C:\\work\\2 semestr\\GUI\\лабы\\Lab1\\loading.gif"
        self.movie = QMovie(ag_file, QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.overlay = QFrame(parent)
        self.overlay.setGeometry(parent.geometry())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        self.overlay.setWindowFlags(Qt.FramelessWindowHint)
        self.overlay.show()


    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

class ClearNoiseWorker(QObject):
    finished = Signal()

    def __init__(self, image_label, compare_action, active_img, parent=None):
        super().__init__(parent)
        self.image_label = image_label
        self.compare_action = compare_action
        self.active_img = active_img

    def process(self, img, window_size):
        global mode
        result_array = create_median_array(img, window_size, mode=mode)
        out_img = result_array.astype('uint8')
        cv2.imwrite("denoise_img.jpg", out_img)
        height, width, _ = out_img.shape
        bytes_per_line = 3 * width
        rgb_img = cv2.cvtColor(out_img, cv2.COLOR_BGR2RGB)
        pixmap = QPixmap.fromImage(QImage(rgb_img.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(pixmap)
        self.image_label.show()
        self.compare_action.setEnabled(True)
        self.active_img = 3

        self.finished.emit()


if __name__ == '__main__':
    app = QApplication([])
    window = ImageSelectorApp()
    window.show()
    app.exec()