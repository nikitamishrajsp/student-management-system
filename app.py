from student_management.db import ping
from student_management.auth import ensure_admin, login
from student_management.students import menu as students_menu
from student_management.academics import courses_menu, attendance_menu, marks_menu, fees_menu
from student_management.reports import dashboard, export_students_csv
from student_management.ui import header, pause

def main():
    try:
        ping()
        ensure_admin()
    except Exception as exc:
        print("\nDatabase connection failed.")
        print("Check MySQL is running, import database/schema.sql, and verify your .env settings.")
        print("Details:", exc)
        return

    user=login()
    if not user:
        print("Too many failed login attempts. Exiting.")
        return

    while True:
        header(f"STUDENT MANAGEMENT SYSTEM | Signed in: {user['username']} ({user['role']})")
        print("1. Dashboard\n2. Student management\n3. Course management")
        print("4. Attendance\n5. Marks\n6. Fee management\n7. Export students to CSV")
        print("0. Exit")
        choice=input("Select an option: ").strip()
        try:
            if choice=="1": dashboard(); pause()
            elif choice=="2": students_menu()
            elif choice=="3": courses_menu()
            elif choice=="4": attendance_menu()
            elif choice=="5": marks_menu()
            elif choice=="6": fees_menu()
            elif choice=="7": export_students_csv(); pause()
            elif choice=="0":
                print("Logged out. Goodbye.")
                break
            else:
                print("Invalid option."); pause()
        except Exception as exc:
            print("Unexpected error:",exc); pause()

if __name__=="__main__":
    main()
