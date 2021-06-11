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
    permissions_view = Permission(
        code='permissions:view',
        name='Просмотр разрешений'
    )
    roles_edit = Permission(
        code='roles:edit',
        name='Редактирование ролей'
    )
    roles_view = Permission(
        code='roles:view',
        name='Просмотр ролей'
    )
    users_edit = Permission(
        code='users:edit',
        name='Редактирование пользователей'
    )
    users_view = Permission(
        code='users:view',
        name='Просмотр пользователей'
    )
    patients_edit = Permission(
        code='patients:edit',
        name='Редактирование пациентов'
    )
    patients_view = Permission(
        code='patients:view',
        name='Просмотр пациентов'
    )
    examinations_edit = Permission(
        code='examinations:edit',
        name='Редактирование общих осмотров'
    )
    examinations_view = Permission(
        code='examinations:view',
        name='Просмотр общих осмотров'
    )
    therapist_examinations_edit = Permission(
        code='examinations:therapist:edit',
        name='Редактирование терапевтических осмотров'
    )
    therapist_examinations_view = Permission(
        code='examinations:therapist:view',
        name='Просмотр терапевтических осмотров'
    )
    surgeon_examinations_edit = Permission(
        code='examinations:surgeon:edit',
        name='Редактирование хирургических осмотров'
    )
    surgeon_examinations_view = Permission(
        code='examinations:surgeon:view',
        name='Просмотр хирургических осмотров'
    )
    orthopedist_examinations_edit = Permission(
        code='examinations:orthopedist:edit',
        name='Редактирование ортопедических осмотров'
    )
    orthopedist_examinations_view = Permission(
        code='examinations:orthopedist:view',
        name='Просмотр ортопедических осмотров'
    )
    researches_edit = Permission(
        code='researches:edit',
        name='Редактирование исследований'
    )
    researches_view = Permission(
        code='researches:view',
        name='Просмотр исследований'
    )
    session.add_all([
        permissions_view,
        roles_edit, roles_view,
        users_edit, users_view,
        patients_edit, patients_view,
        examinations_edit, examinations_view,
        therapist_examinations_edit, therapist_examinations_view,
        surgeon_examinations_edit, surgeon_examinations_view,
        orthopedist_examinations_edit, orthopedist_examinations_view,
        researches_edit, researches_view
    ])

    # Roles
    admin_role = Role(
        code='admin',
        name='Администратор системы',
        permissions=[
            permissions_view,
            roles_edit, roles_view,
            users_edit, users_view,
            patients_edit, patients_view,
            examinations_edit, examinations_view,
            therapist_examinations_edit, therapist_examinations_view,
            surgeon_examinations_edit, surgeon_examinations_view,
            orthopedist_examinations_edit, orthopedist_examinations_view,
            researches_edit, researches_view
        ]
    )
    head_physician_role = Role(
        code='head_physician',
        name='Главный врач',
        permissions=[
            permissions_view,
            roles_view,
            users_edit, users_view,
            patients_view,
            examinations_view,
            therapist_examinations_view,
            surgeon_examinations_view,
            orthopedist_examinations_view,
            researches_view
        ]
    )
    therapist_role = Role(
        code='therapist',
        name='Врач-терапевт',
        permissions=[
            patients_view,
            examinations_view, examinations_edit,
            therapist_examinations_edit, therapist_examinations_view,
            researches_edit, researches_view
        ]
    )
    surgeon_role = Role(
        code='surgeon',
        name='Врач-хирург',
        permissions=[
            patients_view,
            examinations_view, examinations_edit,
            surgeon_examinations_edit, surgeon_examinations_view,
            researches_edit, researches_view
        ]
    )
    orthopedist_role = Role(
        code='orthopedist',
        name='Врач-ортопед',
        permissions=[
            patients_view,
            examinations_view, examinations_edit,
            orthopedist_examinations_edit, orthopedist_examinations_view,
            researches_edit, researches_view
        ]
    )
    administrator_role = Role(
        code='administrator',
        name='Администратор',
        permissions=[
            patients_edit, patients_view,
        ]
    )
    session.add_all([
        admin_role,
        head_physician_role,
        therapist_role,
        surgeon_role,
        orthopedist_role,
        administrator_role,
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
    therapist = User(
        login='therapist',
        password_hash=generate_password_hash('therapist').hex(),
        role=therapist_role,
        first_name='Доктор',
        surname='Терапедов',
    )
    surgeon = User(
        login='surgeon',
        password_hash=generate_password_hash('surgeon').hex(),
        role=surgeon_role,
        first_name='Доктор',
        surname='Хирургов',
    )
    orthopedist = User(
        login='orthopedist',
        password_hash=generate_password_hash('orthopedist').hex(),
        role=orthopedist_role,
        first_name='Доктор',
        surname='Ортопедов',
    )
    administrator = User(
        login='administrator',
        password_hash=generate_password_hash('administrator').hex(),
        role=administrator_role,
        first_name='Администратор',
        surname='Администраторов',
    )
    session.add_all([
        admin,
        head,
        therapist,
        surgeon,
        orthopedist,
        administrator,
    ])
    session.commit()
