# mongo image as base
FROM mongo:latest

# update package and install python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip 

# copy requirements.txt
COPY requirements.txt /usr/src/app/

RUN pip3 install -r /usr/src/app/requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

# making init executable
RUN chmod +x init.sh 

EXPOSE 5000

CMD ["./init.sh"]