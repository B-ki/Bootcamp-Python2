all: 
	python3.10 -m venv venv
	( \
		. ./venv/bin/activate && \
		if [ ! -f requirements.txt ]; then \
			echo "No requirements.txt found, skipping installation."; \
		else \
			pip install --upgrade pip && \
			pip install -r requirements.txt; \
		fi \
	)

clean:
	rm -rf venv

fclean: clean

re: fclean all

.PHONY: all clean fclean re
