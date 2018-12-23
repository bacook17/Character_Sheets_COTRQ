all: sota celadin korth macaw zor zeed merry

clobber:
	-rm *.pdf

rm_sota:
	-rm sota.pdf

rm_celadin:
	-rm celadin.pdf

rm_korth:
	-rm korth.pdf

rm_macaw:
	-rm macaw.pdf

rm_zor:
	-rm zor.pdf

rm_zeed:
	-rm zeed.pdf

rm_merry:
	-rm merry.pdf

sota: rm_sota sota.pdf

celadin: rm_celadin celadin.pdf

korth: rm_korth korth.pdf

macaw: rm_macaw macaw.pdf

zor: rm_zor zor.pdf

zeed: rm_zeed zeed.pdf

merry: rm_merry merry.pdf

%.pdf: %.py
	makesheets $<
