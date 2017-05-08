UNAME:=$(shell uname -s)
ifeq ($(UNAME),Linux)
	VIEWER=xdg-open
endif
ifeq ($(UNAME), Darwin)
	VIEWER=open -a Preview
endif

.PHONY: compile, view

compile: poster.pdf 

%.pdf: %.tex Makefile
	pdflatex --enable-write18 $< &&	pdflatex $< && pdflatex $<

view: compile
	$(VIEWER) poster.pdf
clean:
	rm -f *.aux	*.bbl	*.blg	*.log	poster.pdf 
