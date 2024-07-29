import tkinter as tk
from tkinter import messagebox

# Giả sử chúng ta có một danh sách lưu trữ thông tin tài khoản
users = {"admin": {"password": "password", "email": "admin@example.com"}}

# Hàm xác minh thông tin đăng nhập
def login():
    email = entry_email.get()
    password = entry_password.get()

    for user, info in users.items():
        if info["email"] == email and info["password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {user}!")
            return
    messagebox.showerror("Login Failed", "Invalid email or password")

# Hàm mở cửa sổ đăng ký
def open_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    tk.Label(register_window, text="Username:").pack(pady=5)
    new_username_entry = tk.Entry(register_window)
    new_username_entry.pack(pady=5)

    tk.Label(register_window, text="Password:").pack(pady=5)
    new_password_entry = tk.Entry(register_window, show="*")
    new_password_entry.pack(pady=5)

    tk.Label(register_window, text="Email:").pack(pady=5)
    new_email_entry = tk.Entry(register_window)
    new_email_entry.pack(pady=5)

    def register():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        new_email = new_email_entry.get()

        if new_username in users:
            messagebox.showerror("Registration Failed", "Username already exists")
        else:
            users[new_username] = {"password": new_password, "email": new_email}
            messagebox.showinfo("Registration Successful", "Account created successfully!")
            register_window.destroy()

    tk.Button(register_window, text="Register", command=register).pack(pady=20)

# Hàm mở cửa sổ quên mật khẩu
def open_forgot_password_window():
    forgot_password_window = tk.Toplevel(root)
    forgot_password_window.title("Forgot Your Password?")

    tk.Label(forgot_password_window, text="Your email address:").pack(pady=5)
    email_entry = tk.Entry(forgot_password_window)
    email_entry.pack(pady=5)

    def submit_forgot_password():
        email = email_entry.get()
        for user, info in users.items():
            if info["email"] == email:
                messagebox.showinfo("Password Reset", "A password reset link has been sent to your email.")
                forgot_password_window.destroy()
                return
        messagebox.showerror("Email Not Found", "The email address is not registered.")
        
    tk.Button(forgot_password_window, text="Submit", command=submit_forgot_password).pack(pady=20)
    tk.Button(forgot_password_window, text="Cancel", command=forgot_password_window.destroy).pack(pady=5)

# Tạo cửa sổ chính
root = tk.Tk()
root.geometry("500x300")
root.title("Login Form")

# Tạo frame cho form đăng nhập
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Tạo các label và entry cho form đăng nhập
tk.Label(login_frame, text="Email:", font="ar 12").grid(row=0, column=0, padx=10, pady=10)
entry_email = tk.Entry(login_frame, font="ar 12")
entry_email.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_frame, text="Password:", font="ar 12").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(login_frame, show="*", font="ar 12")
entry_password.grid(row=1, column=1, padx=10, pady=10)

remember_me_var = tk.BooleanVar()
remember_me_checkbox = tk.Checkbutton(login_frame, text="Remember me", variable=remember_me_var)
remember_me_checkbox.grid(row=2, columnspan=2, pady=10)

# Tạo nút đăng nhập
login_button = tk.Button(login_frame, text="SIGN IN", command=login, font="ar 12", bg="blue", fg="white")
login_button.grid(row=3, columnspan=2, pady=10)

# Tạo các liên kết "Forgot your password?" và "Create an account"
forgot_password_label = tk.Label(login_frame, text="Forgot your password?", fg="blue", cursor="hand2")
forgot_password_label.grid(row=4, columnspan=2, pady=5)
forgot_password_label.bind("<Button-1>", lambda e: open_forgot_password_window())

create_account_label = tk.Label(login_frame, text="Create an account", fg="blue", cursor="hand2")
create_account_label.grid(row=5, columnspan=2, pady=5)
create_account_label.bind("<Button-1>", lambda e: open_register_window())

# Tạo khung dưới cho nút đăng ký
register_frame = tk.Frame(root)
register_frame.pack(pady=20)

# Tạo nhãn và nút đăng ký
tk.Label(register_frame, text="Not a registered user yet?", font="ar 12 bold").pack(pady=5)
tk.Button(register_frame, text="REGISTER", command=open_register_window, font="ar 12", bg="blue", fg="white").pack(pady=10)

# Bắt đầu vòng lặp chính
root.mainloop()
