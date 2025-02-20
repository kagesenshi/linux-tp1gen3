# Linux support patches for Lenovo X1 Tablet 3rd generation


## ACPI Patches

**Caution**: These steps will modify your computers firmware. This may break your device and/or attached hardware.

For S3 sleep state and the power/volume buttons of the device to work the ACPI DSDT tables must be modified. The patches contained in this repository
incorporate the information from the [Delta-Xi Blog][dxi]

Prerequisites:
 - Intel ACPI Source Language compiler which is usually provided by the acpica or acpica-tools package
 - make
 - one of the following BIOS versions:
   - N1ZET76W (1.32)
   - N1ZET79W (1.35)
   - N1ZET93W (1.49)
   
   other versions may work but may also require changes to the patch. The current BIOS version can be checked via
   ```
   sudo dmidecode  --string "bios-version"
   ```
 - A Lenovo X1 Tablet 3rd Generation. To check if you have one of these devices you may run
   ```
   sudo dmidecode  --string "system-product-name"
   ```
   The output should beginn, according to the lenovo website with "20KJ" or "20KK". The device the patch was tested on returned "20KJ001NGE".

To apply the ACPI patches change to the acpi subdirectory and run make with the appropriate patch for your BIOS version.
Choose between `patch149` for version "1.49", `patch132` for version "1.32" and `patch135` for version "1.35".

```{.sh}
cd acpi
sudo make dsdt.dat
make patch149 compile
sudo make install
```

The patch should apply cleanly. If not you may patch the dsdt.dsl file by hand.
Finally add the acpi_override file as another initrd to your bootloader configuration.

## Removed items (newer kernels handle it correctly)

- hid-multitouch patches 
- hid-lenovo patches

## Contributions
Thanks goes to
 * [bitbacchus](https://github.com/bitbacchus) for writing the Ubuntu Installation section
 * [parenthetical](https://github.com/parenthetical) for providing the BIOS patch for version 1.35


## Additional Information

 * [intel hid module description (aka the volume buttons) ](https://lkml.org/lkml/2018/6/28/636)
 * [Kernel sleep state information](https://www.kernel.org/doc/html/v4.15/admin-guide/pm/sleep-states.html)
 * [Arch Linux Wiki on using the generated apci_override and DSDT in general](https://wiki.archlinux.org/index.php/DSDT#Using_a_CPIO_archive)

[dxi]: https://delta-xi.net/blog/#056 "Delta-Xi Blog"
[hid-lenovo]: https://github.com/torvalds/linux/blob/9f7582d15f82e86b2041ab22327b7d769e061c1f/drivers/hid/hid-lenovo.c "Linux hid-lenovo module sourcecode"
[hid-multitouch]: https://github.com/torvalds/linux/blob/9f7582d15f82e86b2041ab22327b7d769e061c1f/drivers/hid/hid-multitouch.c "Linux hid-multitouch module sourcecode"
[hid-lenovo-patches]: https://www.spinics.net/linux/fedora/linux-sound/msg00626.html "hid-lenovo: Add support for X1 Tablet special keys and LED control"
[aw-blacklisting]: https://wiki.archlinux.org/index.php/Kernel_module#Blacklisting
[poinstick-issue]: https://github.com/Lunm0us/linux-tp1gen3/issues/2

