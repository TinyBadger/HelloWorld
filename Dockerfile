FROM python:3
ADD HelloWorld.py /
ADD Const.py /
CMD ["python", "./HelloWorld.py"]