compile: dsdt.aml

.PHONY: extract extract_ssdt
extract: dsdt.dat

dsdt.dat:
	cat /sys/firmware/acpi/tables/DSDT > dsdt.dat

extract_ssdt:
	for i in /sys/firmware/acpi/tables/SSDT*; do \
		name=$$(basename $$i); \
		sudo cat $$i > $${name,,}.dat; \
	done

patch132: dsdt.dsl
	patch -p1 < x1t3.patch

patch135: dsdt.dsl
	patch -p1 < x1t3_v1.35.patch

patch149: dsdt.dsl
	patch -p1 < x1t3_v1.49.patch

.PHONY: install
install: 
	echo acpi_override="yes" > /etc/dracut.conf.d/acpi_override.conf
	echo acpi_table_dir="/etc/dracut.conf.d/acpi_tables/" >> /etc/dracut.conf.d/acpi_override.conf
	mkdir -p /etc/dracut.conf.d/acpi_tables/
	cp dsdt.aml /etc/dracut.conf.d/acpi_tables/
	dracut --regenerate-all -f
	grubby --args=mem_sleep_default=deep --update-kernel=ALL

%.dsl: %.dat
	iasl  -d $<

%.aml: %.dsl
	iasl -tc $<
