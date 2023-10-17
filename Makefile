MAIN=src/main.py
FLAGS=-B

.PHONY: test compile
test:
	mkdir -p test
	rm -rf test
	mkdir test
	python3 $(FLAGS) $(MAIN)

compile:
	echo COMPILE DEEZ NUTZ

clean:
	rm -rf test
	mkdir test
