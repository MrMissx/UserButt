# using Alpine Edge
FROM mrmiss/userbutt:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b staging https://github.com/keselekpermen69/userbutt /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

CMD ["python3","-m","userbot"]
