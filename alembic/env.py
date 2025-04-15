import sys
from pathlib import Path
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context

# Добавляем путь к проекту
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database import Base
from app.models import Game, User, Alert  # Импортируем модели для миграций

# Настройка для Alembic
config = context.config
target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск миграций в оффлайн-режиме"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в онлайне"""
    connectable = engine_from_config(config.get_section(config.config_ini_section),
                                     prefix='sqlalchemy.',
                                     poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
