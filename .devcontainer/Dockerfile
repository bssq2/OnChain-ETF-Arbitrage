# Starts from the same image declared in devcontainer.json
ARG VARIANT=20
FROM mcr.microsoft.com/devcontainers/javascript-node:${VARIANT}

# Example: install libssl if some npm module needs it
RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*