FROM node:22.6.0-slim

# Create a group and user to run app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init --create-home -r -g ${APP_USER} ${APP_USER}

# Install packages needed to run application (not build deps):
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN /bin/bash -c 'set -ex \
    && RUN_DEPS=" \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*'

# Create project directory
ARG APP_DIR=/home/${APP_USER}/ccio
RUN mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}

# Copy requirements and application code and grant them execute permissions
COPY --chown=${APP_USER}:${APP_USER} ./ ${APP_DIR}
RUN chmod +x  \
    ${APP_DIR}/scripts/entrypoint.sh \
    ${APP_DIR}/scripts/start_local.sh \
    ${APP_DIR}/scripts/start.sh

# Set the working directory
WORKDIR ${APP_DIR}

RUN /bin/bash -c 'set -euo pipefail \
    && BUILD_DEPS=" \
    python3 \
    build-essential \
    git \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && npm install -g @angular/cli@18.1.4 \
    && npm install \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*'

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

ENTRYPOINT ["./scripts/entrypoint.sh"]
