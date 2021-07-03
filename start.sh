docker run -i -t \
--mount type=bind,source="$(pwd)"/src,target=/app \
cv-counter