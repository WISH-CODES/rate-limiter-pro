import os
import sys
from logging.config import fileConfig
from dotenv import load_dotenv

from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context

# Ensure project root is in sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_dir)

# Load environment variables
load_dotenv(os.path.join(project_dir, ".env"))

# Alembic config object
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import Base metadata
from app.models import Base
target_metadata = Base.metadata

# Get sync DB URL for Alembic migrations
SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")
if not SYNC_DATABASE_URL:
    raise RuntimeError("SYNC_DATABASE_URL is not set in .env")

# Override sqlalchemy.url
config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=SYNC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(SYNC_DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
