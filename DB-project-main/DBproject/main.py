# Libraries and modules used
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt, QDateTime, QDate, QDate
import sys
import pyodbc


server = "DESKTOP-51E978F\SSMSRS0001"
database = "BookMySalon2" # Name of database
use_windows_authentication = True # Set to True to use Windows Authentication

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        loadUi('Welcome.ui', self)
    
        self.Cliwnt.clicked.connect(self.clientDashboard)
        self.Employee.clicked.connect(self.employeeDashboard)

    def clientDashboard(self):
        self.hide()

        self.client_dashboard_window = ClientDashboardWindow()
        self.client_dashboard_window.show()

    def employeeDashboard(self):
        self.hide()
        # Add functionality for the employee dashboard here
        self.Employee_dashboard_window = EmployeeDashboardWindow()
        self.Employee_dashboard_window.show()
        

class ClientDashboardWindow(QMainWindow):
    def __init__(self):
        super(ClientDashboardWindow, self).__init__()
        loadUi('ClientDashboard.ui', self)
        # self.name = name

        self.createAcc.clicked.connect(self.CreateAcc)
        # self.login.clicked.connect(self.LoginScreen())
        self.login.clicked.connect(self.LoginScreen)


    def CreateAcc(self):
        # self.hide()
        self.CreateAcc_window = CreateAccWindow()
        self.CreateAcc_window.show()

    def LoginScreen(self):
        self.hide()
        self.LoginScreenwindow = LoginScreenWindow()
        self.LoginScreenwindow.show()

class LoginScreenWindow(QMainWindow):
    def __init__(self):
        super(LoginScreenWindow, self).__init__()
        loadUi('ClientLogin.ui', self)
        # self.back.clicked.connect(self.backtomain)
        # self.name = name
        
        self.login.clicked.connect(self.checkInfo)
        self.back.clicked.connect(self.goBack)
        
    def goBack(self):
        self.hide()
        self.goBacktoWelcome_window = MyMainWindow()
        self.goBacktoWelcome_window.show()

    def checkInfo(self):
        username = self.username.text()
        password = self.password.text()
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "SELECT UserName, Password FROM Account WHERE UserName = ? AND Password = ?"
        cursor.execute(sql_query, (username, password))
        
        result = cursor.fetchone()

        if result is None:
            warning = QMessageBox()
            # warning.setWindowTitle("Confirmation Box")
            warning.setText("Incorrect password or username. Try again!")
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.addButton(QMessageBox.StandardButton.Ok)
            warning.exec()
        else:
            warning = QMessageBox()
            # warning.setWindowTitle("Confirmation Box")
            warning.setText("Account login successful. You can now book an appointment!")
            warning.setIcon(QMessageBox.Icon.Information)
            warning.addButton(QMessageBox.StandardButton.Ok)
            warning.exec()
            self.bookAppp(username)
        
    def bookAppp(self, username):
        self.bookAppOrView_window = BookApporViewWindow(username)
        self.bookAppOrView_window.show()

class CreateAccWindow(QMainWindow):
    def __init__(self):
        super(CreateAccWindow, self).__init__()
        loadUi('CreateAcc.ui', self)
        
        self.Confirm.clicked.connect(self.check_text)
        self.Back.clicked.connect(self.backtomain)

    def get_username(self, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query_username = """select username from account where username = ?"""
        cursor.execute(sql_query_username, (username))
        result_username = cursor.fetchone()
        connection.commit()
        connection.close()
        return result_username
    
    def get_email(self, email):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query_email = """select email from customer where email = ?"""
        cursor.execute(sql_query_email, (email))
        # sql_query = "SELECT UserName, Password FROM Account WHERE UserName = ? AND Password = ?"
        # cursor.execute(sql_query, (username, password))
        
        result_email = cursor.fetchone()
        connection.commit()
        connection.close()
        return result_email

        
    def check_text(self):
        name = self.name.text()
        contactNo = self.contactNo.text()
        email = self.email.text()
        dob = self.dateEdit.date()
        username = self.Username.text()
        password = self.password.text()
        gender = self.comboBox.currentText()
        city = self.city.text()
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        usernames = self.get_username(username)
        emails = self.get_email(email)
        
        if  name=='' or contactNo=='' or email=='' or username=='' or password=='' or dob>QDate.currentDate():
        # Check if the text contains any numbers
            if name=='':
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Please write your name.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            
            elif contactNo=='':
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Please provide your contact number your name.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            elif email=='':
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Please provide your email.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            elif username=='':
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Please provide a username.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
                
            elif password=='':
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Please provide a password.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            elif city=='':
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Please enter your city.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif dob>QDate.currentDate():
                warning = QMessageBox()
                warning.setText("Please enter the correct date of birth.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

        else:
            if len(contactNo)>6:
                warning = QMessageBox()
                warning.setText("Contact number can only have 6 digits.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            if not any(char.isdigit() for char in username):
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Username requires at least one number.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            if not any(char.isdigit() for char in password):
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Password requires at least one special character.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            if usernames is not None:
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Username already exists, choose a different username.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            if emails is not None:
                warning = QMessageBox()
                # warning.setWindowTitle("Confirmation Box")
                warning.setText("Account already exists for this email, try again.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            else:
                confirmation = QMessageBox()
                confirmation.setText("Your account has been created, you can login now.")
                confirmation.setIcon(QMessageBox.Icon.Information)
                confirmation.addButton(QMessageBox.StandardButton.Ok)
                confirmation.exec()
                sql_query = """INSERT INTO CUSTOMER
                ([Name], [Contact_number], [Email])
            VALUES (?, ?, ?)"""
                cursor.execute(sql_query, (name, contactNo, email))
                connection.commit()
                connection.close()
            # sql_query1 = "SELECT customerID FROM Customer WHERE customer.name = ?"
            # cursor.execute(sql_query1, name)
                self.add_loginInfo(email, username, password)

    def add_loginInfo(self, email, username, password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query2 = "select customerID from customer WHERE email = ?;"
        cursor.execute(sql_query2, (email))
        result = cursor.fetchone()
        sql_query = """INSERT INTO Account
    ([UserName], [Password], [customerID])
        VALUES (?, ?, ?)"""
        cursor.execute(sql_query, (username, password, result[0]))
        connection.commit()
        self.redirectLogin()
        connection.close()
            
        

    def backtomain(self):
        self.close()

    def redirectLogin(self):
        self.close()
        self.LoginScreenwindow = LoginScreenWindow()
        self.LoginScreenwindow.show()
       

class BookApporViewWindow(QMainWindow):
    def __init__(self, username):
        super(BookApporViewWindow, self).__init__()
        loadUi('BookOrView.ui', self)
        self.username = username
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "select customerID from account WHERE username = ?;"
        cursor.execute(sql_query, (username))
        result = cursor.fetchone()
        customerID = result[0]
        connection.commit()
        connection.close()
        self.bookAppt.clicked.connect(lambda: self.bookApp(username, customerID))
        self.viewAppt.clicked.connect(lambda: self.viewApp(username, customerID))


    def bookApp(self, username, customerID):
        self.bookApp_window = BookApptWindow(username, customerID)
        self.bookApp_window.show()

    def viewApp(self, username, customerID):
        self.viewApp_window = ViewApptWindow(username, customerID)
        self.viewApp_window.show()

class EmployeeDashboardWindow(QMainWindow):
    def __init__(self):
        super(EmployeeDashboardWindow, self).__init__()
        loadUi('EmporManager.ui', self)

        # self.staff.clicked.connect(lambda: self.staffDashboard)
        # self.manager.clicked.connect(lambda: self.managerDashboard)
        self.emplogin.clicked.connect(self.showEmpLoginWindow)

    def showEmpLoginWindow(self):
        self.emp_login_window = EmpLoginWindow()
        self.emp_login_window.show()

    # def staffDashboard(self):
    #     self.staffDashboard_window = staffDashboardWindow()
    #     self.staffDashboard_window.show()


    # def managerDashboard(self):
    #     self.managerDashboard_window = managerDashboardWindow()
    #     self.managerDashboard_window.show()

# class staffDashboardWindow(QMainWindow):
#     def __init__(self):
#         super(staffDashboardWindow, self).__init__()
#         loadUi('EmpLogin.ui', self)
        
class EmpLoginWindow(QMainWindow):
    def __init__(self):
        super(EmpLoginWindow, self).__init__()
        loadUi('EmpLogin.ui', self)

        self.pushButton.clicked.connect(self.checkLogin)

        self.pushButton_2.clicked.connect(self.goBack)

    def checkLogin(self):
        name = self.lineEdit.text()
        employee_id = (self.lineEdit_2.text())
        salon_id = (self.lineEdit_4.text())
        if name == ' ' or employee_id == ' ' or salon_id == ' ':
            if name == ' ':
                warning = QMessageBox()
                warning.setText("Please enter your name.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            elif employee_id == ' ':
                warning = QMessageBox()
                warning.setText("Please enter your ID.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            elif salon_id == ' ':
                warning = QMessageBox()
                warning.setText("Please enter your salon ID.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
        else:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            sql_query = "SELECT Name, EmployeeID, SalonID FROM Employee WHERE Name = ? AND EmployeeID = ? AND SalonID = ?"
            cursor.execute(sql_query, (name, int(employee_id,), int(salon_id,)))

            result = cursor.fetchone()
            if result is None:
                warning = QMessageBox()
                warning.setText("No such employee found. Try again.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            else:
                warning = QMessageBox()
                warning.setText("Employee login successful. You can now proceed!")
                warning.setIcon(QMessageBox.Icon.Information)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
                connection.close()
                # Redirect to manager dashboard
                self.redirectToManagerDashboard(int(employee_id), int(salon_id))        

    def redirectToManagerDashboard(self, employee_id, salon_id):
        self.manager_dashboard_window = managerDashboardWindow(employee_id, salon_id)
        self.manager_dashboard_window.show()
        self.hide()

    def goBack(self):
        self.close()
        self.employee_dashboard_window = EmployeeDashboardWindow()
        self.employee_dashboard_window.show()

class managerDashboardWindow(QMainWindow):
    def __init__(self, employee_id, salon_id):
        super(managerDashboardWindow, self).__init__()
        loadUi('ManagerDashboard.ui', self)
        self.inventory.clicked.connect(lambda: self.inventoryWindow(employee_id, salon_id))
        self.update.clicked.connect(lambda: self.updateService(employee_id, salon_id))
        self.monthlyRep.clicked.connect(lambda: self.monthlyReport(employee_id, salon_id))

        # self.viewAppt.clicked.connect(lambda: self.viewApp(username, customerID))
    def inventoryWindow(self, employee_id, salon_id):
        self.inventory_window = InventoryWindow(employee_id, salon_id)
        self.inventory_window.show()
        # self.viewApp_window = ViewApptWindow(username, customerID)
        # self.viewApp_window.show()

    def updateService(self, employee_id, salon_id):
        self.updateServices_window = UpdateServicesWindow(employee_id, salon_id)
        self.updateServices_window.show()


    def monthlyReport(self, employee_id, salon_id):
        self.monthlyReport_window = MonthlyReportWindow(employee_id, salon_id)
        self.monthlyReport_window.show()
    
class InventoryWindow(QMainWindow):
    def __init__(self, employee_id, salon_id):
        super(InventoryWindow, self).__init__()
        loadUi('Inventory.ui', self)

        # self.employee_id = employee_id
        # self.salon_id = salon_id

        # Autofill Manager ID, Salon ID
        self.lineEdit.setText(str(employee_id))
        self.lineEdit_2.setText(str(salon_id))
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        # Connect search button
        self.pushButton_5.clicked.connect(lambda: self.searchInventory( salon_id))

    def searchInventory(self, salon_id):
        product_id = int(self.lineEdit_3.text())
        product_name = self.lineEdit_4.text()

        # Access Inventory table for the specified ProductID
        inventory_data = self.getInventoryData(product_id, salon_id)
        self.order.clicked.connect(lambda: self.orderProd(product_id, salon_id))

        if inventory_data:
            # Display results in the table widget
            self.displayResults(product_id, product_name, *inventory_data)
        else:
            self.clearTable() 

    def orderProd(self, product_id, salon_id):
        self.orderProd_window = OrderProdWindow(product_id, salon_id)
        self.orderProd_window.show()

    def getInventoryData(self, product_id, salon_id):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query = """
            SELECT i.ProductID, p.Product_Name, s.SupplierID, i.QuantityLeft
            FROM Inventory AS i
            JOIN Product AS p ON i.ProductID = p.ProductID
            JOIN Suppliers AS s ON i.ProductID = s.ProductID
            WHERE i.SalonID = ? AND i.ProductID = ?
        """

        cursor.execute(sql_query, (salon_id, product_id))
        result = cursor.fetchone()
        connection.close()

        return result if result else None

    def displayResults(self, product_id, product_name, supplier_id, quantity_left):
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)

        # Set headers
        headers = ["ProductID", "ProductName", "SupplierID", "QuantityLeft"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Populate table with data
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(product_id)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(product_name))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(supplier_id)))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(quantity_left)))

    def clearTable(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        
class OrderProdWindow(QMainWindow):
    def __init__(self, product_id, salon_id):
        super(OrderProdWindow, self).__init__()
        loadUi('ReOrder.ui', self)

class UpdateServicesWindow(QMainWindow):
    def __init__(self, employee_id, salon_id):
        super(UpdateServicesWindow, self).__init__()
        loadUi('AddDeleteServices (1).ui', self)
    # def __init__(self, employee_id, salon_id):
        self.populateServices_table(salon_id)
        self.add.clicked.connect(lambda: self.addService(salon_id))
        self.delete_2.clicked.connect(lambda: self.deleteService(salon_id))

    def populateServices_table(self, salon_id):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select s.servicesID, s.duration, s.name, s.description, s.price from services as s join salon_serv ss on ss.servicesID = s.servicesID where ss.salonID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (salon_id))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.service.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.service.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.service.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def addService(self, salon_id):

        pass

    def deleteService(self, salon_id):
        servRow = self.service.currentRow()
        servID = int(self.service.item(servRow, 0).text())
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Services WHERE servicesID = ?", (servID,))
        connection.commit()
        sql_query = "delete from Salon_Serv where servicesID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (servID))
        connection.commit()
        
        confirm = QMessageBox()
        confirm.setText("This service has been deleted.")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()
        self.appointment.removeRow(servRow)
        connection.close()



class MonthlyReportWindow(QMainWindow):
    def __init__(self,employee_id, salon_id ):
        super(MonthlyReportWindow, self).__init__()
        loadUi('MonthlyReport2.ui', self)

        # self.employee_id = employee_id
        # self.salon_id = salon_id


        # Autofill fields
        # self.lineEdit.setText(str(employee_id))
        self.lineEdit_2.setText(str(salon_id))
        self.lineEdit_3.setText(self.getSalonName(salon_id))
        self.lineEdit_9.setText(QDate.currentDate().toString("MMMM"))
        self.lineEdit_10.setText(str(QDate.currentDate().year()))
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        # Populate other details
        self.monthRep.clicked.connect(lambda: self.populateDetails(salon_id))

        # Connect buttons
        self.Confirm.clicked.connect(self.confirm)
        self.Confirm_2.clicked.connect(self.goBack)

    def getSalonName(self, salon_id):
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query = "SELECT name FROM Salons WHERE SalonID = ?"
        cursor.execute(sql_query, salon_id)
        result = cursor.fetchone()

        connection.close()

        if result:
            return result[0]
        else:
            return ""

    def populateDetails(self, salon_id):
        month = self.lineEdit_9.text()
        month_mapping = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

        # Convert month name to numeric value
        month_numeric = month_mapping.get(month, 1) 
        # self.lineEdit_9.setText(QDate.currentDate().toString("MMMM"))
        # month = self.lineEdit_9.toString("MMMM")
        
        year = int(self.lineEdit_10.text())
        # Total No. Of Appointments
        total_appointments = self.getTotalAppointments(salon_id, month_numeric, year)
        self.lineEdit_4.setText(str(total_appointments))

        # Total Profit
        total_profit = self.getTotalProfit(salon_id, month_numeric, year)
        self.lineEdit_5.setText(str(total_profit))

        # Average Rating
        average_rating = self.getAverageRating(salon_id, month_numeric, year)
        self.lineEdit_6.setText(str(average_rating))
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setDisabled(True)
        
    def getTotalAppointments(self, salon_id, month, year):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "SELECT COUNT(*) FROM Appointment WHERE salonID = ? AND MONTH(date) = ? AND YEAR(date) = YEAR(GETDATE())"
        cursor.execute(sql_query, (salon_id, month))
        result = cursor.fetchone()[0]
        connection.close()
        return result
    
    def getTotalProfit(self, salon_id, month, year):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = """
            SELECT SUM(s.Price)
            FROM Appointment AS a
            JOIN Services AS s ON a.ServicesID = s.ServicesID
            WHERE a.salonID = ? AND MONTH(a.date) = ? AND YEAR(a.date) = YEAR(GETDATE())
        """
        cursor.execute(sql_query, (salon_id, month))
        result = cursor.fetchone()[0]
        connection.close()
        return result if result else 0
    
    def getAverageRating(self, salon_id, month, year):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        # sql_query = """
        #     SELECT AVG(Rating)
        #     FROM SalonRating
        #     WHERE salonID = ? AND MONTH(month) = ? AND YEAR(year) = YEAR(GETDATE())
        # """
        sql_query = """
    SELECT AVG(Rating)
    FROM SalonRating
    WHERE salonID = ? AND MONTH(CONVERT(date, [month] + ' 1 ' + CAST([year] AS VARCHAR(4)))) = ?
    AND YEAR(CONVERT(date, [month] + ' 1 ' + CAST([year] AS VARCHAR(4)))) = YEAR(GETDATE())
"""

        cursor.execute(sql_query, (salon_id, month))
        result = cursor.fetchone()[0]
        connection.close()
        return result if result else 0
    
    def confirm(self):
        QMessageBox.information(self, "Confirmation", "Monthly report details confirmed!")
        self.goBack()

    def goBack(self):
        self.hide()
        # self.inventory.clicked.connect(self.inventoryWindow)
        # self.update.clicked.connect(self.updateService)
        # self.monthlyRep.clicked.connect(self.monthlyReport)

class BookApptWindow(QMainWindow):
    def __init__(self, username, customerID):
        super(BookApptWindow, self).__init__()
        loadUi('BookAppointment.ui', self)
        
        # self.username = username
        # username = self.custname.text()
        self.findSalons.clicked.connect(lambda:self.populate_salonList_table())
        self.salonList.itemSelectionChanged.connect(self.getSelectedSalon)
        self.book.clicked.connect(lambda: self.bookConfirm(username,customerID))
        self.Cancel.clicked.connect(lambda: self.cancel(username))

    def cancel(self, username):
        self.bookAppOrView_window = BookApporViewWindow(username)
        self.bookAppOrView_window.show()

    def onRadioButtonToggled(self):
        # Determine which radio button is selected
        if self.COD.isChecked():
            payMeth = "Cash"
        elif self.credit.isChecked():
            payMeth = "Credit Card"
        elif self.debit.isChecked():
           payMeth = "Debit Card"
        return payMeth

    def bookConfirm(self, username, customerID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        stylistRow = self.stylist.currentRow()
        serviceRow = self.serviceList.currentRow()
        salonRow = self.salonList.currentRow()
        datee = self.stylist.item(stylistRow, 3).text()
        timee = self.stylist.item(stylistRow, 4).text()
        payMeth = self.onRadioButtonToggled()
    

        print(datee, timee)
        servicesID = int(self.serviceList.item(serviceRow, 0).text())
        employeeID = int(self.stylist.item(stylistRow, 1).text())
        salonID = int(self.salonList.item(salonRow, 0).text())
        print(customerID, datee, timee, servicesID, employeeID, salonID)

        sql_query = """INSERT INTO Appointment
    ([customerID], [date], [time], [servicesID], [employeeID], [salonID])
    VALUES (?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql_query, (customerID, datee,
                           timee, servicesID, employeeID, salonID))
        connection.commit()
        connection.close()
        self.bookConfirm_window = bookingConfirm(username,customerID, salonID, servicesID, employeeID, payMeth, datee, timee)
        self.bookConfirm_window.show()
        


    def populate_salonList_table(self):
        city = self.city.text()
        if city == "":
            confirm = QMessageBox()
            confirm.setText("Please enter your city.")
            confirm.setIcon(QMessageBox.Icon.Information)
            confirm.addButton(QMessageBox.StandardButton.Ok)
            confirm.exec()
        else:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            # sql_query = "Select s.salonID, s.name, sr.rating, s.plotno, s.streetno, s.city from salons s join salonrating sr on s.salonID = sr.salonID and city = ? "
            sql_query = """SELECT
    s.salonID,
    s.name,
    COALESCE(CAST(sr.rating AS VARCHAR), '-') AS rating,
    s.plotno,
    s.streetno,
    s.city
FROM
    salons s
LEFT JOIN
    salonrating sr ON s.salonID = sr.salonID
WHERE
    s.city = ?;"""
            # TODO: Write SQL query to fetch salons data
            cursor.execute(sql_query, (city))

            # Fetch all rows and populate the table
            for row_index, row_data in enumerate(cursor.fetchall()):
                self.salonList.insertRow(row_index)
                for col_index, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.salonList.setItem(row_index, col_index, item)
            # salonID = cursor.fetchall()[0]
            # Close the database connection
            connection.close()

            # Adjust the column widths for better display
            header = self.salonList.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        
    
    def getSelectedSalon(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        self.serviceList.setRowCount(0)
        self.stylist.setRowCount(0)
        salonRow = self.salonList.currentRow()
        salonID = int(self.salonList.item(salonRow, 0).text())
        self.populate_services_table(salonID)
        self.populate_stylist_table(salonID)
        


    def populate_services_table(self, salonID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select s.servicesID, s.name, s.description, s.price, s.duration from services as s join salon_serv as ss on ss.servicesID = s.servicesID and ss.salonID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (salonID))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.serviceList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.serviceList.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.serviceList.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def populate_stylist_table(self, salonID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select e.name, e.employeeID, e.Specialty, s.date, s.time from employee as e, availability as s where s.employeeID = e.employeeID and e.specialty != 'Manager' and e.salonID = ?"
        #SQL query to fetch stylists and their availability
        cursor.execute(sql_query, (salonID))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.stylist.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.stylist.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.stylist.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

class bookingConfirm(QMainWindow):
    def __init__(self, username, customerID, salonID, servicesID, employeeID, payMeth, datee, timee):
        super(bookingConfirm, self).__init__()
        loadUi('BookConfirmation.ui', self)

        self.setCustName(customerID)
        self.setSalonName(salonID)
        self.setServiceName(servicesID)
        self.setVals(datee, timee, payMeth)
        totalAmt = self.getTotAMT(servicesID)
        # apptID = self.getAppt(employeeID, customerID, salonID, servicesID,)

        self.name.setDisabled(True)
        self.salonName.setDisabled(True) 
        self.service.setDisabled(True) 
        self.date.setDisabled(True)
        self.time.setDisabled(True)
        self.charges.setDisabled(True)   
        self.paymeth.setDisabled(True)   
        

        # self.insertReceipt(apptID, customerID, salonID, servicesID, payMeth, int(totalAmt))
        self.confirm.clicked.connect(lambda: self.insertApp(customerID, datee,
                           timee, servicesID, employeeID, salonID, payMeth, totalAmt, username))
        self.back.clicked.connect(lambda: self.backToBook(username, customerID))
        # self.confirm.clicked.connect(lambda: self.viewAppt(username, customerID))
    def backToBook(self, username, customerID):
        bookingConfirm.close()
        self.bookApp_window = BookApptWindow(username, customerID)
        self.bookApp_window.show()

    def setVals(self, datee, timee, payMeth):
        self.date.setText(datee)
        self.time.setText(timee)
        self.paymeth.setText(payMeth)

    def setCustName(self, customerID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select name from customer where customerID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (customerID))
        result = cursor.fetchone()
        self.name.setText(result[0])

    def setSalonName(self, salonID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select name from salons where salonID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (salonID))
        result = cursor.fetchone()
        self.salonName.setText(result[0])

    def setServiceName(self, servicesID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select name from Services where servicesID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (servicesID))
        result = cursor.fetchone()
        self.service.setText(result[0])

    def getTotAMT(self, servicesID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select price from services where servicesID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (servicesID))
        result = cursor.fetchone()
        self.charges.setText(str(result[0]))
        return result[0]
    
    def insertApp(self, customerID, datee,timee, servicesID, employeeID, salonID, payMeth, totalAmt, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = """INSERT INTO Appointment
    ([customerID], [date], [time], [servicesID], [employeeID], [salonID])
    VALUES (?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql_query, (customerID, datee,
                           timee, servicesID, employeeID, salonID))
        connection.commit()
        connection.close()
        self.getAppt(employeeID, customerID, salonID, servicesID, payMeth, totalAmt, username)
        
    
    def getAppt(self, employeeID, customerID, salonID, servicesID, payMeth, totalAmt, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select apptID from appointment where employeeID = ? and customerID = ? and salonID = ? and servicesID = ?"
        # SQL query to fetch AppointmentID
        cursor.execute(sql_query, (employeeID, customerID, salonID, servicesID))
        result = cursor.fetchone()
        apptID = result[0]
        self.insertReceipt(apptID, customerID, salonID, servicesID, payMeth, totalAmt, employeeID, username)
        # inserting receipt


    def insertReceipt(self, apptID, customerID, salonID, servicesID, payMeth, totalAmt, employeeID, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query =  """INSERT INTO Receipt
    ([apptID], [customerID], [PayMethod], [TotalAmt])
    VALUES (?, ?, ?, ?)"""

        cursor.execute(sql_query, (apptID, customerID,
                           payMeth, totalAmt))
        connection.commit()
        connection.close()
        
        confirm = QMessageBox()
        confirm.setText("Your appointment has been booked!")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()
        self.viewAppt(username, customerID)
        

    def viewAppt(self, username, customerID):
        self.viewAppt_Window = ViewApptWindow(username, customerID)
        self.viewAppt_Window.show()


class ViewApptWindow(QMainWindow):
    def __init__(self, username, customerID):
        super(ViewApptWindow, self).__init__()
        loadUi('ViewAppt.ui', self)

        self.populate_AppList_table(customerID)
        # self.appointment.itemSelectionChanged.connect(self.getSelectedApp())
        self.cancel.clicked.connect(lambda: self.cancelApp())
        # self.okButton.clicked.connect(lambda: self.clear())
        # self.backButton.clicked.connect(lambda: self.backtoApp(username, customerID))

    def populate_AppList_table(self, customerID):
        print("populate function")
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select a.apptID, a.customerID, a.employeeID, a.date, a.time, a.servicesID, a.salonID from appointment as a where a.customerID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, customerID)

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.appointment.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.appointment.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.appointment.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        
    def backtoApp(self, username, customerID):
        self.bookApp_window = BookApptWindow(username, customerID)
        self.bookApp_window.show()

    def cancelApp(self):
        print("cancel function")
        appRow = self.appointment.currentRow()
        appID = int(self.appointment.item(appRow, 0).text())
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Receipt WHERE apptID = ?", (appID,))
        connection.commit()
        sql_query = "delete from appointment where apptID = ?"
        # TODO: Write SQL query to fetch customers data
        cursor.execute(sql_query, (appID))
        connection.commit()
        
        confirm = QMessageBox()
        confirm.setText("Your appointment has been cancelled.")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()
        self.appointment.removeRow(appRow)
        connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    app.exec()

