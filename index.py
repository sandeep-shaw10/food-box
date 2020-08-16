import mysql.connector
import stdiomask
from datetime import datetime

"""LOGIN AND REGISTRATION OF USER AND ADMIN  WITH VALIDATION AND CHECKING----------------------------------------------------------------------"""

"""validate new password account----------"""
def validate(name,password):
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    sql_check='Select * from user_table where user_password = %s'
    x=(password, )
    mycursor.execute(sql_check,x)
    result = mycursor.fetchall()
    if result:
        print("INVALID : Weak password ! ")
        return 0
    else:
        if(len(name)<=3):
            print("INVALID : Name too short !")
            return 0
        elif(len(name)>=64):
            print("INVALID : Name too long !")
            return 0
        elif(len(password)<=3):
            print("INVALID : password too short !")
            return 0
        elif(len(password)>=64):
            print("INVALID : password too long !")
            return 0
        elif(x==0):
            print("INVALID : your password is weak")
            return 0
        else:
            return 1

"""check login-----------------------------"""
def check_login(name,password):
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    sql_check='Select * from user_table where (username, user_password) = (%s,%s)'
    x=(name, password, )
    mycursor.execute(sql_check,x)
    result = mycursor.fetchall()
    if result:
        print("------>>>>   Logged in succesfully")
    else:
        print("                 >< Access denied ><")
        print("                 TRY AGAIN")
        user_login()

"""check admin login-----------------------"""
def check_adlogin(name,password):
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    sql_check='Select * from admin_table where (name, password) = (%s,%s)'
    x=(name, password, )
    mycursor.execute(sql_check,x)
    result = mycursor.fetchall()
    if result:
        print("            **  Logged in succesfully  **      ")
    else:
        print("                 >< Access denied ><")
        print("                 TRY AGAIN")
        admin_login()

""" Registration portal--------------------"""
def register_login():
    print("-----------------------------------")
    print("WELCOME TO USER REGISTRATION")
    print("PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("ENTER YOUR CHOICE : ")
    if(permission=='1'):
        print("-----------------------------------")
        print("CREATE YOUR USER ACCOUNT ")
        name = raw_input("ENTER NAME : ")
        print("CREATE YOUR USER PASSWORD")
        password = stdiomask.getpass(prompt="ENTER PASSWORD : ")
        proceed=validate(name,password)
        if(proceed==1):
            mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
            mycursor = mydb.cursor()
            sql_form = "Insert into user_table(username,user_password) values(%s,%s)"
            add_admin = [(name, password)]
            mycursor.executemany(sql_form, add_admin)
            mydb.commit()
            print('Your account Registered succesfully')
            user_login()
        else:
            print("------------WARNING  :  TRY AGAIN   ----------------")
            register_login()
    else:
        main()

"""user login------------------------------"""
def user_login():
    print("+------------------WELCOME TO USER LOGIN------------------+")
    print("|---------------------------------------------------------|")
    print("+          PRESS 0 TO DISCONTINUE AND 1 TO PROCEED        +")
    permission=raw_input("                 ENTER YOUR CHOICE : ")
    if(permission=='1'):
        print("|---------------------------------------------------------|")
        name = raw_input("              ENTER NAME : ")
        password = stdiomask.getpass(prompt="              ENTER PASSWORD : ")
        print("|---------------------------------------------------------|")
        check_login(name,password)
        mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
        mycursor = mydb.cursor()
        sql_check='Select * from user_table where (username, user_password) = (%s,%s)'
        x=(name, password, )
        mycursor.execute(sql_check,x)
        result = mycursor.fetchall()
        name = name.title().split()
        name = name[0]
        user_panel(name,result[0][0])
    else:
        main()

"""admin_login-----------------------------"""
def admin_login():
    print("|              WELCOME TO ADMIN LOGIN              |\n+--------------------------------------------------+")
    print("     PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("     ENTER YOUR CHOICE : ")
    print("+--------------------------------------------------+")
    if(permission=='1'):
        name = raw_input("     ENTER NAME : ")
        password = stdiomask.getpass(prompt="     ENTER PASSWORD : ")
        print("+--------------------------------------------------+")
        check_adlogin(name,password)
        name = name.title().split()
        name = name[0]
        admin_panel(name)
    else:
        main()

"""SETUP OF ADMIN PANEL TO VIEW AND ALTER FOOD DATA AND KEEP AN ACCOUNT ON SALES----------------------------------------------------------------"""

def admin_panel(name):
    print("\n--------------------ADMIN PANEL--------------------")
    print("**                  Welcome "+name+"            **")
    print("+-------------------------------------------------+")
    print("|     VIEW STOCK : Press 'V' to Check Stock       |")
    print("|   CREATE STOCK : Press 'C' to Add Stock         |")
    print("|   MODIFY STOCK : Press 'M' to Update Stock      |")
    print("|   DELETE STOCK : Press 'D' to Delete Stock      |")
    print("| SALES ANALYSIS : Press 'S' to View Sales        |")
    print("|         LOGOUT : Press 'L' to Logout            |")
    print("+-------------------------------------------------+")
    command=raw_input("ENTER COMMAND : ")
    print("+-------------------------------------------------+")
    if(command=='V' or command=='v'):
        view_stock(name,1,0)
    elif(command=='C' or command=='c'):
        add_stock(name)
    elif(command=='M' or command=='m'):
        update_stock(name)
    elif(command=='D' or command=='d'):
        del_stock(name)
    elif(command=='S' or command=='s'):
        view_sales(name)
    elif(command=='L' or command=='l'):
        print("Lougout Succesfully")
        main()
    else:
        print("+---------------------------------------------------------+")
        print("|                      ABOUT US                           |") 
        print("+---------------------------------------------------------+")
        print("| Address | 23/1/H/17 Cossipore Road, Kolkata, WestBengal |")
        print("+---------------------------------------------------------+")
        print("|   Email | foodshop@business.org                         |")
        print("+---------------------------------------------------------+")
        print("|   Phone | +91 98353378628                               |")
        print("+---------------------------------------------------------+")
        
#view stock for user and admin
def view_stock(name,type,id):
    print("\n--------------------------------------CURRENT STOCK-------------------------------------------")
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from stock_table")
    myresult = mycursor.fetchall()
    print("Food Number\t\t\tName\t\t\tType\t\t\tPRICE\t\t\tStock")
    for x in myresult:
        print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(x[1],x[2],x[3],x[4],x[5]))
    print("\n----------------------------------------------------------------------------------------------")
    print("Search Stock : Press 'S' ")
    print("      Logout : Press 'L' ")    
    print("        Back : Press any button ")
    ch=raw_input("Enter your Choice : ")
    print("------------------------------------------------------------------------------------------------")
    if(ch=='l' or ch=='L'):
        print("         **  Lougout Succesfully **")
        main()
    elif(ch=='S' or ch=='s'):
        search=raw_input("ENTER THE FOOD NUMBER : ")
        mycursor.execute("Select * from stock_table where num = %s",(search,))
        display = mycursor.fetchall()
        count = mycursor.rowcount
        if(count==0):
            print("Item does not exist")
            if(type==1):
                admin_panel(name)
            else:
                user_panel(name,id)
        else:
            print("Food Exist")
            for y in display:
                print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(y[1],y[2],y[3],y[4],y[5]))
                if(type==1):
                    admin_panel(name)
                else:
                    user_panel(name,id)
    else:
        print("Not executed {}".format(ch))
        if(type==1):
            admin_panel(name)
        else:
            user_panel(name,id)

#adding item to by admin 
def add_stock(name):
    print('--------------------ADD STOCK-----------------------')
    print("PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("ENTER YOUR CHOICE : ")
    print("       ------------------------------------")
    if(permission=='1'):
        mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
        mycursor = mydb.cursor()
        f_num=raw_input("  FOOD NUMBER : ")
        mycursor.execute("Select * from stock_table where num = %s",(f_num,))
        check=mycursor.fetchall()
        if(not check):
            f_name=raw_input("  FOOD NAME : ")
            print("1-> South Indian\t2-> North Indian\t3-> Chinese\tAny other key->Continental")
            f_type=raw_input("  FOOD TYPE : ")
            if(f_type=='1'):
                f_type="South Indian"
            elif(f_type=='2'):
                f_type="North Indian"
            elif(f_type=='3'):
                f_type="Chinese"
            else:
                f_type="Continental"
            f_price=int(raw_input("  FOOD PRICE : "))
            f_stock=int(raw_input("  FOOD STOCK : "))
            mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
            mycursor = mydb.cursor()
            sql_val = "Insert into stock_table(num, name, type, price, quantity) values(%s,%s,%s,%s,%s)"
            value = [(f_num,f_name,f_type,f_price,f_stock)]
            mycursor.executemany(sql_val, value)
            mydb.commit()
            print("    **  ITEM SUCCESSFULLY ADDED  **")
            view_stock(name,1,0)
        else:
            print("     **  FOOD NUMBER ALREADY EXIST ! {}  **".format(check))
            admin_panel(name)
    else:
         admin_panel(name)

#updating item by admin
def update_stock(name):
    print('+----------------UPDATE STOCK-------------------+')
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from stock_table")
    myresult = mycursor.fetchall()
    print("Food Number\t\t\tName\t\t\tType\t\t\tPRICE\t\t\tStock")
    for x in myresult:
        print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(x[1],x[2],x[3],x[4],x[5]))
    print("------------------------------------------------------------------")
    print("PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("ENTER YOUR CHOICE : ")
    print("------------------------------------------------------------------")
    if(permission=='1'):
        f_num=raw_input("  FOOD NUMBER : ")
        mycursor.execute("Select * from stock_table where num = %s",(f_num,))
        check=mycursor.fetchall()
        if(check):
            new_num=raw_input("  SET FOOD NUMBER : ")
            f_name=raw_input("FOOD NAME : ")
            print("1-> South Indian\t2-> North Indian\n3-> Chinese\tAny other key->Continental")
            f_type=raw_input("  FOOD TYPE : ")
            if(f_type=='1'):
                f_type="South Indian"
            elif(f_type=='2'):
                f_type="North Indian"
            elif(f_type=='3'):
                f_type="Chinese"
            else:
                f_type="Continental"
            f_price=int(raw_input("  FOOD PRICE : "))
            f_stock=int(raw_input("  FOOD STOCK : "))
            mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
            mycursor = mydb.cursor()
            sql_val = "Update stock_table set num=%s , name=%s , type=%s , price=%s, quantity=%s where num=%s"
            value = [(new_num,f_name,f_type,f_price,f_stock,f_num)]
            mycursor.executemany(sql_val, value)
            mydb.commit()
            print("         **  ITEM UPDATED SUCCESSFULLY ADDED **")
            print("------------------------------------------------------------------")
            update_stock(name)
        else:
            print("         **  FOOD NUMBER DON'T EXIST !   **")
            admin_panel(name)
    else:
         admin_panel(name)

#deleting item by admin
def del_stock(name):
    print('-------------------------DELETE STOCK-----------------------------')
    print("     PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("      ENTER YOUR CHOICE : ")
    print("------------------------------------------------------------------")
    if(permission=='1'):
        mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
        mycursor = mydb.cursor()
        del_num=raw_input("Enter the food number that you want to delete : ")
        del_num=del_num.upper()
        mycursor.execute("Select * from stock_table where num = %s",(del_num,))
        check=mycursor.fetchall()
        if(check):
            mycursor.execute("Delete from stock_table where num = %s",(del_num,))
            mydb.commit()
            print("         **  ITEM DELETED SUCCESSFULLY   **")
            view_stock(name,1,0)
        else:
            print("         **  FOOD NUMBER DON'T EXIST ! {}    **".format(check))
            admin_panel(name)
    else:
        admin_panel(name)

#viewing sales by admin
def view_sales(name):
    print("\n------------------------------------------------------FOOD-BOX DAILY TRANSACTION------------------------------------------------------\n")
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from sales_table")
    check=mycursor.fetchall()
    if(check):
        for col in check:
            print(" {}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{} ".format(col[3],col[4],col[5],col[6],col[7],col[8],col[2]))   
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print("              DAILY SALES : PRESS 'D' \n              BACK : ANY OTHER CHARACTER")
        back = raw_input("              ENTER YOUR CHOICE : ")
        if(back.upper()=='D'):
            print("\n---------------FOOD-BOX DAILY SALES---------------\n")
            mycursor.execute("Select date(date) as date, sum(quantity) as total_sales, sum(amount) as income from sales_table group by date")
            check = mycursor.fetchall()
            if(check):
                for col in check:
                    mycursor.execute("Insert into daily_sales(date,sold,income) values(%s,%s,%s)",(col[0],col[1],col[2],))
                    mydb.commit()
                mycursor.execute("Select date(date) as date, sum(sold) as total_sales, sum(income) as income from daily_sales group by date")
                display = mycursor.fetchall()
                print("+---------------+---------------+--------------+")
                print("|      DATE     |    QUANTITY   |    INCOME    |")
                print("+---------------+---------------+--------------+")
                for val in display:
                    print("|  {}\t|\t{}\t|\t{}   |".format(val[0],val[1],val[2]))
                print("+---------------+---------------+--------------+")
                mycursor.execute("Truncate table daily_sales")
                admin_panel(name)
            else:
                print("                NO TRANSACTION TILL NOW")
                admin_panel(name)
        else:
            admin_panel(name)
    else:
        print("                     NO TRANSACTION TIL NOW")
        admin_panel(name)
    

"""SETUP OF USER PANEL TO VIEW AND ALTER FOOD DATA AND KEEP AN ACCOUNT ON SALES----------------------------------------------------------------"""
def user_panel(name,id):
    print("+------------------USER PANEL------------------+")
    print("**              Welcome "+name+"         **")
    print("|           MENU : Press S to view stock       |")
    print("|      VIEW CART : Press V to view Cart        |")
    print("|   ORDERCONFIRM : Press C to Confirm Order    |")
    print("|         LOGOUT : Press L to logout           |")
    print("+----------------------------------------------+")
    command=raw_input("ENTER COMMAND : ")
    print("+----------------------------------------------+")
    if(command=='S' or command=='s'):
         view_stock(name,0,id)
    elif(command=='V' or command=='v'):
        view_cart(name,id)
    elif(command=='C' or command=='c'):
        user_order(name,id)
    elif(command=='L' or command=='l'):
        print("             **  Lougout Succesfully  **")
        main()
    else:
        print("+---------------------------------------------------------+")
        print("|                      ABOUT US                           |") 
        print("+---------------------------------------------------------+")
        print("| Address | 23/1/H/17 Cossipore Road, Kolkata, WestBengal |")
        print("+---------------------------------------------------------+")
        print("|   Email | foodshop@business.org                         |")
        print("+---------------------------------------------------------+")
        print("|   Phone | +91 98353378628                               |")
        print("+---------------------------------------------------------+")

#viewing individual cart
def view_cart(name,id):
    print("-------------------------Welcome {} to your Cart--------------------------".format(name))
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from user_cart where user_id = %s",(id,))
    myresult = mycursor.fetchall()
    if(myresult):
        i=0
        for x in myresult:
            item_num = myresult[i][2]
            i+=1
            mycursor.execute("Select * from stock_table where num = %s",(item_num,))
            stock = mycursor.fetchall()
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(x[2],stock[0][2],stock[0][3],stock[0][4],x[3],x[4]))
        print("\n------------------------------------------------------------------")
    else:
        print("No item added to cart")       
    print("+---------------------------------------------------------+")    
    print("         ADD TO CART : PRESS 'A' ")
    print("    REMOVE FROM CART : PRESS 'R' ")
    print("RETURN TO USER PANEL : PRESS ANY OTHER BUTTON")
    choice = raw_input("   ENTER YOUR CHOICE : ")
    if(choice.upper()=='A'):
        add_cart(name,id)
    elif(choice.upper()=='R'):
        del_cart(name,id)
    else:
        user_panel(name,id)

#adding individual cart
def add_cart(name,id):
    print('----------------SELECT ITEM TO ADD TO CART-------------------')
    print("\n--------------------------------------")
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from stock_table")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(x[1],x[2],x[3],x[4],x[5]))
    print("\n------------------------------------------------------------------")
    print("PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("ENTER YOUR CHOICE : ")
    print("+---------------------------------------------------------+")
    if(permission=='1'):
        f_num=raw_input("FOOD NUMBER : ")
        mycursor.execute("Select * from stock_table where num = %s",(f_num,))
        check=mycursor.fetchall()
        if(check):
            dish=check[0][2]
            left=check[0][5]
            cost=check[0][4]
            print("{} has only {} stock available".format(dish,left))
            quantity=int(raw_input("ENTER THE QUANTITY : "))
            if(quantity<=left):
                amt = quantity*cost
                sql_form = "Insert into user_cart(user_id,item_num,quantity,price) values(%s,%s,%s,%s)"
                add = [(id,f_num,quantity,amt)]
                mycursor.executemany(sql_form, add)
                mydb.commit()
                print("ITEM IS SUCCESSFULLY ADDED TO THE CART ")
                add_cart(name,id)
            else:
                print("STOCK IS LESS")
                add_cart(name,id)
        else:
            print("FOOD NUMBER DON'T EXIST ! ")
            add_cart(name,id)
    else:
        user_panel(name,id)

#removing from cart
def del_cart(name,id):
    print("------------------------------------------ENTER THE FOOD NUMBER THAT YOU WANT TO DELETE--------------------------------------------")
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from user_cart where user_id = %s",(id,))
    myresult = mycursor.fetchall()
    if(myresult):
        i=0
        for x in myresult:
            item_num = myresult[i][2]
            i+=1
            mycursor.execute("Select * from stock_table where num = %s",(item_num,))
            stock = mycursor.fetchall()
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(x[2],stock[0][2],stock[0][3],stock[0][4],x[3],x[4]))
        print("\n------------------------------------------------------------------")
    else:
        print("No item added to cart")
        print("\n------------------------------------------------------------------")
    print("PRESS 0 TO DISCONTINUE AND 1 TO PROCEED ")
    permission=raw_input("ENTER YOUR CHOICE : ")
    print("+---------------------------------------------------------+")
    if(permission=='1'):
        f_num=raw_input("FOOD NUMBER : ")
        mycursor.execute("Select * from user_cart where item_num = %s",(f_num,))
        check=mycursor.fetchall()
        if(check):
            mycursor.execute("Delete from user_cart where item_num = %s",(f_num,))
            mydb.commit()
            print("ITEM IS SUCCESSFULLY DELETED FROM THE CART ")
            del_cart(name,id)
        else:
            print("SUCH FOOD NUMBER DON'T EXIST IN YOUR CART ")
            del_cart(name,id)
    else:
        user_panel(name,id)

#ordering element from the cart
def user_order(name,id):
    print("----------------------Welcome {} to the Order Section------------------------------".format(name))
    mydb = mysql.connector.connect(host="localhost", user="root",password="",database="sample")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from user_cart where user_id = %s",(id,))
    myresult = mycursor.fetchall()
    if(myresult):
        i=0
        for x in myresult:
            item_num = myresult[i][2]
            i+=1
            mycursor.execute("Select * from stock_table where num = %s",(item_num,))
            stock = mycursor.fetchall()
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(x[2],stock[0][2],stock[0][3],stock[0][4],x[3],x[4]))
        print("\n------------------------------------------------------------------")
        order=raw_input("ENTER (Yes) TO CONFIRM THE ORDER : ")
        order = order.upper()
        print(order)
        if(order=='YES'):
            mycursor.execute("Select * from user_cart where user_id = %s",(id,))
            myresult = mycursor.fetchall()
            i=0
            money=0
            for sl in myresult:
                f_num=sl[2]
                mycursor.execute("Select * from stock_table where num = %s",(f_num,))
                stock = mycursor.fetchall()
                f_name=stock[0][2]
                f_quantity=sl[3]
                f_price=stock[0][4]
                amt= f_quantity*f_price
                money+=amt
                if(f_quantity<=stock[0][5]):
                    # Adding ordered stock to sales tables
                    sql_form = "Insert into sales_table(user_id,orderby,number,name,quantity,price,amount) values(%s,%s,%s,%s,%s,%s,%s)"
                    add = [(id,name,f_num,f_name,f_quantity,f_price,amt)]
                    mycursor.executemany(sql_form, add)
                    mydb.commit()
                    i+=1
                    # Removing Stock from Stock_tables
                    stock_left = stock[0][5] - f_quantity
                    if(stock_left==0):
                        mycursor.execute("Delete from stock_table where num = %s",(f_num,))
                    else:
                        mycursor.execute("Update stock_table set quantity=%s where num=%s",(stock_left,f_num,))
                        mydb.commit()
                    #Emptying the cart
                    #mycursor.execute("Delete from user_cart where user_id = %s",(id,))
                #for worst case scenario
                else:
                    # Adding ordered stock to sales tables
                    sql_form = "Insert into sales_table(user_id,orderby,number,name,quantity,price,amount) values(%s,%s,%s,%s,%s,%s,%s)"
                    add = [(id,name,f_num,f_name,stock[0][5],f_price,amt)]
                    mycursor.executemany(sql_form, add)
                    mydb.commit()
                    i+=1
                    mycursor.execute("Delete from stock_table where num = %s",(f_num,))
                    #Emptying the cart
                    #mycursor.execute("Delete from user_cart where user_id = %s",(id,))
                    print("HIGH DEMAND OF {} ONLY {} PCS. ORDERED".format(f_name,stock[0][5]))
            #Billing 
            date = datetime.today().strftime("%B %d, %Y")
            time = datetime.now().strftime("%H:%M:%S")
            now = datetime.today().strftime("%d/%m/%Y")
            print("\nINVOICE BILLING : FOOD-BOX\nName : {}\nDate : {}\nTime : {}\nTotal Amount = RS. {}".format(name,date,time,money))
            print("Bill inserted")
            mycursor.execute("Insert into ordered(user_id,money,day) values(%s,%s,%s)",(id,money,now))
            print("Cart deleted")
            print(id)
            mycursor.execute("Delete from user_cart where user_id = %s",(id,))
            mydb.commit()
            user_panel(name,id)
        else:
            user_panel(name,id)
    else:
        print("***********Nothing to order from the cart***********")
        print("\n------------------------------------------------------------------")
        add_cart(name,id)

""" Starting of the page -->  Home page -------------------------------------------------------------------------------------------------------"""
def main():
    print("\n+--------------------------------------------------+")
    print("|---------WELCOME TO FOOD BOX SAMLE ENTRY----------|")
    print("|              'BOOST YOUR APPETITE'               |\n+--------------------------------------------------+")
    print("|    Admin : Enter A to Admin Login                |")
    print("|     User : Enter U to User Login                 |")
    print("| Register : Enter R to User Registration          |")
    print("|     Exit : Enter X to exit                       |")
    print("| About us : Enter any other key                   |")
    print("+--------------------------------------------------+")
    val=raw_input("ENTER YOUR CHOICE : ")
    print("+--------------------------------------------------+")
    if(val=='A' or val=='a'):
        admin_login()
    elif(val=='U' or val=='u'):
        user_login()
    elif(val=='R' or val=='r'):
        register_login()
    elif(val=='X' or val=='x'):
        exit()
    else:
        print("+---------------------------------------------------------+")
        print("|                      ABOUT US                           |") 
        print("+---------------------------------------------------------+")
        print("| Address | 23/1/H/17 Cossipore Road, Kolkata, WestBengal |")
        print("+---------------------------------------------------------+")
        print("|   Email | foodshop@business.org                         |")
        print("+---------------------------------------------------------+")
        print("|   Phone | +91 98353378628                               |")
        print("+---------------------------------------------------------+")
main()

