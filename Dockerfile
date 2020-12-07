# using Alpine Edge
FROM mrmiss/userbutt:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/keselekpermen69/userbutt /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

# Make open port TCP
EXPOSE 80 443

CMD ["python3","-m","userbot"]
