FROM repo.inboc.net/inboc/ubuntu:latest-py3.10.12

USER inboc
ENV HOME=/home/inboc
ARG PACKAGE_NAME
ARG PYPI_TOKEN
ARG PYPI_USER
ARG PACKAGE_PATH=$HOME/source/$PACKAGE_NAME
RUN mkdir -p $PACKAGE_PATH
COPY requirements.txt $PACKAGE_PATH
RUN pip install -r $PACKAGE_PATH/requirements.txt -i https://$INBOC_DEV_PYPI_USER:$INBOC_DEV_PYPI_TOKEN@gitlab.inboc.net/api/v4/projects/93/packages/pypi/simple  --extra-index-url https://nexus.inboc.net/repository/pypi/simple

USER root
COPY . $PACKAGE_PATH
RUN chown -R inboc:inboc $PACKAGE_PATH

USER inboc
CMD [ "/bin/bash" ]