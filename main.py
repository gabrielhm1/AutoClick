from interface.main_window import *
from pynput.mouse import Listener
import win32gui
import time
from interface import select_window
from functions.command import Command
from functions.runthread import RunThread

text_to_print='default_predefined_text'
shortcut = 'c' #define your hot-keyc


commands = []
events = 0

def main(ui):
    ui.events = 0
    ui.commands = commands

    def fileOpen():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        for event in range(ui.events):
            ui.tableWidget.setItem(ui.events, 0, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 1, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 2, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 3, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 4, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 5, QTableWidgetItem(''))
            ui.events = 0
        if file:
            fileO = open(file,'r')

            for line in fileO:
                word = line.split(',')
                print(word)
                ui.tableWidget.setItem(ui.events, 0, QTableWidgetItem(word[0]))
                ui.tableWidget.setItem(ui.events, 1, QTableWidgetItem(word[1]))
                ui.tableWidget.setItem(ui.events, 2, QTableWidgetItem(word[2]))
                ui.tableWidget.setItem(ui.events, 3, QTableWidgetItem(word[3]))
                ui.tableWidget.setItem(ui.events, 4, QTableWidgetItem(word[4]))
                ui.tableWidget.setItem(ui.events, 5, QTableWidgetItem(word[5]))
                ui.events=ui.events+1


    def fileSave():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)


        if file:
            fileO = open(file,'w')
            for x in range(ui.events):
                line = ''
                for y in range(6):
                    if y == 0:
                        line = ui.tableWidget.item(x,y).text()
                    else:
                        line = line+','+ui.tableWidget.item(x,y).text()

                line = line+'\n'
                fileO.write(line)

            fileO.close()

    def runMode():
        allCommands =[]

        for x in range(ui.events):
            currentCommand = Command()
            currentCommand.setId(ui.tableWidget.item(x, 0).text())
            currentCommand.setAction(ui.tableWidget.item(x, 1).text())

            if ui.tableWidget.item(x, 1).text() == "Click":
                currentCommand.setxAxis(ui.tableWidget.item(x, 2).text())
                currentCommand.setyAxis(ui.tableWidget.item(x, 3).text())
            elif ui.tableWidget.item(x, 1).text() == "Key":
                currentCommand.setKey(ui.tableWidget.item(x, 2).text())

            currentCommand.setDelay(ui.tableWidget.item(x, 4).text())
            currentCommand.setRepeat(ui.tableWidget.item(x, 5).text())
            allCommands.append(currentCommand)

        ui.thread = RunThread()
        ui.thread.setCommand(allCommands)
        ui.breakLoop.clicked.connect(threadStop)
        ui.thread.start()
        ui.addKey.setEnabled(False)
        ui.addClick.setEnabled(False)
        ui.runProgram.setEnabled(False)
        ui.deleteIt.setEnabled(False)


    def threadStop():
        ui.thread.stop()
        ui.addKey.setEnabled(True)
        ui.addClick.setEnabled(True)
        ui.runProgram.setEnabled(True)
        ui.deleteIt.setEnabled(True)

    def clickl():
        def on_click(x, y, button, pressed):

            global x1, x2, y1, y2
            if pressed:
                x1, y1 = x, y
            if not pressed:
                x2, y2 = x, y
                # Pega o contexto gráfico para o Desktop
                dc = win32gui.GetDC(0)
                #inseri os dados nos campos das coordenadas
                ui.aX1.setText(str(x1))
                ui.aX2.setText(str(x2))
                ui.aY1.setText(str(y1))
                ui.aY2.setText(str(y2))
                # Desenha um quadrado
                win32gui.MoveToEx(dc, x1, y1)
                win32gui.PolylineTo(dc,((x1,y1),(x1,y2),(x2,y2),(x2,y1),(x1,y1)))
                time.sleep(1)
                listener.stop()

        with Listener(on_click=on_click) as listener:
            listener.join()


    def delLast():

        if ui.events == 0:
            ui.tableWidget.setItem(ui.events, 0, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 1, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 2, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 3, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 4, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events, 5, QTableWidgetItem(''))

        else:
            ui.tableWidget.setItem(ui.events-1, 0, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events-1, 1, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events-1, 2, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events-1, 3, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events-1, 4, QTableWidgetItem(''))
            ui.tableWidget.setItem(ui.events-1, 5, QTableWidgetItem(''))
            ui.events = ui.events-1



    def addClicked():
        ui.tableWidget.setItem(ui.events,0,QTableWidgetItem(str(ui.events)))
        ui.tableWidget.setItem(ui.events,1,QTableWidgetItem("Click"))
        ui.tableWidget.setItem(ui.events,2,QTableWidgetItem(str(ui.aX1.text()+" - "+str(ui.aX2.text()))))
        ui.tableWidget.setItem(ui.events,3,QTableWidgetItem(str(ui.aY1.text()+" - "+str(ui.aY2.text()))))
        ui.tableWidget.setItem(ui.events,4,QTableWidgetItem(str(ui.TimeI.text()+" - "+str(ui.TimeE.text()))))
        ui.tableWidget.setItem(ui.events,5,QTableWidgetItem(str(ui.repeatI.text()+" - "+str(ui.repeatE.text()))))
        ui.events = ui.events+1


    def addKeyed():
        ui.tableWidget.setItem(ui.events,0,QTableWidgetItem(str(ui.events)))
        ui.tableWidget.setItem(ui.events,1,QTableWidgetItem("Key"))
        ui.tableWidget.setItem(ui.events,2,QTableWidgetItem(ui.Key.text()))
        ui.tableWidget.setItem(ui.events,3,QTableWidgetItem(ui.Key.text()))
        ui.tableWidget.setItem(ui.events,4,QTableWidgetItem(str(ui.timeKI.text()+" - "+str(ui.timeKE.text()))))
        ui.tableWidget.setItem(ui.events,5,QTableWidgetItem(str(ui.repeatKI.text()+" - "+str(ui.repeatKE.text()))))
        ui.events = ui.events+1



    def arSelect():
        ui.window = select_window.Window()
        ui.window.show()
        MainWindow.showMinimized()

        clickl()
        MainWindow.showNormal()
        ui.window.close()



    ui.pushButton_2.clicked.connect(arSelect)
    ui.addKey.clicked.connect(addKeyed)
    ui.addClick.clicked.connect(addClicked)
    ui.runProgram.clicked.connect(runMode)
    ui.actionOpen.triggered.connect(fileOpen)
    ui.actionSave.triggered.connect(fileSave)
    ui.deleteIt.clicked.connect(delLast)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    main(ui)
    MainWindow.show()
    sys.exit(app.exec_())