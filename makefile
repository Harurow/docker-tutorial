.PHONY: start stop clean restart

start:
	docker compose up -d

stop:
	docker compose down

clean:
	docker compose down --rmi all --volumes --remove-orphans

restart:
	make clean
	make start
