from app.hash import generate_password_hash
from app.services import session_scope
from app.models import (
    User,
    Role,
    Permission,
)


with session_scope() as session:
    # https://docs.google.com/spreadsheets/d/1gn1_ilyrgJIaMEI0fL8TGaDO6ZYDnluiyFQ0nKIgMVU
    # Permissions
    permissions_view = Permission(code='permissions:view', name='Просмотр разрешений')
    roles_edit = Permission(code='roles:edit', name='Редактирование ролей')
    roles_view = Permission(code='roles:view', name='Просмотр ролей')
    users_edit = Permission(code='users:edit', name='Редактирование пользователей')
    users_view = Permission(code='users:view', name='Просмотр пользователей')
    session.add_all([
        permissions_view,
        roles_edit, roles_view,
        users_edit, users_view,
    ])

    # Roles
    admin_role = Role(
        code='admin', 
        name='Администратор системы',
        permissions=[
            permissions_view,
            roles_edit, roles_view,
            users_edit, users_view,
        ]
    )
    head_physician_role = Role(
        code='head_physician', 
        name='Главный врач',
        permissions=[
            permissions_view,
            roles_view,
            users_edit, users_view,
        ]
    )
    physician_role = Role(
        code='physician', 
        name='Врач',
        permissions=[]
    )
    administrator_role = Role(
        code='administrator', 
        name='Администратор',
        permissions=[]
    )
    session.add_all([
        admin_role, head_physician_role, physician_role, administrator_role
    ])

    # Users
    admin = User(
        login='admin', 
        password_hash=generate_password_hash('admin').hex(),
        role=admin_role,
        first_name='Админ',
        surname='Админов',
    )
    head = User(
        login='head', 
        password_hash=generate_password_hash('head').hex(),
        role=head_physician_role,
        first_name='Глава',
        surname='Глав',
    )
    doctor = User(
        login='doctor', 
        password_hash=generate_password_hash('doctor').hex(),
        role=physician_role,
        first_name='Доктор',
        surname='Докторов',
    )
    administrator = User(
        login='administrator', 
        password_hash=generate_password_hash('administrator').hex(),
        role=administrator_role,
        first_name='Администратор',
        surname='Администраторов',
    )
    session.add_all([
        admin, head, doctor, administrator
    ])
    session.commit()
