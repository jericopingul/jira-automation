FROM python:3
ADD main.py /
RUN pip install asyncio
RUN pip install jira
CMD [ "python", "./main.py"]