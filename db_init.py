from app.hash import generate_password_hash
from app.services import session_scope
from app.models import (
    User,
    Role,
    Permission,
)


with session_scope() as session:
    # Permissions
    users_edit = Permission(code='users:edit', name='Редактирование пользователей')
    users_view = Permission(code='users:view', name='Просмотр пользователей')
    session.add_all([
        users_edit, users_view
    ])

    # Roles
    admin_role = Role(
        code='admin', 
        name='Администратор системы',
        permissions=[users_edit, users_view]
    )
    user_role = Role(
        code='user', 
        name='Пользователь',
        permissions=[]
    )
    session.add_all([
        admin_role, user_role
    ])

    # Users
    admin = User(
        login='admin', 
        password_hash=generate_password_hash('admin').hex(),
        role=admin_role
    )
    user = User(
        login='user', 
        password_hash=generate_password_hash('user').hex(),
        role=user_role
    )
    session.add_all([
        admin, user
    ])
    session.commit()
