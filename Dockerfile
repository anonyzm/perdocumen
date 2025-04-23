FROM python:3.13.3-alpine3.21

RUN apk add --no-cache git

RUN mkdir /opt/perdocumen  \
    && mkdir /opt/codebase  \
    && mkdir /opt/tutorial  \
    && cd /opt/perdocumen  \
    && git clone https://github.com/The-Pocket/Tutorial-Codebase-Knowledge.git . \
    && pip install -r requirements.txt

RUN pip install openai

COPY call_llm.py /opt/perdocumen/utils/call_llm.py

RUN chmod +x /opt/perdocumen/main.py

#ENTRYPOINT ["python"]
CMD ["python", "/opt/perdocumen/main.py", "--dir", "/opt/codebase", "--output", "/opt/tutorial", "--max-size", "70000", "--include"]