MAIN=src/main.py
FLAGS=-B

.PHONY: test
test:
	mkdir -p test
	rm -rf test
	mkdir test
	python3 $(FLAGS) $(MAIN)

clean:
	rm -rf test
	mkdir test
