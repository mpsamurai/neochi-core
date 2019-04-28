FROM mpsamurai/neochi-dev-base:20190424-x64

WORKDIR /code
COPY ./src .
CMD ["python", "main.py"]
