from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QDialog, \
    QTabWidget, QSpinBox, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowTitle("Sparse Matrix")
        layout = QVBoxLayout()
        self.setLayout(layout)

        tabWidget = QTabWidget()
        tabWidget.setStyleSheet("font-size: 13px;")

        self.firstMatrixTab = FirstMatrixTab()
        self.secondMatrixTab = SecondMatrixTab()
        self.resultMatrixTab = ResultMatrixTab()

        tabWidget.addTab(self.firstMatrixTab, "First Matrix")
        tabWidget.addTab(self.secondMatrixTab, "Second Matrix")
        tabWidget.addTab(self.resultMatrixTab, "Result Matrix")

        layout.addWidget(tabWidget)


class FirstMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        dimensionsBox = QHBoxLayout()
        self.layout.addLayout(dimensionsBox)

        matrixDimensionsLabel = QLabel("Matrix Dimensios : ")
        matrixDimensionsLabel.setStyleSheet("font-size: 16px;")

        self.matrixRow = QSpinBox()
        self.matrixRow.setToolTip("Row")
        self.matrixRow.setMinimum(1)
        self.matrixRow.setMaximum(1000)
        self.matrixRow.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        xLabel = QLabel("\u00d7")
        xLabel.setStyleSheet("font-size: 25px;")

        self.matrixColumn = QSpinBox()
        self.matrixColumn.setToolTip("Column")
        self.matrixColumn.setMinimum(1)
        self.matrixColumn.setMaximum(1000)
        self.matrixColumn.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        self.showButton = QPushButton("Show Matrix")
        self.showButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.showButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 30px;
        """)

        dimensionsBox.addWidget(matrixDimensionsLabel)
        dimensionsBox.addWidget(self.matrixRow)
        dimensionsBox.addWidget(xLabel)
        dimensionsBox.addWidget(self.matrixColumn)
        dimensionsBox.addWidget(self.showButton)
        dimensionsBox.addStretch(1)
        dimensionsBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)

    def creatTable(self, row, column, matrix):
        matrix.setRowCount(row)
        matrix.setColumnCount(column)
        matrix.setStyleSheet("font-size: 14px;")
        for i in range(row):
            for j in range(column):
                matrix.setColumnWidth(j, 25)
                matrix.setItem(i, j, QTableWidgetItem('0'))
        return matrix


class SecondMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        dimensionsBox = QHBoxLayout()
        self.layout.addLayout(dimensionsBox)

        matrixDimensionsLabel = QLabel("Matrix Dimensios : ")
        matrixDimensionsLabel.setStyleSheet("font-size: 16px;")

        self.matrixRow = QSpinBox()
        self.matrixRow.setToolTip("Row")
        self.matrixRow.setMinimum(1)
        self.matrixRow.setMaximum(1000)
        self.matrixRow.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        xLabel = QLabel("\u00d7")
        xLabel.setStyleSheet("font-size: 25px;")

        self.matrixColumn = QSpinBox()
        self.matrixColumn.setToolTip("Column")
        self.matrixColumn.setMinimum(1)
        self.matrixColumn.setMaximum(1000)
        self.matrixColumn.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        self.showButton = QPushButton("Show Matrix")
        self.showButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.showButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 30px;
        """)

        dimensionsBox.addWidget(matrixDimensionsLabel)
        dimensionsBox.addWidget(self.matrixRow)
        dimensionsBox.addWidget(xLabel)
        dimensionsBox.addWidget(self.matrixColumn)
        dimensionsBox.addWidget(self.showButton)
        dimensionsBox.addStretch(1)
        dimensionsBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)

    def creatTable(self, row, column, matrix):
        matrix.setRowCount(row)
        matrix.setColumnCount(column)
        matrix.setStyleSheet("font-size: 14px;")
        for i in range(row):
            for j in range(column):
                matrix.setColumnWidth(j, 25)
                matrix.setItem(i, j, QTableWidgetItem('0'))
        return matrix


class ResultMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
