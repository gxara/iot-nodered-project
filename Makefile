
develop:
	docker run -it -p 1880:1880 -v nodered_data:/data --name mynodered nodered/node-red

stop:
	docker stop mynodered

clean:
	@make stop
	docker rm mynodered