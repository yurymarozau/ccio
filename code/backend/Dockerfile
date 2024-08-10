FROM python:3.12.5-slim

# do not buffer output
ENV PYTHONUNBUFFERED 1

# do not write pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Create a group and user to run app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init --create-home -r -g ${APP_USER} ${APP_USER}

# Install packages needed to run application (not build deps):
#   gettext -- for django localization
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN /bin/bash -c 'set -ex \
    && RUN_DEPS=" \
    gettext \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*'

# Create project directory
ARG APP_DIR=/home/${APP_USER}/ccio
RUN mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}

# Copy requirements and application code and grant them execute permissions
COPY --chown=${APP_USER}:${APP_USER} ./requirements.txt ./src/ ${APP_DIR}
RUN chmod +x  \
    ${APP_DIR}/scripts/entrypoint.sh \
    ${APP_DIR}/scripts/wait-for-it.sh \
    ${APP_DIR}/scripts/migrate.sh \
    ${APP_DIR}/scripts/start_local.sh \
    ${APP_DIR}/scripts/start.sh

# Install python requirements
RUN /bin/bash -c 'set -euo pipefail \
    && BUILD_DEPS=" \
    gcc \
    g++ \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip3 install --no-cache-dir -r ${APP_DIR}/requirements.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*'

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

# Set the working directory
WORKDIR ${APP_DIR}

ENTRYPOINT ["./scripts/entrypoint.sh"]
