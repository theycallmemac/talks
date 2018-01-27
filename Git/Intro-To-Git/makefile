
targets  = Factorial.class

build: $(targets)
	@true

%.class: %.java
	javac $<

test:
	$(MAKE) build
	for script in tests/*.sh; do sh $$script && echo "$$script passed\n" || echo -e "$$script failed\n" && exit 1; done

clean:
	rm -fv $(targets)


