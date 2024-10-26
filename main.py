from user_credentials import app, db, register, login, dashboard, logout

with app.app_context() :
    db.create_all()
    print("Database tables created successfully!")  