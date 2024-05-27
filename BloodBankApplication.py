# ======================= libraries for project requirement =================================

import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import networkx as nx
import matplotlib.pyplot as plt

#=============== to connect to SQL Server databasec================================
def connect_to_database(server, database):
    try:
        # Establish a connection to the database
        conn = pyodbc.connect(Driver='{SQL Server}',
                              Server=server,
                              Database=database,
                              Trusted_Connection='yes')
        print("Successfully connected to the database.")
        return conn
    except pyodbc.Error as e:
        print("Error connecting to the database:", e)
        return None

# ============================= universal arrays ===================================
id_array= []
name_array= []
email_array =[]
contact_array =[]
bgroup_array =[]
pass_array =[]

# ================================ Functions ================================ 

connection = connect_to_database('DESKTOP-5ETADPF\\SQLEXPRESS', 'BloodBanKApplication')
if connection:
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Reg')
    results = cursor.fetchall()
    for row in results:
      id_array.append(row[0]) 
      email_array.append(row[4]) 
      name_array.append(row[1]) 
      bgroup_array.append(row[3]) 
      contact_array.append(row[2]) 
      pass_array.append(row[5]) 

def insert_data():
    connection = connect_to_database('DESKTOP-5ETADPF\\SQLEXPRESS', 'BloodBanKApplication')
    bottle= 0
    if connection:
        cursor = connection.cursor()
        query = f"INSERT INTO reg (ID, Name,Contact, BloodGroup,Email, Password,bottle) VALUES ('{id_entry_reg.get()}', '{name_entry_reg.get()}', '{contact_entry_reg.get()}', '{blood_group_entry_reg.get()}' ,'{email_entry_reg.get()}', '{password_entry_reg.get()}','{bottle}')"
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("info","Data inserted successfully.") 
        panel1.tkraise()
        cursor.close()

def user():
    login_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
    mainP.place_forget()

def admin():
    admin_login.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
    mainP.place_forget()

def show_graph():
    create_graph()
    plt.show()

def exit_form():
    root.destroy()

def logout():
    # Show a confirmation dialog
    confirm_logout = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm_logout:
        mainP.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.4, anchor="center")        
        admin_frame.place_forget()
        
def logout_d():
    # Show a confirmation dialog
    confirm_logout = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm_logout:
        mainP.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.4, anchor="center")        
        donor.place_forget()
        
def logout_a():
    # Show a confirmation dialog
    confirm_logout = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm_logout:
        mainP.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.4, anchor="center")        
        acceptor.place_forget()
    
def admin_l():
    # Get the email and password from entry widgets of admin_login frame
    email = email_entry_A1.get()
    password = password_entry_A1.get()
    print(email , password)
    # Check if the email and password match the predefined values
    if email == "ali@gmail.com" and password == "12345":
        # Display the admin frame
        admin_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
        # Hide the admin login frame
        admin_login.place_forget()
    else:
        # Show error message if email or password is incorrect
        print("Error", "Incorrect email or password")

def show_panel(panel):
    panel.tkraise()

def delete_row():
    selected_item = tree.selection()
    if selected_item:
        selected_id = tree.item(selected_item, "values")[0]
        selected_name = tree.item(selected_item, "values")[1]

        print(selected_id,selected_name)   
        cursor.execute(f"DELETE FROM Reg WHERE ID ={selected_id} AND Name ='{selected_name}'")
        connection.commit()

        # Delete the selected row from the Treeview
        tree.delete(selected_item)
    else:
        tk.messagebox.showerror("Error", "Please select a row to delete.")


#================================== Create the main window ===============================================

root = tk.Tk()
root.minsize(800, 450)
root.maxsize(800, 450)
root.title("Blood Bank Application")



#================================= background image =====================================

background_image = Image.open("images/bg1.jpg")
background_image = background_image.resize((800, 450))  
photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




# ==================================== main page ================================================

mainP = tk.Frame(root, bg="white", bd=5)
mainP.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.4, anchor="center")

label = tk.Label(mainP, text="Welcome ! to our Blood Bank Application", fg="white", bg="black", font="Arial 15 bold")
label.pack(fill="x")

admin_button = tk.Button(mainP, text="login as admin", padx=20, pady=3, bg="red", font=20, foreground="white", command=admin)
admin_button.place(x=80, y=100)

user_button = tk.Button(mainP, text="login as user", padx=20, pady=3, bg="red", font=20, foreground="white",command=user)
user_button.place(x=240, y=100)








# =================================== admin login =======================================

admin_login = tk.Frame(root, bg="white", bd=5)

label = tk.Label(admin_login, text="ADMIN LOGIN", fg="white", bg="black", font="Arial 25 bold")
label.pack(fill="x")

email_label1 = tk.Label(admin_login, text="Email:")
email_label1.place(x=150, y=80)
email_entry_A1 = ttk.Entry(admin_login)
email_entry_A1.place(x=250, y=80, width=200)

password_label1 = tk.Label(admin_login, text="Password:")
password_label1.place(x=150, y=120)
password_entry_A1 = ttk.Entry(admin_login)
password_entry_A1.place(x=250, y=120, width=200)

adminbtn = tk.Button(admin_login, text="Login", padx=20, pady=3, bg="red", font=20, foreground="white",command=admin_l)
adminbtn.place(x=140, y=190)

exit_button_login = tk.Button(admin_login, text="Exit", padx=20, pady=3, bg="red", font=20, foreground="white",command=exit_form )
exit_button_login.place(x=340, y=190)






# ====================================== admin frame =============================================

admin_frame = tk.Frame(root, bg="white", bd=5)

label = tk.Label(admin_frame, text="ADMIN PANEL", fg="white", bg="black", font="Arial 25 bold")
label.pack(fill="x")


# =========== dashboard ==================
sidebar_frame = tk.Frame(admin_frame, bg="red", width=100)
sidebar_frame.pack(side="left", fill="y")

dashboard_frame = tk.Frame(admin_frame ,bg="white" , width=400 )
dashboard_frame.pack()




#===== panel :1 =====
panel1 = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(panel1, text="Home", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")

tree = ttk.Treeview(panel1, columns=("ID", "Name", "Contact", "Blood Group", "Email"), show="headings")
tree.pack(side="left", fill="both", expand=True)

# Define column heading
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Contact", text="Contact")
tree.heading("Blood Group", text="Blood Group")
tree.heading("Email", text="Email")

# Set column widths
tree.column("ID", width=30)
tree.column("Name", width=120)
tree.column("Contact", width=100)
tree.column("Blood Group", width=30)
tree.column("Email", width=150)

for i in range(len(id_array)):
    tree.insert("", "end", values=(id_array[i], name_array[i], contact_array[i], bgroup_array[i], email_array[i]))

delete_button = tk.Button(panel1, text="Delete", command=delete_row)
delete_button.pack(side="bottom")

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(panel1, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")

# Configure the treeview to work with the scrollbar
tree.configure(yscrollcommand=scrollbar.set)



#===== panel2 =====
panel2 = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(panel2, text="User Registration", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")

email_label = tk.Label(panel2, text="email:", bg="white")
email_label.place(x=50, y=40)
email_entry_reg = ttk.Entry(panel2)
email_entry_reg.place(x=150, y=40 , width=200)

id_label = tk.Label(panel2, text="ID:", bg="white")
id_label.place(x=50, y=70)
id_entry_reg = ttk.Entry(panel2)
id_entry_reg.place(x=150, y=70, width=200)

name_label = tk.Label(panel2, text="Name:", bg="white")
name_label.place(x=50, y=100)
name_entry_reg = ttk.Entry(panel2)
name_entry_reg.place(x=150, y=100, width=200)

blood_group_label = tk.Label(panel2, text="Blood Group:", bg="white")
blood_group_label.place(x=50, y=130)
options = ["A+", "AB+", "O+", "B+","A-", "AB-", "O-", "B-"]
blood_group_entry_reg = ttk.Combobox(panel2, values=options)
blood_group_entry_reg.place(x=150, y=130, width=200)

contact_label = tk.Label(panel2, text="Contact:", bg="white")
contact_label.place(x=50, y=160)
contact_entry_reg = ttk.Entry(panel2)
contact_entry_reg.place(x=150, y=160 , width=200)

password_label = tk.Label(panel2, text="password:", bg="white")
password_label.place(x=50, y=190)
password_entry_reg = ttk.Entry(panel2)
password_entry_reg.place(x=150, y=190 , width=200)

save_button = ttk.Button(panel2, text="Save User" , command=insert_data)
save_button.place(x=70, y=220)

exit_button = ttk.Button(panel2, text="Exit", command=exit_form)
exit_button.place(x=170,y=220)



# ====panel 3 ======

panel3 = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(panel3, text="History", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")


show_graph = tk.Button(panel3, text="Show Graph", command=show_graph)
show_graph.pack(pady=10)


def create_graph():

    G = nx.DiGraph()
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Reg')
    results = cursor.fetchall()
    for row in results:
        name = row[1]
        blood_group = row[3]
        G.add_node(name, type='name')
        G.add_node(blood_group, type='blood_group')
        G.add_edge(name, blood_group)
    # Define colors for different types of nodes
    node_colors = {'name': 'lightblue', 'blood_group': 'lightgreen'}
    # Define node positions along parallel vertical lines
    pos = {}
    x_offsets = {'name': -0.5, 'blood_group': 0.5}
    for node_type in node_colors.keys():
        nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == node_type]
        for i, node in enumerate(nodes):
            pos[node] = (x_offsets[node_type], i)
    # Draw nodes for each type with different colors
    for node_type, color in node_colors.items():
        nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == node_type]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=color, node_size=2000, label=node_type)
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
    # Add a legend
    legend_patches = [plt.Circle((-1, -1), label=label, color=color) for label, color in node_colors.items()]
    plt.legend(handles=legend_patches, loc='best')
    # Add title
    plt.title("history Graph")
    plt.axis('off')

#===== griw view======
panel1.grid(row=0, column=0, sticky="nsew")
panel2.grid(row=0, column=0, sticky="nsew")
panel3.grid(row=0, column=0, sticky="nsew")

# ======= sidebar ===========
button1 = tk.Button(sidebar_frame, text="Home", command=lambda: show_panel(panel1))
button1.pack(fill="x", padx=10, pady=5)
button2 = tk.Button(sidebar_frame, text="User Registration", command=lambda: show_panel(panel2))
button2.pack(fill="x", padx=10, pady=5)
button3 = tk.Button(sidebar_frame, text="History", command=lambda: show_panel(panel3))
button3.pack(fill="x", padx=10, pady=5)
button4 = tk.Button(sidebar_frame, text="Logout", command=logout)
button4.pack(fill="x", padx=10, pady=5)







# ============================  user frames ==========================


# ================================= universal array ============================ 

id_array_d = []
email_array_d = []
name_array_d = []
bgroup_array_d = []
contact_array_d = []
pass_array_d = []
Bottle_array_d = []




# ============================================ donor frame functions =======================================

def showfilter():
    global id_array_d, email_array_d, name_array_d, bgroup_array_d, contact_array_d, pass_array_d
    compatibility = {
        "AB+": ["AB+"],
        "O+": ["A+", "B+", "AB+", "O+"],
        "A-": ["AB+", "AB-", "A+", "A-"],
        "A+": ["AB+", "A+"],
        "B-": ["B+", "B-", "AB+", "AB-"],
        "B+": ["AB+", "B+"],
        "AB-": ["AB+", "AB-"],
        "O-": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
    }
    profile = donor_function()
    donor_blood_group = profile[3]
    print(donor_blood_group)
    filtered_data = [x for x in results if x[3] in compatibility.get(donor_blood_group, [])]
    id_array_d.clear()
    email_array_d.clear()
    name_array_d.clear()
    bgroup_array_d.clear()
    contact_array_d.clear()
    pass_array_d.clear()
    print(filtered_data)
    for row in filtered_data:
        id_array_d.append(row[0])
        email_array_d.append(row[4])
        name_array_d.append(row[1])
        bgroup_array_d.append(row[3])
        contact_array_d.append(row[2])
        pass_array_d.append(row[5])
        Bottle_array_d.append(row[6])

    tree1 = ttk.Treeview(home_d, columns=("ID", "Name", "Contact", "Blood Group", "Email","Bottles"), show="headings")
    tree1.pack(expand=True, fill="both")
# Define column headings
    tree1.heading("ID", text="ID")
    tree1.heading("Name", text="Name")
    tree1.heading("Contact", text="Contact")
    tree1.heading("Blood Group", text="Blood Group")
    tree1.heading("Email", text="Email")
    tree1.heading("Bottles", text="Bottles")
# Set column widths
    tree1.column("ID", width=30)
    tree1.column("Name", width=100)
    tree1.column("Contact", width=90)
    tree1.column("Blood Group", width=30)
    tree1.column("Email", width=120)
    tree1.column("Bottles", width=40)
    for i in range(len(id_array_d)):
        tree1.insert("", "end", values=(id_array_d[i], name_array_d[i], contact_array_d[i], bgroup_array_d[i], email_array_d[i],Bottle_array_d[i]))
    scrollbar = ttk.Scrollbar(home_d, orient="vertical", command=tree1.yview)
    scrollbar.pack(side="right", fill="y")
    tree1.configure(yscrollcommand=scrollbar.set)
    
    



def create_graph2():
    users = []
    blood_groups = []
    bottle_counts = []
    for row in results:
        users.append(row[1])
        blood_groups.append(row[3])
        bottle_counts.append(row[6])

    # Create a directed graph
    G = nx.DiGraph()

    # Define node colors
    node_colors = {'users': 'lightblue', 'blood_groups': 'lightgreen', 'bottle_counts': 'red'}

    # Add nodes for users, blood groups, and bottle counts
    for user in users:
        G.add_node(user, type='users')
    for blood_group in blood_groups:
        G.add_node(blood_group, type='blood_groups')
    for count in bottle_counts:
        G.add_node(count, type='bottle_counts')

    for user, blood_group, count in zip(users, blood_groups, bottle_counts):
        G.add_edge(user, blood_group)
        G.add_edge(blood_group, count)

    # Define node positions
    pos = {node: (1, i) for i, node in enumerate(users)}
    pos.update({node: (2, i) for i, node in enumerate(blood_groups)})
    pos.update({node: (3, i) for i, node in enumerate(bottle_counts)})

    # Draw nodes and edges
    for node_type, color in node_colors.items():
        nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == node_type]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=color, node_size=2000, label=node_type)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    # Add a legend
    legend_patches = [plt.Circle((0, 0), label=label, color=color) for label, color in node_colors.items()]
    plt.legend(handles=legend_patches, loc='best')

    # Add title
    plt.title("Graph with Users, Blood Groups, and Bottle Counts")

    plt.axis('off')
    plt.show()

def donor_function():
    profile_details = []
    em = email_donor.get()
    password = password_donor.get()
    for row in results:
        if em == row[4]:
            profile_details=row
    if em not in email_array:
        return messagebox.showerror("Error", "No user found with this email.")
    if pass_array[email_array.index(em)] != password:
        return  messagebox.showerror("Error", "Incorrect password.")
    selected_indices = disease_combobox.curselection()
    selected_diseases = [disease_options[index] for index in selected_indices]
    for i in selected_diseases:
        if i == "none":
            donor.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
            login_frame.place_forget()
            break
        else:
            login_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
            messagebox.showerror("Error", "Sorry! You are not able to donate/accept blood.")
    return profile_details
    


def show_profile():
    profile_d.tkraise()
    profile_frame = tk.Frame(root)
    profile_frame.pack()
    profile_details = donor_function()
    if profile_details:
        label = tk.Label(profile_d, text=f"Id : {profile_details[0]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_d, text=f"Name: {profile_details[1]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_d, text=f"Contact: {profile_details[2]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_d, text=f"Blood Group: {profile_details[3]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_d, text=f"Email: {profile_details[4]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
            

def donorform():
    month = month_entry.get()
    bottle = bottle_entry.get()
    name = name_form_entry.get()
    id = id_form_entry.get()
    print(month, name, bottle)
    
    if bottle != 0:
        if connection:
            cursor = connection.cursor()
            # Use single quotes around string values in the SQL query
            query = f"UPDATE Reg SET bottle = {bottle} WHERE Name = '{name}' AND ID = {id}"
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("info", "Donate Successfully!")
            # cursor.close()
            home_d.tkraise()


# ============ universal array ================
id_array_a = []
email_array_a = []
name_array_a = []
bgroup_array_a = []
contact_array_a = []
pass_array_a= []
Bottle_array_a = []










# ============================= acceptor frame function =========================

def acceptor(): 
    profile_details = []
    em = email_donor.get()
    password = password_donor.get()
    for row in results:
        if em == row[4]:
            profile_details=row
    if em not in email_array:
        return messagebox.showerror("Error", "No user found with this email.")
    if pass_array[email_array.index(em)] != password:
        return  messagebox.showerror("Error", "Incorrect password.")
    selected_indices = disease_combobox.curselection()
    selected_diseases = [disease_options[index] for index in selected_indices]
    for i in selected_diseases:
        if i == "none":
            acceptor.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
            login_frame.place_forget()
            break
        else:
            login_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
            messagebox.showerror("Error", "Sorry! You are not able to donate/accept blood.")
           
    return profile_details
 

def showfilter_A():
    global id_array_a, email_array_a, name_array_a, bgroup_array_a, contact_array_a, pass_array_a
    compatibility = {
        "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
        "AB-": ["A-","B-","O-", "AB-"],
        "A-": ["O-", "A-"],
        "A+": ["O+", "A+","O-","A-"],
        "B-": ["O-", "B-"],
        "B+": ["O+", "B+","O-", "B-"],
        "O+": ["O-","O+"],
        "O-": ["O-"]
    }
    profile = donor_function()
    donor_blood_group = profile[3]
    print(donor_blood_group)
    filtered_data = [x for x in results if x[3] in compatibility.get(donor_blood_group, [])]
    id_array_a.clear()
    email_array_a.clear()
    name_array_a.clear()
    bgroup_array_a.clear()
    contact_array_a.clear()
    pass_array_a.clear()
    print(filtered_data)
    for row in filtered_data:
        id_array_a.append(row[0])
        email_array_a.append(row[4])
        name_array_a.append(row[1])
        bgroup_array_a.append(row[3])
        contact_array_a.append(row[2])
        pass_array_a.append(row[5])
        Bottle_array_a.append(row[6])
    tree2 = ttk.Treeview(home_a, columns=("ID", "Name", "Contact", "Blood Group", "Email", "Bottles"), show="headings")
    tree2.pack(expand=True, fill="both")

# Define column headings
    tree2.heading("ID", text="ID")
    tree2.heading("Name", text="Name")
    tree2.heading("Contact", text="Contact")
    tree2.heading("Blood Group", text="Blood Group")
    tree2.heading("Email", text="Email")
    tree2.heading("Bottles", text="Bottles")

# Set column widths
    tree2.column("ID", width=50)
    tree2.column("Name", width=120)
    tree2.column("Contact", width=80)
    tree2.column("Blood Group", width=60)
    tree2.column("Email", width=120)
    tree2.column("Bottles", width=40)

    for i in range(len(id_array_a)):
        tree2.insert("", "end", values=(id_array_a[i], name_array_a[i], contact_array_a[i], bgroup_array_a[i], email_array_a[i], Bottle_array_a[i]))

    scrollbar_y = ttk.Scrollbar(home_a, orient="vertical", command=tree2.yview)
    scrollbar_y.pack(side="right", fill="y")
    tree2.configure(yscrollcommand=scrollbar_y.set)


def show_graph():
    create_graph()
    plt.show()


def show_profile_A():
    profile_a.tkraise()
    profile_frame = tk.Frame(root)
    profile_frame.pack()
    profile_aetails = donor_function()
    if profile_aetails:
        label = tk.Label(profile_a, text=f"Id : {profile_aetails[0]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_a, text=f"Name: {profile_aetails[1]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_a, text=f"Contact: {profile_aetails[2]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_a, text=f"Blood Group: {profile_aetails[3]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="x")
        label = tk.Label(profile_a, text=f"Email: {profile_aetails[4]}", bg="red",fg="white", font=("Arial", 15))
        label.pack(fill="both")
             
def acceptorform():
    bottle = bottle_entry_a.get()
    name_A = name_form_entry_a.get()
    id_A = id_form_entry_a.get()
    print(bottle,name_A,id_A)
    for row in results:
        print(row[1],row[0])
        if name_A == row[1] and int(id_A) == row[0]:
            available_bottles = int(row[6])
            print(available_bottles)
            if available_bottles is None or available_bottles == 0 or available_bottles < int(bottle):
                messagebox.showerror("Error", "Blood not available or insufficient!")
            else:
                # Update donor's inventory
                new_available_bottles = available_bottles - int(bottle)
                
                donor_cursor =connection.cursor()
                donor_query = f"UPDATE Reg SET bottle = {new_available_bottles} WHERE Name = '{name_A}' AND ID = {id_A}"
                donor_cursor.execute(donor_query)
                connection.commit()
                donor_cursor.close()
                messagebox.showinfo("Info", "Blood Received Successfully!")
                home_d.tkraise()
                break


#  ============================= login screeen for user =========================================
login_frame = tk.Frame(root, bg="white", bd=5)
label = tk.Label(login_frame, text="LOGIN", fg="white", bg="black", font="Arial 25 bold")
label.pack(fill="x")

email_label = tk.Label(login_frame, text="Email:")
email_label.place(x=150, y=80)
email_donor = ttk.Entry(login_frame)
email_donor.place(x=250, y=80, width=200)

password_label = tk.Label(login_frame, text="Password:")
password_label.place(x=150, y=120)
password_donor = ttk.Entry(login_frame)
password_donor.place(x=250, y=120, width=200)

disease_label = tk.Label(login_frame, text="Any Disease:")
disease_label.place(x=150, y=160)
disease_options = ["none","HIV/AIDS","Hepatitis B or C","Syphilis","Malaria","Creutzfeldt-Jakob Disease (CJD)","Chagas Disease","HTLV (Human T-lymphotropic virus) Types I or II","Variant Creutzfeldt-Jakob Disease (vCJD)","Babesiosis","Zika Virus Infection"]
scrollbar = tk.Scrollbar(login_frame, orient=tk.VERTICAL)
disease_combobox = tk.Listbox(login_frame, selectmode=tk.MULTIPLE, height=6, yscrollcommand=scrollbar.set)
for option in disease_options:
    disease_combobox.insert(tk.END, option)
disease_combobox.place(x=250, y=160, width=200)
scrollbar.config(command=disease_combobox.yview)
scrollbar.place(x=450, y=160, height=110)

Donor = tk.Button(login_frame, text=" Donor", padx=20, pady=3, bg="red", font=20, foreground="white",command=donor_function)
Donor.place(x=140, y=290)

Acceptor = tk.Button(login_frame, text=" Accepter", padx=20, pady=3, bg="red", font=20, foreground="white",command=acceptor)
Acceptor.place(x=340, y=290)










# ========================================== donor FRame ==================================================

donor = tk.Frame(root, bg="white", bd=5)
label = tk.Label(donor, text="DONOR DASHBOARD", fg="white", bg="black", font="Arial 25 bold")
label.pack(fill="x")


#============ Dashboard Frame ==============
sidebar_frame = tk.Frame(donor, bg="red", width=100)
sidebar_frame.pack(side="left", fill="y")

dashboard_frame = tk.Frame(donor ,bg="white" , width=400)
dashboard_frame.pack(fill="y")

#=== home ======
home_d = tk.Frame(dashboard_frame, bg="white")
show= tk.Button(home_d, text="show user which are able to accept blood", fg="black", bg="white", font="Arial 10 bold",command=showfilter)
show.pack(fill="x")


# ======= donor form ============
form_d = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(form_d, text="DONOR FORM", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")

month_label = tk.Label(form_d, text="Date:", bg="white")
month_label.place(x=50, y=50)
options = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_entry = ttk.Combobox(form_d, values=options)
month_entry.place(x=150, y=50, width=200)

id_form_label = tk.Label(form_d, text="id:", bg="white")
id_form_label.place(x=50, y=80)
id_form_entry = ttk.Entry(form_d)
id_form_entry.place(x=150, y=80, width=200)

name_form_label = tk.Label(form_d, text="Name:", bg="white")
name_form_label.place(x=50, y=110)
name_form_entry = ttk.Entry(form_d)
name_form_entry.place(x=150, y=110, width=200)

bottle_label = tk.Label(form_d, text="Bottle:", bg="white")
bottle_label.place(x=50, y=140)
options = ['1','2','3']
bottle_entry = ttk.Combobox(form_d, values=options)
bottle_entry.place(x=150, y=140, width=200)

save_button = tk.Button(form_d, text="Donote", padx=20, pady=3, bg="red", font=20, foreground="white",command=donorform)
save_button.place(x=80, y=180)

exit_button = tk.Button(form_d, padx=20, pady=3, bg="red", font=20, foreground="white", text="Exit", command=exit_form)
exit_button.place(x=210,y=180)

# ========= history ===============
history_d = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(history_d, text="History", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")
show_graph = tk.Button(history_d, text="Show Graph for donors", command=create_graph2)
show_graph.pack(pady=10)


# ============== profile =====================
profile_d = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(profile_d, text="Profile", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")

# gird veiw
home_d.grid(row=0, column=0, sticky="nsew")
profile_d.grid(row=0, column=0, sticky="nsew")
history_d.grid(row=0, column=0, sticky="nsew")
form_d.grid(row=0, column=0, sticky="nsew")
# sidebar
button1 = tk.Button(sidebar_frame, text="Home", command=lambda: show_panel(home_d))
button1.pack(fill="x", padx=10, pady=5)
button3 = tk.Button(sidebar_frame, text="History", command=lambda: show_panel(history_d))
button3.pack(fill="x", padx=10, pady=5)
button4 = tk.Button(sidebar_frame, text="Profile", command=show_profile)
button4.pack(fill="x", padx=10, pady=5)
button2 = tk.Button(sidebar_frame, text="Donor Form", command=lambda: show_panel(form_d))
button2.pack(fill="x", padx=10, pady=5)
button5 = tk.Button(sidebar_frame, text="Logout", command=logout_d)
button5.pack(fill="x", padx=10, pady=5)












# ================================================= acceptor frame ====================================
acceptor = tk.Frame(root, bg="white", bd=5)
label = tk.Label(acceptor, text="ACCEPTOR DASHBOARD", fg="white", bg="black", font="Arial 25 bold")
label.pack(fill="x")
#============ Dashboard Frame ==============
sidebar_frame = tk.Frame(acceptor, bg="red", width=100)
sidebar_frame.pack(side="left", fill="y")

dashboard_frame = tk.Frame(acceptor ,bg="white" , width=400 )
dashboard_frame.pack()

#=== home ======
home_a= tk.Frame(dashboard_frame, bg="white")
show= tk.Button(home_a, text="show user which are able to accept blood", fg="black", bg="white", font="Arial 10 bold",command=showfilter_A)
show.pack(fill="x")

# ======= acceptor form ============
form_a = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(form_a, text="Acceptor Form", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")

id_form_label_a = tk.Label(form_a, text="id:", bg="white")
id_form_label_a.place(x=50, y=80)
id_form_entry_a = ttk.Entry(form_a)
id_form_entry_a.place(x=150, y=80, width=200)

name_form_label_a = tk.Label(form_a, text="Name:", bg="white")
name_form_label_a.place(x=50, y=110)
name_form_entry_a = ttk.Entry(form_a)
name_form_entry_a.place(x=150, y=110, width=200)

bottle_label_a = tk.Label(form_a, text="Bottle:", bg="white")
bottle_label_a.place(x=50, y=140)
options_a = ['1','2','3']
bottle_entry_a = ttk.Combobox(form_a, values=options_a)
bottle_entry_a.place(x=150, y=140, width=200)

save_button = tk.Button(form_a, text="Receive", padx=20, pady=3, bg="red", font=20, foreground="white",command=acceptorform)
save_button.place(x=80, y=180)

exit_button = tk.Button(form_a, padx=20, pady=3, bg="red", font=20, foreground="white", text="Exit", command=exit_form)
exit_button.place(x=210,y=180)



# ========= history ===============
history_a = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(history_a, text="History", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")
show_graph = tk.Button(history_a, text="Show Graph for donors", command=create_graph2)
show_graph.pack(pady=10)


# ============== profile =====================
profile_a = tk.Frame(dashboard_frame, bg="white")
label = tk.Label(profile_a, text="Profile", fg="black", bg="white", font="Arial 10 bold")
label.pack(fill="x")

# gird veiw
home_a.grid(row=0, column=0, sticky="nsew")
profile_a.grid(row=0, column=0, sticky="nsew")
history_a.grid(row=0, column=0, sticky="nsew")
form_a.grid(row=0, column=0, sticky="nsew")
# sidebar
button1 = tk.Button(sidebar_frame, text="Home", command=lambda: show_panel(home_a))
button1.pack(fill="x", padx=10, pady=5)
button3 = tk.Button(sidebar_frame, text="History", command=lambda: show_panel(history_a))
button3.pack(fill="x", padx=10, pady=5)
button4 = tk.Button(sidebar_frame, text="Profile", command=show_profile_A)
button4.pack(fill="x", padx=10, pady=5)
button2 = tk.Button(sidebar_frame, text="Acceptor Form", command=lambda: show_panel(form_a))
button2.pack(fill="x", padx=10, pady=5)
button5 = tk.Button(sidebar_frame, text="Logout", command=logout_a)
button5.pack(fill="x", padx=10, pady=5)

root.mainloop()
