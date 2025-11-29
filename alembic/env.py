from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import Base from models
from app.models import Base  # Adjust according to your app's structure
from app.database import DATABASE_URL  # Import the sync database URL

config = context.config

# Set up logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Use models' metadata
target_metadata = Base.metadata
# Set the SQLAlchemy URL for Alembic
config.set_main_option('sqlalchemy.url', DATABASE_URL)

def run_migrations_online():
    # Create synchronous engine for Alembic
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    # Run migrations
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        # Run migrations
        with context.begin_transaction():
            context.run_migrations()

# If we are running online migrations (default), use the function defined above
if context.is_offline_mode():
    # If running offline mode, use the URL directly
    context.configure(url=DATABASE_URL, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()
else:
    # If running online, use the online function
    run_migrations_online()
